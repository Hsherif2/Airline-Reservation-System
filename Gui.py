import tkinter as tk
from datetime import datetime

def create_widgets(self):
   self.main_menu_frame = tk.Frame(self)
        self.main_menu_frame.pack()
self.show_airline_button = tk.Button(self.main_menu_frame, text="Show Airline Schedules", command=self.show_airline, width=20, bg='gray')
        self.show_airline_button.pack(pady=10)


