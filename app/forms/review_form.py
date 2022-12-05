from flask_wtf import FlaskForm
from wtforms.fields import  IntegerField, StringField
from wtforms.validators import Length, DataRequired, NumberRange


class CreateEditReviewForm(FlaskForm):
    text = StringField('Text', validators=[Length(min=1, max=255), DataRequired()])
    rating = IntegerField('Rating', validators=[NumberRange(min=1, max=5), DataRequired()])
