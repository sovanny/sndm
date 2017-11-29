from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    steamid = StringField('steamid', validators=[DataRequired()])
    

class ThreeGamesForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    game1 = StringField('game1', validators=[DataRequired()])
    game2 = StringField('game2', validators=[DataRequired()])
    game3 = StringField('game3', validators=[DataRequired()])
    
