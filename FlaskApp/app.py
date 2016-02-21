#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request, jsonify
import json

app = Flask(__name__)


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
