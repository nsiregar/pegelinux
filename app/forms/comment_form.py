from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError


class CommentForm(FlaskForm):
    messages = TextAreaField("comment", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("reply")

    def validate_messages(self, messages):
        if len(messages.data.strip()) < 10:
            raise ValidationError("minimum comment require 10 characters")
