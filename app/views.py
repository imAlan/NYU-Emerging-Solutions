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
    doc_comments = db.session.query(Comment).join(User).join(Comment).outerjoin(CommentVotes).filter(Comment.docid == 1).order_by(desc(Comment.date)).all()
    #get top 20 documents
    top_docs = db.session.query(func.count(Votes.docid).label('upvotes'), Document).outerjoin(Document).group_by(Votes.docid).order_by('upvotes DESC').all()
    for doc in top_docs:
        print doc[0],doc[1].id
    return '<h1>Querying Data</h1>'

@app.route('/insert')
def insert():
    # title = "This is a random idea"
    # description = "Random idea"
    # userid=1
    # docid=1
    # comment1 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "I am so freakin tired"
    # description = "Really tired"
    # userid=2
    # docid=1
    # comment2 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "This is a random idea"
    # description = "Random idea"
    # userid=1
    # docid=1
    # comment3 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "Let's fix all the elevators"
    # description = "Please"
    # userid=1
    # docid=2
    # comment4 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "Let's give out free bitcoins"
    # description = "Free money!"
    # userid=4
    # docid=2
    # comment5 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "Let's Party!"
    # description = "It's been a while"
    # userid=3
    # docid=2
    # comment6 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "Random idea number 6"
    # description = "Random idea num6"
    # userid=4
    # docid=3
    # comment7 = Comment(title=title,description=description,userid=userid,docid=docid)
    # title = "This is a random idea num7"
    # description = "Random idea num7"
    # userid=1
    # docid=4
    # comment8 = Comment(title=title,description=description,userid=userid,docid=docid)
    # db.session.add(comment1)
    # db.session.add(comment2)
    # db.session.add(comment3)
    # db.session.add(comment4)
    # db.session.add(comment5)
    # db.session.add(comment6)
    # db.session.add(comment7)
    # db.session.add(comment8)
    cid = 1
    userid = 1
    comment_votes1 = CommentVotes(cid=cid, userid=userid)
    cid = 1
    userid = 2
    comment_votes2= CommentVotes(cid=cid, userid=userid)
    cid = 1
    userid = 3
    comment_votes3 = CommentVotes(cid=cid, userid=userid)
    cid = 1
    userid = 4
    comment_votes4 = CommentVotes(cid=cid, userid=userid)
    cid = 2
    userid = 3
    comment_votes5 = CommentVotes(cid=cid, userid=userid)
    cid = 3
    userid = 4
    comment_votes6 = CommentVotes(cid=cid, userid=userid)
    cid = 4
    userid = 2
    comment_votes7 = CommentVotes(cid=cid, userid=userid)
    cid = 5
    userid = 1
    comment_votes8 = CommentVotes(cid=cid, userid=userid)
    cid = 6
    userid = 3
    comment_votes9 = CommentVotes(cid=cid, userid=userid)
    cid = 7
    userid = 4
    comment_votes10 = CommentVotes(cid=cid, userid=userid)
    db.session.add(comment_votes1)
    db.session.add(comment_votes2)
    db.session.add(comment_votes3)
    db.session.add(comment_votes4)
    db.session.add(comment_votes5)
    db.session.add(comment_votes6)
    db.session.add(comment_votes7)
    db.session.add(comment_votes8)
    db.session.add(comment_votes9)
    db.session.add(comment_votes10)


    db.session.commit()
    return '<h1>Inserting Data</h1>'

@app.route('/user')
def user():
    # first_name = "Ayanna"
    # last_name = "Seals"
    # email = "as@nyu.edu"
    # password = "danger"
    # user1 = User(first_name=first_name, last_name=last_name, email=email, password=password)
    # first_name = "Ken"
    # last_name = "Chan"
    # email = "kc@nyu.edu"
    # password = "danger"
    # user2 = User(first_name=first_name, last_name=last_name, email=email, password=password)
    # first_name = "Alan"
    # last_name = "Chen"
    # email = "ac@nyu.edu"
    # password = "danger"
    # user3 = User(first_name=first_name, last_name=last_name, email=email, password=password)
    # first_name = "Alvi"
    # last_name = "Kabir"
    # email = "ak@nyu.edu"
    # password = "danger"
    # user4 = User(first_name=first_name, last_name=last_name, email=email, password=password)
    #
    docid = 1
    userid =1
    votes1 = Votes(docid = docid, userid = userid)
    docid = 1
    userid =2
    votes2 = Votes(docid = docid, userid = userid)
    docid = 1
    userid =3
    votes3 = Votes(docid = docid, userid = userid)
    docid = 2
    userid =1
    votes4 = Votes(docid = docid, userid = userid)
    docid = 2
    userid =2
    votes5 = Votes(docid = docid, userid = userid)
    docid = 3
    userid =1
    votes6 = Votes(docid = docid, userid = userid)


    #
    db.session.add(votes1)
    db.session.add(votes2)
    db.session.add(votes3)
    db.session.add(votes4)
    db.session.add(votes5)
    db.session.add(votes6)
    db.session.commit()
    # db.session.add(comment_votes)
    # db.session.commit()

    return '<h1>Inserting User</h1>'



@app.route('/', methods=['GET', 'POST'])
def index():
    sForm = signinForm(request.form)
    if sForm.validate_on_submit():
        email = sForm.email.data
        password = sForm.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(url_for('submit'))
    return render_template('login.html', sForm=sForm)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('')

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
        doc_vote = Votes(docid=did,userid=current_user.id)
        db.session.add(doc_vote)
        db.session.commit()
    return render_template('submission.html',dForm=dForm)