import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    first_name = wtforms.StringField("Name", [wtforms.validators.DataRequired()], [wtforms.validators.Length(max=25)])
    last_country = wtforms.StringField("Lastname", [wtforms.validators.DataRequired()])
    age = wtforms.IntegerField("Age", [wtforms.validators.DataRequired()])
    experience = wtforms.StringField("Experience", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("submit")
    