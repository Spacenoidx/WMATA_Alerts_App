# Importing modules

import os

import requests
from dotenv import load_dotenv

# load environment variables ("YOUR_API_KEY")

load_dotenv()


api_key = os.environ.get('YOUR_API_KEY')

url = "https://api.wmata.com/Incidents.svc/json/BusIncidents"

headers = {'api_key': api_key}
response = requests.get(url, headers=headers)
data = response.json()
data = data["BusIncidents"]

# this function returns the alerts in a list of strings. It is accessed in main.py
# and used to populate the listbox with tkinter methods.
def get_alerts():
    alert_list = []

    for incident in data:
        alert = f"{incident['Description']}. Routes affected: {incident['RoutesAffected']}"
        alert_list.append(alert)
    return alert_list



