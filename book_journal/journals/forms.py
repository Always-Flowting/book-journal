from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class JournalForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    start_page = IntegerField('Starting Page', validators=[DataRequired(), NumberRange(min=0)])
    end_page = IntegerField('Ending Page', validators=[DataRequired(), NumberRange(min=0)])
    content = TextAreaField('Journal Entry', validators=[DataRequired()])