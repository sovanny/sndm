from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    steamid = StringField('steamid', validators=[DataRequired()])
    
