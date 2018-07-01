from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class CommentForm(FlaskForm):
    messages = TextAreaField(
        "comment", validators=[DataRequired(), Length(min=10, max=140)]
    )
    submit = SubmitField("reply")
