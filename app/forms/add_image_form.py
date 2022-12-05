from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, URLField
from wtforms.validators import DataRequired, URL


class AddImageForm(FlaskForm):
    url = URLField('Image URL', validators=[DataRequired(), URL()])
    preview_image = BooleanField('Make Preivew Image:')
