from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title =StringField('Review title', [Required()])
    review = TextAreaField('Movie review', [Required()])
    submit = SubmitField('Submit')