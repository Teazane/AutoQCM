from App import app
from flask import render_template, redirect, session, url_for, request
from jinja2 import Environment, PackageLoader
from .forms.questionnaire_form import Generate_questionnaire, DB_choice
import json

env_jinja = Environment(loader=PackageLoader('app_src', 'templates'))

@app.route('/')
def home():
    return render_template(env_jinja.get_template('home.html'))

@app.route('/data_base_choice', methods=['GET', 'POST'])
def database_choice():
    form = DB_choice()
    if form.validate_on_submit():
        print("This is a valid form!")
        data = json.dumps({"TODO":"TODO"}) # Charger les data de l'excel
        session['data'] = data
        return redirect(url_for('.questionnaire', data=data))
    return render_template(env_jinja.get_template('data_base_choice.html'), form=form)

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    data = request.args['data']  # counterpart for url_for()
    data = session['data']       # counterpart for session
    form = Generate_questionnaire()
    form.subject.choices = [(0, "Choix 0"), (1, "Choix 1")]
    form.notion.choices = [(0, "Choix 0"), (1, "Choix 1")]
    form.level.choices = [(0, "Choix 0"), (1, "Choix 1")]
    form.difficulty.choices = [(0, "Choix 0"), (1, "Choix 1")]
    if form.validate_on_submit():
        # TODO
        return redirect("/")
    return render_template(env_jinja.get_template('questionnaire.html'), form=form)

@app.route('/favico.ico')
def favicon():
    return ''