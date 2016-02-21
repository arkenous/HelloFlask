#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request, jsonify
import json
from flask import session, redirect, url_for
import os

app = Flask(__name__)
# cookieを暗号化する秘密鍵
app.config['SECRET_KEY'] = os.urandom(24)


# 各route関数の前に実行される処理
@app.before_request
def before_request():
    # セッションにusernameが保存されている．つまりログイン済み
    if session.get('username') is not None:
        return
    # リクエストパスがログインページに関する場合
    if request.path == '/login':
        return
    # ログインされておらず，ログインページに関するリクエストでない場合
    return redirect('/login')


# ログイン処理を行う
@app.route('/login', methods=['GET', 'POST'])
def login():
    # ログイン処理
    if request.method == 'POST' and _is_account_valid():
        # セッションにユーザ名を保存してからトップページにリダイレクト
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    # ログインページに戻る
    return render_template('login.html')


# 個人認証を行い，正規のアカウントか確認する
def _is_account_valid():
    username = request.form.get('username')
    # この例では，ユーザ名にadminが指定されていれば正規のアカウントであるとみなしている
    # ここで具体的な個人認証処理を行う．認証に成功であればTrueを返すようにする
    if username == 'admin':
        return True
    return False


# ログアウト処理を行う
@app.route('/logout')
def logout():
    # セッションからusernameを取り出す
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/postText', methods=['POST'])
def lower_conversion():
    text = request.json['text']
    if "ping" in text:
        return_data = {"result":"pong"}
        return jsonify(ResultSet=json.dumps(return_data))
    lower_text = text.lower()
    return_data = {"result":lower_text}
    return jsonify(ResultSet=json.dumps(return_data))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
