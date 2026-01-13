from flask import Blueprint, render_template, redirect , request, jsonify
from .data import countries, sports
from .models import db, SurveyResponse
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')


@main.route('/survey')
def survey():
    return render_template('survey.html', countries=countries, sports=sports)

@main.route('/survey_submitted')
def survey_submitted():
    return render_template('survey_submitted.html')

@main.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        become_olympian = request.form.get("become_Olympian", "false")  # Default to "false"
        become_olympian = become_olympian.lower() == "true" 
        new_entry = SurveyResponse(
            age= request.form['age'],
            country= request.form['country'],
            gender= request.form['gender'],
            watch_olympics= request.form['watch_olympics'],
            summer_vs_winter= request.form['summer_vs_winter'],
            athlete= request.form['athlete'],
            sport= request.form['sport'],
            how_long = request.form['how_long'],
            become_olympian= become_olympian
        )

        db.session.add(new_entry)
        db.session.commit()
        return redirect('/survey_submitted')
 

    else:
        render_template('survey.html')

@main.route("/print_db", methods=["GET"])
def print_db():
    entrys = SurveyResponse.query.all()
    entrys_list = [{"id": entry.id, "age": entry.age, "country": entry.country} for entry in entrys]
    return jsonify(entrys_list)


