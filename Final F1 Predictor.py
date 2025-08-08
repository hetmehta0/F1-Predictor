# ------------------ IMPORTS ------------------
import fastf1 as f1 # get data
import pandas as pd # store data
import numpy as np # do maths
import json # store additional data
import os # retrieve data
from sklearn.linear_model import LogisticRegression  # for DNF classification
import xgboost as xgb

# ------------------ CONSTANTS ------------------
team_strength = {
    "McLaren": 10, "Mercedes": 9, "Red Bull Racing": 8, "Ferrari": 7,
    "Williams": 6, "Haas F1 Team": 5, "Aston Martin": 4, "Racing Bulls": 3,
    "Kick Sauber": 2, "Alpine": 1,
}

team_name_mapping = {'Alfa Romeo': 'Sauber', 'AlphaTauri': 'Racing Bulls', 'RB': 'Racing Bulls'}
retired_drivers = ['bottas', 'zhou', 'sargeant', 'kevin_magnussen', 'ricciardo', 'perez', 'doohan']
rookies = ['bearman', 'hadjar', 'colapinto', 'bortoleto', 'antonelli', 'lawson']

CHAR_FILE = 'track_characteristics.json'
current_year  = 2025
current_track = 'Japan'
session_type = 'R'

# ------------------ LOADING DATA ------------------
f1.Cache.enable_cache('f1_cache')

def load_data():
    if os.path.exists(CHAR_FILE):
        with open(CHAR_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(CHAR_FILE, "w") as f:
        json.dump(data, f, indent=2)

session = f1.get_session(current_year, current_track, session_type) #load the data
session.load()
laps_data = session.laps
drivers = session.results

# ------------------ SETUP DATA ------------------
laps_df = s