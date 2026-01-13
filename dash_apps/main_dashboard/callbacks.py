from dash.dependencies import Input, Output
from .data import *
import plotly.express as px

def register_callbacks(app):
    @app.callback(
        Output('Event', 'options'),
        Input('Sport', 'value'),
        Input('season', 'value'),
    )
    def Events(value, season):
        df = Clean_data(season)
        df = df[df["Sport"].isin(value)].Event.unique()
        print(value)
 
        return df


    @app.callback(
        Output('Teams', 'options'),
        Input('season', 'value'),
        
    )
    def Teams(season):
        return Clean_data(season).Team.unique()

    @app.callback(
        Output('Total_amount_competitors', 'children'),
        Output('Total_amount_of_medals', 'children'),
        Output('Total_amount_of_gold', 'children'),
        Output('Total_amount_of_silver', 'children'),
        Output('Total_amount_of_bronze', 'children'),
        Input('season', 'value'),
        Input('Sport', 'value')
    )
    def Update_number_data(value, season):
        df = Clean_data(season)
        amount = Total_amount(df)
        amount_of_medals = Total_amount(df[df["Medal"]!="No Medal"])
        amount_of_gold = Total_amount(df[df["Medal"]=="Gold"])
        amount_of_silver = Total_amount(df[df["Medal"]=="Silver"])
        amount_of_bronze = Total_amount(df[df["Medal"]=="Bronze"])

        return amount, amount_of_medals, amount_of_gold, amount_of_silver, amount_of_bronze

    @app.callback(
        Output('Medals_team_long', 'figure'),
        Output('Medals_people_long', 'figure'),
        Output('Medals_sport_long', 'figure'),
        Output('Medals_event_long', 'figure'),
        Output('Medals_sex', 'figure'),
        Output('Medals_age', 'figure'),
        Output('participants_age', 'figure'),
        Output('Gender_over_time', 'figure'),
        Output('Best_countrys_over_time', 'figure'),
        Output('Medals_per_team_map', 'figure'),

        Input('season', 'value'),
        Input('gender', 'value'),
        Input('Teams', 'value'),
        Input('medals', 'value'),
        Input('Sport', 'value'),
        Input('Event', 'value'),
        Input('Years', 'value'),
        
    )
    def update_bar_charts(season, gender, Teams, Medals, Sports, Events, Years):

        def create_fig_with_fixed_height(fig, height=500):
            fig.update_layout(
                autosize=False,
                height=height,
                margin=dict(l=50, r=50, t=50, b=50)
            )
            return fig

        df = Clean_data(season)
        print(season)
        print(gender)
        #Season
        if season=="Both":
            df=df.copy()
        else:
            df = df[df["Season"]==season].copy()
        #Gender
        if gender=="All":
            df=df.copy()
        elif gender=="Male":
            df = df[df["Sex"]=="M"].copy()
            print(gender)
        elif gender=="Female":
            df = df[df["Sex"]=="F"].copy()
            print(gender)
       # print(df.head(10))
        
        #Country
        if Teams is not None:
            df = df[df["Team"].isin(Teams)].copy()
        print(Teams)

        #Medals
        if Medals is not None:
            df = df[df["Medal"].isin(Medals)].copy()
        
        #Sport
        if Sports is not None:
            df = df[df["Sport"].isin(Sports)].copy()

        #Event
        if Events is not None:
            df = df[df["Event"].isin(Events)].copy()
        
        #Years 
        min_year, max_year = map(int, Years)
        print(min_year, max_year)
        df["Year"] = df["Year"].astype(int) 
        df = df[df["Year"] >= min_year] 
        df= df[df["Year"] <= max_year]
        
        
        return [
            create_fig_with_fixed_height(px.bar(Amount_of_medals_per_team(df), x='count', y="Team", color="Medal", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.bar(Amount_of_medals_per_person(df), x='count', y="Name", color="Medal", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.bar(Amount_of_medals_per_Sport(df), x='count', y="Sport", color="Medal", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.bar(Amount_of_medals_per_Event(df), x='count', y="Event", color="Medal", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.pie(Total_amount_of_medals_per_sex(df), values='Medal', names='Sex', title='Distribution of medals based on Sex', template='plotly_dark'), 400),
            create_fig_with_fixed_height(px.line(Total_amount_of_medals_per_age(df), x='Age', y="Medal", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.line(Total_amount_of_participants_per_age(df), x='Age', y="Medal", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.line(Genders_over_time(df), x='Year', y="count", color="Sex", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.line(Best_countrys_over_time(df), x='Year', y="count", color="Team", template='plotly_dark'), 500),
            create_fig_with_fixed_height(px.choropleth(
                Amount_of_medals_per_team_NOC(df), 
                locations="NOC",
                color="Medal_count",
                hover_name="Team", 
                color_continuous_scale=px.colors.sequential.Plasma,
                template='plotly_dark'
            ), 600),
        ]



