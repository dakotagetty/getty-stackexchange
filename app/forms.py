from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

# Object to hold the form submission containing the value of the number of requested users
class UsersForm(FlaskForm):
    num_users = IntegerField('Number of Users (Range of 1 to 100)', validators=[DataRequired()])
    submit = SubmitField('Submit')