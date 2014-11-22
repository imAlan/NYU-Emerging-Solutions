__author__ = 'Coffee_Ninja'
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    role = db.Column(db.Enum('User','Admin'), default='User')
    title = db.Column(db.String(255),nullable=True)
    documents = db.relationship('Document', backref='user',lazy='dynamic')
    votes = db.relationship('Votes', backref='user',lazy='dynamic')
    comment_votes = db.relationship('CommentVotes', backref='user',lazy='dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)
    submitter = db.Column(db.Integer, db.ForeignKey('user.id'))
    location = db.Column(db.String(255),nullable=True)
    issue_idea = db.Column(db.Enum('Issue','Idea'),nullable=False)
    category = db.Column(db.String(255),nullable=True)
    date = db.Column(db.DateTime,nullable=False, default=datetime.datetime.now())
    votes = db.relationship('Votes', backref='document',lazy='dynamic')

class Votes(db.Model):
    __tablename__ = 'votes'
    docid = db.Column(db.Integer,db.ForeignKey('document.id'),primary_key=True)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'))
    docid = db.Column(db.Integer,db.ForeignKey('document.id'))
    date = db.Column(db.DateTime,nullable=False, default=datetime.datetime.now())
    votes = db.relationship('CommentVotes', backref='comment',lazy='dynamic')

class CommentVotes(db.Model):
    __tablename__ = 'comment_votes'
    cid = db.Column(db.Integer,db.ForeignKey('comment.id'),primary_key=True)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user

