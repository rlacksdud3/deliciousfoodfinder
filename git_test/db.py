from datetime import datetime
from flask import Flask, jsonify,render_template,request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'asldjalksjdklasd'
admin = Admin(app)
db = SQLAlchemy(app)


class User(db.Model):
    """
    from test import db
    db.create_all()
    """
    __tablename__ = "user"

    idx = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, default=20)
    name = db.Column(db.String(20))
    id = db.Column(db.String(20), unique=True)
    pw = db.Column(db.String(20))
    created = db.Column(db.DateTime, default=datetime.now)

    # no __init__()

class Comment(db.Model):
    __tablename__ = "comment"

    idx = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    who = db.Column(db.Integer, db.ForeignKey('user.idx'))

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Comment, db.session))


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/create/<name>/<id>/<pw>")
def create(name, id, pw):
    new = User()
    new.name = name
    new.id = id
    new.pw = pw
    db.session.add(new)
    db.session.commit()
    return jsonify({
        "id": id,
        "pw": pw,
        "data": [
            "heheheheheh",
            "wowowowowowo",
            "hell yeah",
        ]
    })

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


@app.route("/delete/<name>/<id>/<pw>")
def delete(name, id, pw):
    found = search(name, id, pw, is_web=False)
    db.session.delete(found)
    db.session.commit()
    return 'deleted!'

@app.route("/loginpage")
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['id']
    password = request.form['password']
    found = User.query.filter(
        User.id == username,
        User.pw == password,
    ).first()
    if found:
        return "<h1>" + str(request.form['id'] ) + " <h1>" + str(request.form['password'])
    else :
        return "Login Failed"

@app.route("/signpage")
def sign_page():
    return render_template('sign.html')

@app.route("/sign" ,  methods=['GET', 'POST'])
def sign():
    new = User()
    new.name = request.form['nickname']
    new.id = request.form['id']
    new.pw = request.form['password']
    db.session.add(new)
    db.session.commit()
    return render_template("success.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
