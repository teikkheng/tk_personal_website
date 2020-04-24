from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TextInputForm(FlaskForm):
    text = StringField("Input Text", validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Submit')