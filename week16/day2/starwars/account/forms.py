import flask_wtf
import wtforms


class Login(flask_wtf.FlaskForm):
    username = wtforms.StringField(label="username", validators=[wtforms.validators.DataRequired()])
    password = wtforms.StringField(label="password", validators=[wtforms.validators.DataRequired()])
    remember_me = wtforms.BooleanField(label="remember me")

    submit = wtforms.SubmitField("Submit")


class Register(flask_wtf.FlaskForm):
    username = wtforms.StringField(label="username", validators=[wtforms.validators.DataRequired()])

    password = wtforms.StringField(label="password", validators=[
        wtforms.validators.DataRequired(),
        wtforms.validators.Length(min=6, max=10)])

    submit = wtforms.SubmitField("Submit")


class Profile(flask_wtf.FlaskForm):
    username = wtforms.StringField(label="username", validators=[wtforms.validators.DataRequired()])
    specie = wtforms.StringField(label="specie", validators=[wtforms.validators.DataRequired()])
    image = wtforms.FileField(label='image')

    submit = wtforms.SubmitField("Submit")
