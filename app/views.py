from app import app
from flask import render_template,request,redirect,url_for,abort
from models import db,User,Document,Votes,Comment,CommentVotes

@app.route('/')
def index():
    print "hello world!!!"
    db.drop_all()
    db.create_all()
    return '<h1>Hello World!</h1>'


@app.route('/signup')
def signup():
    first_name = 'Alvi'
    last_name = 'Kabir'
    email = 'something@me.com'
    password = 'hello'
    user = User(first_name=first_name,last_name=last_name,email=email,password=password)
    db.session.add(user)
    db.session.commit()
    return '<h1>Signed Up</h1>'
