from flask_wtf import FlaskForm
from wtforms import FileField, SelectMultipleField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Generate_questionnaire(FlaskForm):
    bdd_file = FileField(label="Base de questions", validators=[DataRequired()])
    subject = SelectMultipleField(label="Discipline(s)", coerce=int)
    notion = SelectMultipleField(label="Rudiment(s)", coerce=int)
    level = SelectMultipleField(label="Niveau(x) scolaire(s)", coerce=int)
    time = IntegerField(label="Temps de l'épreuve")
    difficulty = SelectField(label="Difficulté de l'épreuve", coerce=int)
    submit = SubmitField(label="Générer le questionnaire")