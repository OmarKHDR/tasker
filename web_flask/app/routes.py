#!/usr/bin/env python3
from flask import render_template, request, jsonify
import json
from app import app

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup.html', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        body = request.get_json()
        return jsonify({
            'success':{
                'status': True,
                'reason': "dont worry brother"
            }
        })
    return render_template('signup.html')

@app.route('/login.html', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return "hello {}"