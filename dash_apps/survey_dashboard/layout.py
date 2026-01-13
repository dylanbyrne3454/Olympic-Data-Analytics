from dash import Dash, dash_table, html, dcc, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from .data import *

GRAPH_STYLE = {
    "padding": "1rem",
    
}
HOME_BUTTON_DIV = {
    "padding": "2rem", 
}
A_STYLE = {
    "background-color": "#fe53bb",
    "color": "black",
    "padding": "14px 25px",
    "text-align": "center",
    "text-decoration": "none",
    "display": "inline-block",
    "border-radius": "5px"
}

H2_STYLE = {
    "padding": "0.5em",
    "padding-top": "1em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "30px",
    "color": "#fe53bb",
}
TITLE_STYLE = {
    "padding": "0.5em",
    "padding-top": "0em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "80px",
    "color": "#fe53bb",
    'textAlign':'center'
}
def create_layout():
    layout = html.Div([
        html.Div(id="hidden-div", style={"display": "none"}),
        dcc.Interval(id="interval-component", interval=5000, n_intervals=0), 
        html.Div([
            html.A(href="/", children="Home", style=A_STYLE),
        ], style=HOME_BUTTON_DIV),
        dbc.Row([
            dbc.Col(html.H1(children='Survey Results', style=TITLE_STYLE))
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row(dcc.Graph(id="gender", style=GRAPH_STYLE)),
            ], width=3),
        
            dbc.Col([
                dbc.Row(dcc.Graph(id="age", style=GRAPH_STYLE)),
            ], width=9)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row(dcc.Graph(id="country", style=GRAPH_STYLE)),
            ], width=9),
        
            dbc.Col([
                dbc.Row(dcc.Graph(id="become_olympian", style=GRAPH_STYLE)),
            ], width=3)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row(dcc.Graph(id="athlete", style=GRAPH_STYLE)),
            ], width=6),
        
            dbc.Col([
                dbc.Row(dcc.Graph(id="sport", style=GRAPH_STYLE)),
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row(dcc.Graph(id="winter_vs_summer", style=GRAPH_STYLE)),
            ], width=3),
        
            dbc.Col([
                dbc.Row(dcc.Graph(id="watch_olympics", style=GRAPH_STYLE)),
            ], width=9)
        ]),

        dash_table.DataTable(
            id='table',
            columns=[],
            data=[],
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="#fe53bb", color="black"),
            style_data=dict(backgroundColor="black"),
            style_table={"padding": "20px"},
    ), 
    

    
    ])
    return layout