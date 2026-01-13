import pandas as pd
from flask_app.models import SurveyResponse
import plotly.express as px
import os


def load_database():
    from flask import current_app
    
    with current_app.app_context():
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


def gender_pi(df):
    df = df[["Id", "Gender"]]
    counts = df["Gender"].value_counts().reset_index()
    return counts

def winter_vs_summer(df):
    df = df[["Id", "Summer_vs_Winter"]]
    counts = df["Summer_vs_Winter"].value_counts().reset_index()
    return counts

def become_olympian(df):
    df = df[["Id", "Become_olympian"]]
    counts = df["Become_olympian"].value_counts().reset_index()
    return counts

def age(df):
    df = df[["Id", "Age"]]
    counts = df["Age"].value_counts().reset_index()
    return counts

def country(df):
    df = df[["Id", "Country"]]
    counts = df["Country"].value_counts().reset_index()
    return counts

def sport(df):
    df = df[["Id", "Sport"]]
    counts = df["Sport"].value_counts().reset_index().sort_values(["count"], ascending=False)
    return counts

def athlete(df):
    df = df[["Id", "Athlete"]]
    counts = df["Athlete"].value_counts().reset_index().sort_values(["count"], ascending=False)
    return counts

def watch_olympics(df):
    df = df[["Id", "Watch_Olympics"]]
    counts = df["Watch_Olympics"].value_counts().reset_index().sort_values(["count"], ascending=False)
    return counts


