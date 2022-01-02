import flask_wtf
import wtforms


class Login(flask_wtf.FlaskForm):
    def __init__(self, formdata=_Auto, _Auto=None, **kwargs):
        super().__init__(formdata, kwargs)
        self.status = None

    name = wtforms.StringField(label="name", validators=[wtforms.validators.data_required()])
    city_name = wtforms.StringField(label="city name", validators=[wtforms.validators.data_required()])

    submit = wtforms.SubmitField("Submit")


class Register(flask_wtf.FlaskForm):
    name = wtforms.StringField(label="name", validators=[wtforms.validators.DataRequired()])
    city_name = wtforms.StringField(label="city name", validators=[wtforms.validators.DataRequired()])

    submit = wtforms.SubmitField("Submit")
