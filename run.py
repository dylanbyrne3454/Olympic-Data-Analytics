from flask_app import create_app
from dash_apps.main_dashboard import main_dashboard_app
from dash_apps.main_dashboard.data import *
from dash_apps.survey_dashboard import survey_dashboard_app

app=create_app()
main_dashboard_app(app)
survey_dashboard_app(app)

if __name__ == '__main__':
    app.run(debug=True)