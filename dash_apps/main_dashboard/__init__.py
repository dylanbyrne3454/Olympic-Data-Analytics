from dash import Dash, dash_table, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


from .layout import layout
from .callbacks import register_callbacks


def main_dashboard_app(server):
    app = Dash(
        __name__,
        server=server,
        url_base_pathname='/main_dashboard/',
        external_stylesheets=[dbc.themes.CYBORG])
    app.layout = layout
    register_callbacks(app)
    return app
