#!/usr/bin/env python3
from flask import render_template, request, jsonify,redirect, url_for, make_response
import sqlalchemy as sa
from app.models import User, Tasks, Check, Session
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
from app import app
import json


@app.route('/')
@app.route('/index.html/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/signup.html/', methods=['GET', 'POST'])
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('createtasks'))
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
                login_user(user, remember=True)
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
                'success':{
                    'status':False,
                    'reason': str(e)
                } 
            })
    return render_template('signup.html')

@app.route('/login.html/<flag>', methods=['GET', 'POST'])
@app.route('/login.html/', defaults={'flag':''}, methods=['GET', 'POST'])
@app.route('/login/<flag>', methods=['GET', 'POST'])
@app.route('/login/',defaults={'flag':''}, methods=['GET', 'POST'])
def login(flag):
    if current_user.is_authenticated:
        return redirect(url_for('createtasks'))
    if request.method == 'GET':
        return render_template('login.html', flag=flag)
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
            return redirect("/login/wrongdata")


@app.route('/createtasks/',methods=['GET','POST'])
@app.route('/createtasks.html/',methods=['GET','POST'])
@login_required
def createtasks():
    if request.method == "GET":
        return render_template('createtasks.html')
    if request.method == "POST":
        try:
            body = request.get_json()
            session = Session()
            id = current_user.id
            for task in body['tasks']:
                if (session.query(Tasks).where(Tasks.id == body['tasks'][task][1]).all() != []):
                    continue
                t = Tasks(user_id=id, id=body['tasks'][task][1], name=task,description=body['tasks'][task][0],
                    date_added=datetime.now(),
                    evaluation=0,task_progress=0)
                session.add(t)
                session.commit()
            session.close()
            return jsonify({
                'status': 'success'
            })
        except Exception as e:
            return jsonify({
                'status': 'failed',
                'reason': str(e)
            })

@app.route('/gettasks/',methods=['GET'])
@login_required
def get_tasks():
    task_arr = []
    session = Session()
    tasks = session.query(Tasks).filter(Tasks.user_id == current_user.id).all()
    for task in tasks:
        task_arr.append({
            'name':task.name,
            'desc':task.description,
            'task_id':task.id
        })
    return make_response(jsonify(task_arr))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))

@app.route('/deletetask/', methods=['POST'])
@login_required
def delete_task():
    body = request.get_json()
    session = Session()
    task =  session.query(Tasks).where(Tasks.id == body['task_id']).first()
    try:
        session.delete(task)
        session.commit()
        session.close()
        return jsonify({
            'status':'success'
        })
    except Exception as e:
        return jsonify({
            'status':'failed',
            'reason': e
        })