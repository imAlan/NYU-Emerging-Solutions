from app import app
from flask import render_template,request,redirect,url_for,abort, jsonify
from models import db,User,Document,Votes,Comment,CommentVotes
from forms import signinForm ,documentForm, commentForm
from sqlalchemy import func, or_, and_, desc
from flask.ext.login import login_user, login_required, logout_user, current_user
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
    # email = "alanchen@nyu.edu"
    # password = "danger"
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



@app.route('/', methods=['GET', 'POST'])
def index():
    sForm = signinForm(request.form)

    # cForm = commentForm(request.form)
    if sForm.validate_on_submit():
        email = sForm.email.data
        password = sForm.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            print "Alvi wants to go in here"
            login_user(user)
            return redirect(url_for('submit'))
    return render_template('login.html', sForm=sForm)



@app.route('/signup')
def signup():
    # db.drop_all()
    # db.create_all()
    # file = request.files['picture']
    # did = db.session.query(func.max(Document.id)).scalar()
    # filename = str(did) + '_' + doc.title + ".jpeg"
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # doc.filename = filename
    return '<h1>Signed Up</h1>'

@app.route('/submit',methods=['GET', 'POST'])
def submit():
    dForm = documentForm(request.form)
    print current_user.id
    if dForm.validate_on_submit():
        title=dForm.title.data
        description=dForm.description.data
        location=dForm.location.data
        issue_idea=dForm.issue_idea.data
        category=dForm.category.data
        submitter=current_user.id
        document = Document(title=title,description=description,location=location,issue_idea=issue_idea,category=category,submitter=submitter)
        db.session.add(document)
        db.session.commit()
        did = db.session.query(func.max(Document.id)).scalar()
        document = Document.query.get(did)
        file = request.files['file']
        filename = str(did) + ".png"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        document.filename = filename
        db.session.commit()
    return render_template('submission.html',dForm=dForm)