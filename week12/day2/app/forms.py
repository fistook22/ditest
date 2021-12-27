import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    city_name = wtforms.StringField("Name", [wtforms.validators.DataRequired()], [wtforms.validators.Length(max=25)])
    city_country = wtforms.StringField("Country", [wtforms.validators.DataRequired()])
    num_of_inhabit = wtforms.IntegerField("number_of_inhabitants", [wtforms.validators.DataRequired()])
    city_area = wtforms.IntegerField("area in square km")
