from flask_wtf import FlaskForm
from wtforms.fields import StringField, FloatField, TextAreaField
from wtforms.validators import Length, DataRequired, NumberRange


class CreateEditProductForm(FlaskForm):
    name = StringField('Name', validators=[Length(min=1, max=75), DataRequired()])
    price = FloatField('Price', validators=[NumberRange(min=0), DataRequired()])
    description = StringField('Description', validators=[Length(min=1, max=2000), DataRequired()])
    images_urls = TextAreaField('Images URLs (sperated by comma, put prview image first)')
