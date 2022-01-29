from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length


class Login(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])
    password = StringField(label="password", validators=[DataRequired()])
    remember_me = BooleanField(label="remember me")

    submit = SubmitField("Submit")


class Register(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])

    password = StringField(label="password", validators=[
        DataRequired(),
        Length(min=6, max=10)])

    submit = SubmitField("Submit")


class Profile(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])
    specie = SelectField(label="specie", chices=[1, 'Human', 2, 'Droid', 3, 'Wookie', 4, 'Hutt'],
                         validators=[DataRequired()])
    image = FileField(label='image')

    submit = SubmitField("Submit")
