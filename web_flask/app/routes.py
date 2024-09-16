#!/usr/bin/env python3
from flask import render_template, request, jsonify,redirect, url_for
import sqlalchemy as sa
from app.models import User, Tasks, Check, Session
from flask_login import current_user, login_user
from app import app
import json


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
        try:
            session = Session()
            if (session.query(User).filter(User.email == body['email']).first() != None):
                session.close()
                return jsonify({
                    'success': {
                        'status': False,
                        'reason': "this email already exists"
                    },
                })
            else:
                user = User(name=body['name'],email=body['email'],password=body['password'])
                session.add(user)
                session.commit()
                session.close()
                return jsonify({
                    'success': {
                        'status': True,
                        'reason': "dont worry brother"
                    },
                })
        except Exception as e:
            try:
                session.close()
            except:
                pass
            return jsonify({
                'success': False,
                'reason': str(e)
            })
    return render_template('signup.html')

@app.route('/login.html', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('createtasks'))
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        body = request.get_json()
        session = Session()
        user = session.scalar(sa.select(User).where(User.email == body['email']))
        if (user != None) and (user.password == body['password']):
            session.close()
            login_user(user, remember=True)
            return redirect(url_for("createtasks"))
        else:
            session.close()
            return redirect(url_for("login"))

@app.route('/createtasks',methods=['GET','POST'])
@app.route('/createtasks.html',methods=['GET','POST'])
def createtasks():
    if request.method == "GET":
        return render_template("createtasks.html")