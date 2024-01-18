# loading modules and libraries needed

from backend.utils import get_alerts
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()


# Creating a window class
class MyWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        # window basics
        self.title("WMATA Bus Alerts")
        self.geometry("600x400")
        self.configure(bg="lightgray")

        self.toplabel = tk.Label(text="Search for WMATA Bus alerts", bg="lightgray")
        self.toplabel.pack()
        # the entry field and StringVar that will be wrking on the listbox
        # self.URLfield = self.create_entry_field(label_text="Enter URL here...", width=30)
        self.textentry_var = tk.StringVar()
        self.textentry = tk.Entry(self, textvariable=self.textentry_var)

        self.textentry.bind("<KeyRelease>", self.on_entry_key_release)
        self.textentry.pack()

        # creating the alerts list the first time
        self.alert_list = get_alerts()

        # the listbox populated by the alerts function

        self.listbox = tk.Listbox(self, height=20, width=60)
        self.listbox.pack()

        # self.button1 = tk.Button(self, bg="lightgrey", text="Print", fg="black", command=self.text_test)
        # self.button1.pack()

        self.button2 = tk.Button(self, bg="lightgrey", text="Download Data", fg="black", command=self.populate_listbox)
        self.button2.pack()

        # Bind the show_full_entry method to the double click event
        self.listbox.bind("<Double-Button-1>", self.show_full_entry)

    # function to display a messagebox with the whole entry selected
    def show_full_entry(self, event):
        # Get the selected item from the listbox
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index)
            # Display a messagebox with the full entry
            messagebox.showinfo("More Info", f"Alert: {selected_item}")


    # keybind is accessed by this function

    def on_entry_key_release(self, event):
        # Get the current content of the entry
        current_text = self.textentry_var.get().lower()

        self.listbox.delete(0, tk.END)

        for item in get_alerts():
            if current_text in item.lower():
                self.listbox.insert(tk.END, item)

    # this function uses a function from backend.utils to populate the listbox
    # self.alert_list = get_alerts() from backend.utils
    def populate_listbox(self):
        self.listbox.delete(1, 100)
        for alert in self.alert_list:
            self.listbox.insert(tk.END, alert)
        return self.alert_list


if __name__ == "__main__":
    app = MyWindow()

# We populate the listbox before the main loop.
    app.populate_listbox()
    app.mainloop()
