import pandas as pd
import os

def load_data():
    # Dynamically resolve the path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'athlete_events.csv')
    return pd.read_csv(csv_path)

df = load_data()


def Clean_data(season):
    df = load_data()
    df =  df.fillna({"Medal": "No Medal"})
    return df

def medal_counts(df):
    df = pd.read_csv('athlete_events.csv')
    new_df = df
    new_df = df.drop(["Name", "player_id", "Sex","NOC","Year","Season","City","Sport","Event",], axis=1)
    new_df= new_df[new_df["Medal"]!="No medal"]
    return new_df

def Total_amount(df):
    amount = df.count()
    return str(amount["ID"])

def Amount_of_each_medal(df):
    amount = df[df["Medal"]!="No Medal"].groupby(["Medal"]).count().reset_index(names="Medal").sort_values(["Medal"], ascending=True)
    return amount

def Amount_of_medals_per_team(df):
    df = df[["Team", "Medal"]]
    amount_per_team = df[df["Medal"]!="No Medal"]
    amount_per_team["total_count"] = amount_per_team.groupby(["Team"]).transform("count")
    amount_per_team["count"]= amount_per_team.groupby(["Team","Medal"])["Team"].transform("count")
    amount_per_team = amount_per_team.groupby(["Team","Medal"]).first().reset_index().sort_values(["total_count"], ascending=False).head(30).sort_values(["total_count"], ascending=True)
    return amount_per_team

def Amount_of_specific_medal_per_team(df, medal_type):
    df = df[["Team", "Medal"]]
    amount_per_team = df[df["Medal"]!="No Medal"]
    amount_per_team = df[df["Medal"]==medal_type]
    amount_per_team["total_count"] = amount_per_team.groupby(["Team"]).transform("count")
    amount_per_team["count"]= amount_per_team.groupby(["Team","Medal"])["Team"].transform("count")
    amount_per_team = amount_per_team.groupby(["Team","Medal"]).first().reset_index().sort_values(["total_count"], ascending=False).head(30).sort_values(["total_count"], ascending=True)
    return amount_per_team


def Amount_of_medals_per_person(df):
    df = df[["Name", "Medal"]]
    new_df = df[df["Medal"]!="No Medal"]
    new_df["total_count"] = new_df.groupby(["Name"]).transform("count")
    names = new_df.groupby("Name").first().reset_index().sort_values(["total_count"], ascending=False).head(10)
    names = names["Name"]

    amount = new_df[new_df["Name"].isin(names)]
    amount["count"]= amount.groupby(["Name","Medal"])["Name"].transform("count")
    amount = amount.groupby(["Name","Medal"]).first().reset_index().sort_values(["total_count"], ascending=True)
    return amount


def run_unit_test(df):
    
        dff = Amount_of_medals_per_person(df)
        
        
run_unit_test(df)

def Amount_of_medals_per_Sport(df):
    df = df[["Sport", "Medal"]]
    new_df = df[df["Medal"]!="No Medal"]
    new_df["total_count"] = new_df.groupby(["Sport"]).transform("count")
    sports = new_df.groupby("Sport").first().reset_index().sort_values(["total_count"], ascending=False).head(10)
    sports = sports["Sport"]

    amount = new_df[new_df["Sport"].isin(sports)]
    amount["count"]= amount.groupby(["Sport","Medal"])["Sport"].transform("count")
    amount = amount.groupby(["Sport","Medal"]).first().reset_index().sort_values(["total_count"], ascending=True)
    return amount

def Amount_of_medals_per_Event(df):
    df = df[["Event", "Medal"]]
    new_df = df[df["Medal"]!="No Medal"]
    new_df["total_count"] = new_df.groupby(["Event"]).transform("count")
    events = new_df.groupby("Event").first().reset_index().sort_values(["total_count"], ascending=False).head(10)
    events = events["Event"]

    amount = new_df[new_df["Event"].isin(events)]
    amount["count"]= amount.groupby(["Event","Medal"])["Event"].transform("count")
    amount = amount.groupby(["Event","Medal"]).first().reset_index().sort_values(["total_count"], ascending=True)
    return amount


def Amount_of_medals_per_team_NOC(df):
 
    df = df
    amount = df.replace("URS", "RUS")
    amount = amount.replace(to_replace=["Soviet Union", "Russia"], value="Soviet Union/Russia", inplace=True)
    amount = df[df["Medal"]!="No Medal"]
    amount = amount[["Team", "NOC"]]
    amount["Medal_count"] = amount.groupby(["Team", "NOC"])["Team"].transform("count")
    amount = amount.groupby("NOC").first().reset_index()
    Soviet_medals = amount[amount["Team"]=="Soviet Union"]
    print(Soviet_medals)
    return amount

def Total_amount_of_medals_per_team(df):
    df = df[["Team", "Medal"]]
    amount = df[df["Medal"]!="No Medal"].groupby(["Team"]).count().reset_index(names="Team").sort_values(["Medal"], ascending=False).head(10).sort_values(["Medal"], ascending=True)
    return amount

def Total_amount_of_medals_per_person(df):
    df = df[["Name", "Medal"]]
    amount = df[df["Medal"]!="No Medal"].groupby(["Name"]).count().reset_index(names="Name").sort_values(["Medal"], ascending=False).head(10).sort_values(["Medal"], ascending=False)
    return amount

def Total_amount_of_medals_per_sex(df):
    df = df[["Sex", "Medal"]]
    amount = df[df["Medal"]!="No Medal"].groupby(["Sex"]).count().reset_index(names="Sex")
    amount = amount.replace("M", "Male").replace("F", "Female")
    return amount

def Total_amount_of_participants_per_age(df):
    df = df[["Age", "Medal"]]
    amount = df.groupby(["Age"]).count().reset_index(names="Age")
    return amount
def Total_amount_of_medals_per_age(df):
    df = df[["Age", "Medal"]]
    amount = df[df["Medal"]!="No Medal"].groupby(["Age"]).count().reset_index(names="Age")
    return amount

def Amount_of_medals_per_gender_over_time(df):
    amount = df[df["Medal"]!="No Medal"].groupby(["Sex", "Year"]).size().sort_values(ascending=False)
    return amount

def Genders_over_time(df):
    amount = df[["Sex", "Year"]]
    amount = amount.replace("M", "Male").replace("F", "Female")
    amount["count"]= amount.groupby(["Sex","Year"])["Sex"].transform("count")
    amount = amount.groupby(["Sex","Year"]).first().reset_index()
    return amount

def Best_countrys_over_time(df):
    best_countrys = df[df["Medal"]!="No Medal"].groupby(["Team"]).count().reset_index(names="Team").sort_values(["Medal"], ascending=False).head(20)
    best_countryss = best_countrys["Team"]

    amount = df[df["Medal"]!="No Medal"]
    amount = amount[amount["Team"].isin(best_countryss)]
    amount = amount[["Team", "Year"]]
    amount["count"]= amount.groupby(["Team","Year"])["Team"].transform("count")
    amount = amount.groupby(["Team","Year"]).first().reset_index()
    return amount


#print(Amount_of_medals_per_gender_over_time(Clean_data()))
#print(Best_countrys_over_time(Clean_data()))
