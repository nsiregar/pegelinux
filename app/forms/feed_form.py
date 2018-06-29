from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import ValidationError
from wtforms.validators import DataRequired

from app.models.feed import Feed

class SubmissionForm(FlaskForm):
    owner = StringField('owner', validators=[DataRequired()])
    rss = StringField('your rss feed address', validators=[DataRequired()])
    html = StringField('your tld', validators=[DataRequired()])
    submit = SubmitField('register feed')

    def validate_owner(self, owner):
        owner = Feed.query.filter_by(owner=owner.data).first()
        if owner is not None:
            raise ValidationError('this owner name already registered')

    def validate_rss(self, rss):
        rss = Feed.query.filter_by(rss=rss.data).first()
        if rss is not None:
            raise ValidationError('this feed already registered')
    
    def validate_html(self, html):
        html = Feed.query.filter_by(html=html.data).first()
        if html is not None:
            raise ValidationError('this tld already registered')


class FeedModerationForm(FlaskForm):
    approved = BooleanField('approved')
    submit = SubmitField('register feed')