from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Length, InputRequired, Email


class signinForm(Form):
    email = StringField('Email:', validators=[InputRequired(message="This field is required"), Email(message="Not a valid email")])
    password = PasswordField('Password: ', validators=(InputRequired(message="This field is required"), Length(min=6, message="Password must be at least 6 characters")))
    submit = SubmitField('Login')


class documentForm(Form):
    title = StringField('Title:', validators=[InputRequired(message="This field is required")])
    description = TextAreaField('Description:', validators=[InputRequired(message="This field is required")])
    location = StringField('Location:')
    issue_idea = SelectField('Type:', choices=[('Issue','Issue'), ('Idea','Idea')])
    category = SelectField('Type:', choices=[('Housing','Housing'), ('Technology','Technology')])
    submit = SubmitField('Submit')


class commentForm(Form):
    title = StringField('Title:')
    description = TextAreaField('Description:', validators=[InputRequired(message="This field is required")])
    submit = SubmitField('Comment')