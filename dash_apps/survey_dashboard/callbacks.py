
from dash.dependencies import Input, Output
from .data import *
import plotly.express as px

def register_callbacks(app):
    
    @app.callback(
            [
                Output('gender', 'figure'),
                Output('age', 'figure'),
                Output('country', 'figure'),
                Output('become_olympian', 'figure'),
                Output('athlete', 'figure'),
                Output('sport', 'figure'),
                Output('winter_vs_summer', 'figure'),
                Output('watch_olympics', 'figure'),
                Output('table', 'columns'),
                Output('table', 'data'),
            ],
        Input("interval-component", "n_intervals"),
    )
    def update_charts(_):
        print("works")
        with app.server.app_context():
            df = load_database()
     
        return [
            px.pie(gender_pi(df), values='count', names='Gender', title='Gender', template='plotly_dark'),
            px.bar(age(df), x='Age', y="count", template='plotly_dark', color="Age"),
            px.bar(country(df), x='Country', y="count", template='plotly_dark', color="Country"),
            px.pie(become_olympian(df), values='count', names='Become_olympian', title='Become_olympian', template='plotly_dark'),
            px.bar(athlete(df), x='count', y="Athlete", template='plotly_dark', color="Athlete"), 
            px.bar(sport(df), x='count', y="Sport", template='plotly_dark', color="Sport"),
            px.pie(winter_vs_summer(df), values='count', names='Summer_vs_Winter', title='Summer_vs_Winter', template='plotly_dark'),
            px.bar(watch_olympics(df), x='count', y="Watch_Olympics", template='plotly_dark', color="Watch_Olympics"),
            [{"name": i, "id": i} for i in df.columns],
            df.to_dict('records')
        ]