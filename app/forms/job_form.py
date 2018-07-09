from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

EMPLOYMENT_TYPE = [
    ("fulltime", "Fulltime"),
    ("contract", "Contract"),
    ("freelance", "Freelance"),
]

ONSITE_TYPE = [
    ("onsite", "Full On-Site"),
    ("partially", "Partially"),
    ("remote", "Remote Jobs"),
]


class JobSubmissionForm(FlaskForm):
    title = StringField("job title", validators=[DataRequired()])
    company = StringField("company", validators=[DataRequired()])
    location = StringField("location", validators=[DataRequired()])
    description = TextAreaField("description")
    skills = TextAreaField("required skills")
    website = StringField("website")
    contact = TextAreaField("contact")
    employment = SelectField("employment", choices=EMPLOYMENT_TYPE)
    on_site = SelectField("on site", choices=ONSITE_TYPE)
    submit = SubmitField("submit")

    def validate_description(self, description):
        if len(description.data.strip()) <= 30:
            raise ValidationError("please add more description")

    def validate_skills(self, skills):
        if len(skills.data.strip()) <= 30:
            raise ValidationError("please provide detailed requirement")
