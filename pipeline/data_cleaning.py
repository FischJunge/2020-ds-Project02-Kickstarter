# Importing libraries
import numpy as np
import pandas as pd
import json
from datetime import datetime

def drop_columns(df:pd.DataFrame):
    """Drops unused columns."""

    df = df.drop(columns=['friends','is_backing','is_starred','permissions','currency_symbol','photo','profile','source_url','urls','currency_trailing_code', 'current_currency','disable_communication', 'is_starrable','spotlight','staff_pick', 'static_usd_rate','usd_type','converted_pledged_amount', 'pledged','backers_count','usd_pledged','creator','location'])
    return df

def drop_rows(df:pd.DataFrame):
    """Drops the rows of canceled, suspended and live states as well as rows of duplicates in the column id."""

    df = df.drop(df[(df.state == 'canceled')|(df.state == 'suspended')|(df.state == 'live')].index)
    df = df.drop_duplicates(subset=['id'], keep='last')
    df = df.drop(columns='id')
    return df

def get_category(df:pd.DataFrame):
    """Extracts the category parent id and makes a new column for the feature and drops the column category."""

    a = df.category.apply(json.loads).values.tolist()
    df = df.join(pd.DataFrame.from_records(a)["parent_id"])
    df = df.rename(columns={"parent_id": "category_parent_id"})
    df = df.drop(columns='category')
    return df

def get_creator(df:pd.DataFrame): 
    """Extracts the creator name and makes a new column for the feature and drops the column creator_name."""

    a = df.creator.apply(json.loads).values.tolist()
    df = df.join(pd.DataFrame.from_records(a)["name"],rsuffix="_other")
    df = df.rename(columns={"name_other": "creator_name"})
    df = df.drop(columns='creator')
    return df
    
def get_location(df:pd.DataFrame):
    """Extracts the location name and state and makes a new column for the location name and state and drops the column location."""

    a = df.location.apply(json.loads).values.tolist()
    df = df.join(pd.DataFrame.from_records(a)["name","state"],rsuffix="_other")
    df = df.rename(columns={"name_other": "location_name","state_other": "location_state"})
    df = df.drop(columns='location')
    return df

def get_time(df:pd.DataFrame):
    """Creates human readable time based on UNIX time stamps and makes new columns for the human readable time."""

    df["created_at_rd"] = [datetime.fromtimestamp(x) for x in df["created_at"]]
    df["deadline_rd"] = [datetime.fromtimestamp(x) for x in df["deadline"]]
    df["launched_at_rd"] = [datetime.fromtimestamp(x) for x in df["launched_at"]]
    df["state_changed_at_rd"] = [datetime.fromtimestamp(x) for x in df["state_changed_at"]]
    return df

def replace_missing_data(df:pd.DataFrame):
    """Replaces missing blurbs with the project name, missing creator names with John Doe, missing location states with country, missing location names with location states and missing category parent ids with 27."""
    
    df.loc[df['blurb'].isnull(),'blurb'] = df['name']
    #df.loc[df['creator_name'].isnull(),'creator_name'] = "John Doe"
    #df.loc[df['location_state'].isnull(),'location_state'] = df['country']
    #df.loc[df['location_name'].isnull(),'location_name'] = df['location_state']
    df.loc[df['category_parent_id'].isnull(),'category_parent_id'] = 27
    df = df.drop(columns="country")
    return df
