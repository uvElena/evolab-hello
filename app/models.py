from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    user_name = db.Column(db.String(255), primary_key=True)
