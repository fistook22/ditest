import flask_wtf
import wtforms


class AddTask(flask_wtf.FlaskForm):
    name = wtforms.StringField(label="name", validators=[wtforms.validators.DataRequired()])
    details = wtforms.StringField(label="details", validators=[wtforms.validators.DataRequired()])

    submit = wtforms.SubmitField("Submit")


