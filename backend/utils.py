import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get('YOUR_API_KEY')

url = "https://api.wmata.com/Incidents.svc/json/BusIncidents"

headers = {'api_key': api_key}
response = requests.get(url, headers=headers)
data = response.json()
data = data["BusIncidents"]
print(data)


def get_alerts():
    alert_list = []

    for incident in data:
        alert = f"{incident['Description']}. Routes affected: {incident['RoutesAffected']}"
        alert_list.append(alert)
    return alert_list

def list_alerts(get_alerts):
    for alert in get_alerts:
        pass





# class MyWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("WMATA Alerts")
#         self.geometry("300x200")
#         self.configure(bg="lightgray")
#
#         # self.URLfield = self.create_entry_field(label_text="Enter URL here...", width=30)
#         self.URLentry = tk.Entry(self)
#         self.URLentry.pack()
#         self.listbox = tk.Listbox(self)
#         self.listbox.pack()
#
#         self.panel = tk.Label(self)  # Create a label for the image
#         self.button1 = tk.Button(self, bg="lightgrey",text="Load Image...", fg="black", command=self.get_the_URL)
#         self.button1.pack()
#         self.panel.pack()  # Position the label in the window
#
#     def get_the_URL(self):
#         link = self.URLentry.get()
#         print(link)
#         return link



