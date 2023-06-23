from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class JournalForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    book = StringField('Book', id='book_input', render_kw={"autocomplete": "off", "list": "book_list"})
    start_page = IntegerField('Starting Page', validators=[DataRequired(), NumberRange(min=0)])
    end_page = IntegerField('Ending Page', validators=[DataRequired(), NumberRange(min=0)])
    content = TextAreaField('Journal Entry', validators=[DataRequired()])
    submit = SubmitField('Submit')


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Submit')