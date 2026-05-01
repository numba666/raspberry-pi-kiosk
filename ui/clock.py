# ui/clock.py
from datetime import datetime

def update_clock(root, time_label, date_label):
    now = datetime.now()

    time_label.config(text=now.strftime("%H:%M"))
    date_label.config(text=now.strftime("%a, %d.%m.%Y"))

    root.after(30000, update_clock, root, time_label, date_label)