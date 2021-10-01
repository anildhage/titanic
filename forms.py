from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
# 	Pclass - 1,2,3
# 	Sex - male/female
# 	Age - 00.0
# 	SibSp - 0 - 5 (can be any num, usually its less than 5)
# 	Parch - 0 - 6 (can be any num, usually its less than 6)
# 	Fare - its a float value - Any number - 00.00

class ticket_details(FlaskForm):
	sex = StringField('Sex', validators = [DataRequired(), Length(min=4,max=6)])
	pclass = StringField('Pclass', validators=[DataRequired(), Length(min=1,max=1)])
	age = StringField('Age', validators=[DataRequired(), Length(min=1,max=2)])
	sibsp = StringField('SibSp', validators=[DataRequired(), Length(min=1,max=1)])
	parch = StringField('Parch', validators=[DataRequired(), Length(min=1,max=1)])
	fare = StringField('Fare', validators=[DataRequired(), Length(min=1,max=10)])
	submit = SubmitField("Predict")
