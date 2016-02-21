#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_, ok_
from FlaskApp import app
import json

app.testing = True
client = app.app.test_client()


def test_get_index():
    res = client.get('/')
    eq_(302, res.status_code)
    ok_('/login' in res.headers['Location'])


def test_get_login():
    res = client.get('/login')
    eq_(200, res.status_code)


def test_fail_login():
    res = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    })
    eq_(200, res.status_code)


def test_login():
    res = client.post('/login', data={
        'username': 'admin',
        'password': 'testpassword'
    })
    eq_(302, res.status_code)


def test_post_hoge():
    res = client.post('/postText',
                      data=json.dumps(dict(text='hoge')),
                      content_type='application/json')
    eq_(200, res.status_code)
    data = json.loads(json.loads(res.data.decode('utf-8'))['ResultSet'])
    eq_('hoge', data['result'])


def test_post_HOGE():
    res = client.post('/postText',
                      data=json.dumps(dict(text='HOGE')),
                      content_type='application/json')
    eq_(200, res.status_code)
    data = json.loads(json.loads(res.data.decode('utf-8'))['ResultSet'])
    eq_('hoge', data['result'])


def test_post_ping():
    res = client.post('/postText',
                      data=json.dumps(dict(text='ping')),
                      content_type='application/json')
    eq_(200, res.status_code)
    data = json.loads(json.loads(res.data.decode('utf-8'))['ResultSet'])
    eq_('pong', data['result'])


def test_logout():
    res = client.get('/logout')
    eq_(302, res.status_code)
