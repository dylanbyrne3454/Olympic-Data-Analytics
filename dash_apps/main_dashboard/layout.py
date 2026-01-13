from dash import Dash, dash_table, html, dcc, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from .data import *

top_cards= [
    dbc.Col([
            html.H2(children='Amount of Competitors', style={'textAlign':'center'}),
            html.H2(id="Total_amount_competitors", style={'textAlign':'center'}),
        ]),
    dbc.Col([
            html.H2(children='Amount of Medals', style={'textAlign':'center'}),
            html.H2(id="Total_amount_of_medals", style={'textAlign':'center'}),
        ]),
    dbc.Col([
            html.H2(children='Amount of Gold', style={'textAlign':'center'}),
            html.H2(id="Total_amount_of_gold", style={'textAlign':'center'}),
        ]),
    dbc.Col([
            html.H2(children='Amount of Silver', style={'textAlign':'center'}),
            html.H2(id="Total_amount_of_silver", style={'textAlign':'center'}),
        ]),
    dbc.Col([
            html.H2(children='Amount of Bronze', style={'textAlign':'center'}),
            html.H2(id="Total_amount_of_bronze", style={'textAlign':'center'}),
        ]),
]

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "32rem",
    "padding": "2rem 1rem",
    "background-color": "#060606",
    "border-color": "#fe53bb",
    "border-radius": "10px",
}


SELECT_STYLE = {
    "width": "400px",
    "height": "20px",
    "background-color": "#060606",
    "color": "#fe53bb",
   # "padding": "0.7em",
    "font-family": '"Lucida Console", "Courier New", "monospace"',
    "font-size": "20px",
    "border-radius": "10px",
    "border-color": "#fe53bb",
}

HOME_BUTTON_DIV = {
    "padding": "1rem", 
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
H2_STYLE_RADIO = {
    "padding": "0.25em",
    "padding-top": "0.25em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "30px",
    "color": "#fe53bb",
}
CHART_TITLES_STYLE = {
    "padding": "0.5em",
    "padding-top": "1em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "30px",
    "color": "#fe53bb",
}
TITLE_STYLE = {
    "padding": "0.5em",
    "padding-top": "1em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "80px",
    "color": "#fe53bb",
}
FILTERS_TITLE = {
    "padding": "0.5em",
    "padding-bottom": "0em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "40px",
    "color": "#fe53bb",

}
MAP_STYLE = {
    "padding": "0.5em",
    "padding-top": "1em",
    "font-family": '"Lucida Console", "Courier New", monospace',
    "font-size": "30px",
    "color": "#fe53bb",
    "height": "1000px"
}

CHARTS_STYLE= {
    'height': '100%', 
    'padding': '1em', 
    'padding-top': '0em'
}
MAP_CHARTS_STYLE= {
    'height': '100%', 
    'padding': '1em', 
    'padding-top': '0em'
}
RADIO_DIV_STYLE = {
    "font-size": "2rem",
    "font-weight":"bold",
    "line-height": "1.1",
    "display": "grid",
  #  "grid-template-columns": "1em auto",
  #  "gap": "0.5em",
}
RADIO_STYLE={
    "font-size": "1.25rem",
 #   "display": "flex",
  #  "align-items": "center",
   # "grid-template-columns": "1em auto",
    "gap": "0.5em",
   # "background-color": "#08f7fe",
    "color": "#08f7fe",
    "padding-left": "0.7em",
    "font-family": '"Lucida Console", "Courier New", "monospace"',
    #"font-size": "20px",
}

sidebar = html.Div([
    html.Div([
            html.A(href="/", children="Home", style=A_STYLE),
        ], style=HOME_BUTTON_DIV),
    html.H1(children='Filters', style=FILTERS_TITLE),

    html.H2(children='Season', style=H2_STYLE_RADIO),
    dcc.RadioItems(['Summer', 'Winter','Both'], 'Summer', id="season", style=RADIO_STYLE),

    html.H2(children='Gender', style=H2_STYLE_RADIO),
 #   html.Div([
    dcc.RadioItems(['All', 'Male','Female'], 'All', id="gender", style=RADIO_STYLE),


    html.H2(children='Country', style=H2_STYLE_RADIO),
  #  dcc.RadioItems(['All', 'Custom'], 'All', id="all_countrys_or_custom", style=RADIO_STYLE),
    dcc.Dropdown(id='Teams', multi=True, style=SELECT_STYLE),

    html.H2(children='Medal', style=H2_STYLE),
    dcc.Dropdown(Amount_of_each_medal(df).Medal.unique(), id='medals', multi=True, style=SELECT_STYLE),

    html.H2(children='Sport', style=H2_STYLE),
    dcc.Dropdown(df.Sport.unique(), id='Sport',multi=True, style=SELECT_STYLE),

    html.H2(children='Event', style=H2_STYLE),
    dcc.Dropdown(id='Event', multi=True, style=SELECT_STYLE),

    html.H2(children='Years', style=H2_STYLE),
    dcc.RangeSlider(
        id='Years',
        min = df['Year'].min(), 
        max = df['Year'].max(), 
        value=[df['Year'].min(), df['Year'].max()],
        marks={year: str(year) for year in range(df['Year'].min(), df['Year'].max() + 1, 8)},
        allowCross=False,
    ),

], style=SIDEBAR_STYLE)

graph_totaL_medals=html.Div([
    dcc.Graph(id='total_medals',  style=CHARTS_STYLE),
])
mone_lisa = html.Div([
    html.H1(children='Best Countrys over time', style=CHART_TITLES_STYLE),
    dcc.Graph(id='Best_countrys_over_time',  style=CHARTS_STYLE),
    ])

map = html.Div([
    html.H1(children='Medals distribution worldwide', style=CHART_TITLES_STYLE),
    dcc.Graph(id="Medals_per_team_map",  style=MAP_CHARTS_STYLE)
    ], style=MAP_STYLE)

bar_charts = html.Div([

    html.H1(children='Distribution of Genders over time', style=CHART_TITLES_STYLE),
    dcc.Graph(id='Gender_over_time',  style=CHARTS_STYLE),

    html.H1(children='Total amount of participants per Age', style=CHART_TITLES_STYLE),
    dcc.Graph(id='participants_age',  style=CHARTS_STYLE),
    
    html.H1(children='Total amount of medals per country', style=CHART_TITLES_STYLE),
    dcc.Graph(id='Medals_team_long',  style=CHARTS_STYLE),

    html.H1(children='Total amount of medals per person', style=CHART_TITLES_STYLE),
    dcc.Graph(id='Medals_people_long',  style=CHARTS_STYLE),

    html.H1(children='Total amount of medals per sport', style=CHART_TITLES_STYLE),
    dcc.Graph(id='Medals_sport_long',  style=CHARTS_STYLE),

    html.H1(children='Total amount of medals per Event', style=CHART_TITLES_STYLE),
    dcc.Graph(id='Medals_event_long',  style=CHARTS_STYLE),

    ], style={'padding-top': '2.5em'})

Age_Gender_graphs= [
    dbc.Col([
            html.H1(children='Medal distribution- Sex', style=CHART_TITLES_STYLE),
            dcc.Graph(id='Medals_sex', style=CHARTS_STYLE)
        ], width=4),
    dbc.Col([
            html.H1(children='Medal distribution- Age', style=CHART_TITLES_STYLE),
            dcc.Graph(id='Medals_age', style=CHARTS_STYLE)
        ], width=8)
]

# Create the final layout
layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Row(sidebar), 
        ], width=3),
    
        dbc.Col([
            dbc.Row(html.H1(children='Olympics Analysed', style=TITLE_STYLE)),
            dbc.Row(dbc.Col(mone_lisa)),
            dbc.Row(Age_Gender_graphs),
            dbc.Row(map),
            dbc.Row(bar_charts),
        ], width=9)
    ])
])