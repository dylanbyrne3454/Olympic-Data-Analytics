from dash import Dash, dash_table, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from flask_app.models import SurveyResponse

from .layout import create_layout
from .callbacks import register_callbacks
from .data import load_database
"""
def load_database(app):
    with app.app_context():
        entrys = SurveyResponse.query.all()
        data = [
            {
                "Id": s.id, 
                "Age": s.age,
                "Country": s.country,
                "Gender": s.gender, 
                "Watch_Olympics": s.watch_olympics,
                "Summer_vs_Winter": s.summer_vs_winter,
                "Athlete": s.athlete, 
                "Sport": s.sport,
                "How_long": s.how_long,
                "Become_olympian": s.become_olympian
            } 
            
            for s in entrys]
        df = pd.DataFrame(data)
        return df

"""
def survey_dashboard_app(server):
    app = Dash(
        __name__,
        server=server,
        url_base_pathname='/survey_dashboard/',
        external_stylesheets=[dbc.themes.CYBORG]
    )
    
  #  df =  load_database(server)
    app.layout = create_layout()
    register_callbacks(app)
    return app
