from app import app
from flask import render_template,request,redirect,url_for,abort
from models import db,User,Document,Votes,Comment,CommentVotes
from forms import signinForm ,documentForm, commentForm
from sqlalchemy import func, or_, and_, desc
import os


@app.route('/query')
def query():
    #querying document
    doc = Document.query.get(1)
    #number of votes on a document
    votes = db.session.query(func.count(Votes.docid)).filter(Votes.docid == 1).first()
    #number of votes on a comment
    com_votes = db.session.query(func.count(CommentVotes.cid)).filter(CommentVotes.cid == 1).first()
    #get all comments for a document
    doc_comments = db.session.query(func.count(CommentVotes.cid),Comment.title,Comment.description,Comment.date,User.first_name,User.title).join(User).join(Comment).join(CommentVotes).filter(Comment.docid == 1).all()
    print doc_comments
    return '<h1>Querying Data</h1>'

@app.route('/insert')
def insert():
    title = "Emerging Technologies"
    description = "Hello World"
    submitter = 1
    location = "NYU"
    category = "Housing"
    doc = Document(title=title, description=description, submitter=submitter, location=location, category=category)
    db.session.add(doc)
    db.session.commit()
    return '<h1>Inserting Data</h1>'

@app.route('/user')
def user():
    # first_name = "Alan"
    # last_name = "Chen"
    # email = "Alan@nyu.edu"
    # password = "hello"
    # user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    #
    # docid = 1
    # userid = 2
    # votes = Votes(docid = docid, userid = userid)
    #
    # # title = "I love NYU"
    # # description = "Teachers make to little money"
    # # userid = 1
    # # docid = 1
    # #comment = Comment(title=title, description=description, userid=userid, docid=docid)
    #
    # cid = 1
    # userid = 2
    # comment_votes = CommentVotes(cid=cid, userid=userid)
    #
    # db.session.add(user)
    # db.session.commit()
    # db.session.add(comment_votes)
    # db.session.commit()

    return '<h1>Inserting User</h1>'



@app.route('/')
def index():
    print "hello world!!!"
    sForm = signinForm(request.form)
    dForm = documentForm(request.form)
    cForm = commentForm(request.form)
    return render_template('page.html',sForm=sForm,dForm=dForm,cForm=cForm)



@app.route('/signup')
def signup():
    db.drop_all()
    db.create_all()
    # file = request.files['picture']
    # did = db.session.query(func.max(Document.id)).scalar()
    # filename = str(did) + '_' + doc.title + ".jpeg"
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # doc.filename = filename
    return '<h1>Signed Up</h1>'
