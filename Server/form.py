from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class PredictForm(FlaskForm):
    total_sqft = StringField(label="Area", validators=[Length(min=200,max=15000), DataRequired() ])
    location = SelectField(label="Location", validators=[DataRequired()])
    bhks = RadioField(label="BHKs", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),], validators=[DataRequired(),])
    bathrooms = RadioField(label="Bathrooms", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),], validators=[DataRequired()])
    submit = SubmitField(label="Submit")
