from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


class AddForm(FlaskForm):
    person = StringField('person', validators=[data_required()])
    phonenumber = StringField('phonenumber', validators=[data_required()])
    email = StringField('email', validators=[data_required()])
    address = StringField('address')
    submit = SubmitField('Add a New Number')

