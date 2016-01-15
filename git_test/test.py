from datetime import datetime

from flask import Flask, jsonify, render_template, request, make_response, session
from sqlalchemy.sql import (
    func,
)
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from db import db,migrate
from user import User,Comment,Board
from admin import admin

app = Flask(__name__)
app.config.from_pyfile("config.py")
admin.init_app(app)
db.init_app(app)
migrate.init_app(app,db)



@app.route("/")
def index():

    return render_template('index.html')

#################################### Login
@app.route("/loginpage")
def login_page():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['id']
    password = request.form['password']

    found = User.query.filter(
        User.id == username,
        User.pw == password,
    ).first()
    if found:
        session['logged_in'] = True
        resp = make_response(render_template('main.html')  )
        resp.set_cookie('username', username)
        print(session['logged_in'])
        return resp
    else :
        return "Login Failed"
##################################### Sign

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')

@app.route("/signpage")
def sign_page():
    return render_template('index.html')

@app.route("/sign" ,  methods=['GET', 'POST'])
def sign():
    new = User()
    new.name = request.form['nickname']
    new.id = request.form['id']
    new.pw = request.form['password']

    if not len(new.name) or not len(new.id) or not len(new.pw) :
        return "fuck"
    if is_already_registered(new.id, new.pw, new.name ) == 2:
        return "id"
    if is_already_registered(new.id, new.pw, new.name)== 3:
        return "pw"
    if is_already_registered(new.id, new.pw, new.name) == 4:
        return "name"
    db.session.add(new)
    db.session.commit()

    return render_template("index.html")

def is_already_registered(id,pw, name):
    found = User.query.filter(
        User.id == id,
    ).first()
    found2 = User.query.filter(
        User.pw == pw,
    ).first()
    found3 = User.query.filter(
        User.name == name,
    ).first()

    if found:
        return 2
    if found2:
        return 3
    if found3:
        return 4
    return False

@app.route("/success")
def success():
    username = request.cookies.get('username')
    return "<h1>" + str(username)

@app.route("/form.html")
def write():
    return render_template("form.html")

@app.route("/w_success",methods=['GET','POST'])
def w_success():
    board = Board()
    title = request.form['title']
    text = request.form['textarea']
    board.title = title
    board.text = text
    board_id = board.idx
    board.good = "0"
    board.bad = "0"
    board.count = "0"
    board.num = db.session.query(
            func.max(Board.num),
    ).one()[0]
    if board.num == None:
        board.num = 0
    else:
        board.num += 1
    db.session.add(board)
    db.session.commit()
    board1 = board.query.filter(
    ).all()
    return render_template("Board.html",board = board1,)

@app.route("/<id>")
def view(id):
    board = Board()
    board = board.query.get(id)
    return render_template("view.html",post = board)
       

"""
@app.route("/search/<name>/<id>/<pw>")
def search(name, id, pw, is_web=True):
    found = User.query.filter(
        User.name == name,
        User.id == id,
        User.pw == pw,
    ).first()
    if found:
        if is_web:
            return 'success! %s' % (found.id, )
    else:
        return found

    if is_web:
        return 'failed'
    else:
        return None
"""
"""
@app.route("/delete/<name>/<id>/<pw>")
def delete(name, id, pw):
    found = search(name, id, pw, is_web=False)
    db.session.delete(found)
    db.session.commit()

    return 'deleted!'
"""
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
