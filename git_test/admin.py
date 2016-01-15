from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from user import User,Comment
from db import db

admin = Admin()
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Comment, db.session))
