import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to save data to CSV
def save_to_csv():
    groom = groom_name.get()
    bride = bride_name.get()
    date_val = date.get()
    time_val = time.get()
    venue_val = venue.get()
    
    if not (groom and bride and date_val and time_val and venue_val):
        messagebox.showwarning("Missing Info", "All fields are required!")
        return

    # Save data to CSV
    file_exists = os.path.isfile("invitations.csv")
    with open("invitations.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Groom", "Bride", "Date", "Time", "Venue"])
        writer.writerow([groom, bride, date_val, time_val, venue_val])

    messagebox.showinfo("Success", "Invitation saved!")
    # Clear the fields
    groom_name.set("")
    bride_name.set("")
    date.set("")
    time.set("")
    venue.set("")

# Create the main window
root = tk.Tk()
root.title("Marriage Invitation Form")
root.geometry("400x350")
root.configure(bg="red")

# Variables to store input
groom_name = tk.StringVar()
bride_name = tk.StringVar()
date = tk.StringVar()
time = tk.StringVar()
venue = tk.StringVar()

# Labels and Entries
tk.Label(root, text="Groom Name", bg="lightgreen").pack(pady=5)
tk.Entry(root, textvariable=groom_name).pack()

tk.Label(root, text="Bride Name", bg="lightgreen").pack(pady=5)
tk.Entry(root, textvariable=bride_name).pack()

tk.Label(root, text="Wedding Date (YYYY-MM-DD)", bg="lightgreen").pack(pady=5)
tk.Entry(root, textvariable=date).pack()

tk.Label(root, text="Time", bg="lightgreen").pack(pady=5)
tk.Entry(root, textvariable=time).pack()

tk.Label(root, text="Venue", bg="lightgreen").pack(pady=5)
tk.Entry(root, textvariable=venue).pack()

# Submit Button
tk.Button(root, text="Submit Invitation", command=save_to_csv, bg="white").pack(pady=20)

root.mainloop()
