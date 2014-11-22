from app import app
app.config['SECRET_KEY'] = 'hello world'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost/vent"


