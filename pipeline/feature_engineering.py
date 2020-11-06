# Importing libraries
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import RobustScaler

def feat_goal_duration(df:pd.DataFrame):
    """Converts goal to USD and computes the duration between project launch and deadline and the duration between project creation and launch."""

    # Goal in USD
    df["usd_goal"] = df.goal * df.fx_rate

    # Project duration in days
    df["duration_days"] = round((df.deadline - df.launched_at)/(60*60*24))
    df["duration_days_prep"] = round((df.launched_at - df.created_at)/(60*60*24))

    # Drop columns
    df = df.drop(columns=["goal","currency","fx_rate","created_at", "deadline", "launched_at", "state_changed_at"])
    return df

def feat_time(df:pd.DataFrame):
    """Computes the season of the project deadline and whether the launch and deadline were on the weekend or not."""
    # Year, month and weekday
    df["year_deadline"] = pd.DatetimeIndex(df['deadline_rd']).year
    df["month_deadline"] = pd.DatetimeIndex(df['deadline_rd']).month
    df["weekday_deadline"] = pd.DatetimeIndex(df['deadline_rd']).weekday
    df["weekday_launched_at"] = pd.DatetimeIndex(df['launched_at_rd']).weekday
    
    # Which season is the month in?
    winter = [12,1,2]
    spring = [3,4,5]
    summer = [6,7,8]

    df['winter_deadline'] = np.where(df['month_deadline'].isin(winter), True, False)
    df['spring_deadline'] = np.where(df['month_deadline'].isin(spring), True, False)
    df['summer_deadline'] = np.where(df['month_deadline'].isin(summer), True, False)

    # Is the weekday on the weekend?
    weekend = [5,6]

    df['deadline_weekend'] = np.where(df['weekday_deadline'].isin(weekend), True, False)
    df['launched_weekend'] = np.where(df['weekday_launched_at'].isin(weekend), True, False)

    # Create dummies for the five relevant columns.
    df = pd.get_dummies(df, columns=["winter_deadline","spring_deadline","summer_deadline","deadline_weekend","launched_weekend"],drop_first=True)

    # Drop columns
    df = df.drop(columns=["created_at_rd","deadline_rd","launched_at_rd","state_changed_at_rd","month_deadline","weekday_deadline","weekday_launched_at"])
    return df

def feat_location(df:pd.DataFrame):
    """Defines whether location of creator is on the eastcoast."""
    # Change location_state to a boolean operator in two columns for eastcoast
    eastern = ["ME","NH","VT","NY","MA","RI","CT","NJ","PA","DE","MD","DC","MI","OH","IN","IL","WI","WV","VA","NC","TN","KY","SC","GA","AL","MS","FL"]
    df['eastcoast'] = np.where(df['location_state'].isin(eastern), True, False)

    # Create dummies
    df = pd.get_dummies(df, columns=['eastcoast'], drop_first=True)

    # Drop columns
    df = df.drop(columns=["location_name","location_state"])
    return df

def feat_text(df:pd.DataFrame):
    """Defines text features regarding blurb, project name, state and creator name."""

    # Change blurb to a boolean operator for long or short blurb based on word count.
    df['blurb_nwords'] = df['blurb'].str.count(' ') + 1
    bmean = df.blurb_nwords.mean()
    df['long_blurb'] = np.where(df['blurb_nwords'] >= bmean, True, False)

    # Change name to a boolean operator for long or short project name based on word count.
    df['name_nwords'] = df['name'].str.count(' ') + 1
    nmean = df.name_nwords.mean()
    df['long_name'] = np.where(df['name_nwords'] >= nmean, True, False)

    # Change state to a boolean operator for successful and failed.
    df['state_b'] = np.where(df['state'] == 'successful', True, False)

    # Change creator name to a boolean operator for long or short creator name based on word count.
    #df['creator_name_nwords'] = df['creator_name'].str.count(' ') + 1
    #df['long_creator_name'] = np.where(df['creator_name_nwords'] > 2, True, False)

    # Create dummies
    df = pd.get_dummies(df, columns=['long_blurb','long_name','state_b'], drop_first=True)
    
    # Drop columns
    df = df.drop(columns=['blurb','blurb_nwords','name','name_nwords','slug','state'])
    return df

def scale_X(X):
    """Scales the columns that do not contain dummy variables using robust scaler."""
    # Define columns to scale
    col_scale = ['category_parent_id','usd_goal', 'duration_days','duration_days_prep','year_deadline']

    # Scale columns
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X[col_scale])
    
    # Concatenating scaled and dummy columns 
    X = np.concatenate([X_scaled, X.drop(col_scale, axis=1)], axis=1)
    return X