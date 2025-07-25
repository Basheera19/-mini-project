import tkinter as tk
from tkinter import messagebox
import csv
import os

# File path for CSV
csv_file = 'quiz_data.csv'

# Create CSV file with headers if not exists
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer'])

# Submit function
def submit_data():
    question = entry_question.get()
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    d = entry_d.get()
    answer = entry_answer.get().upper()

    if not (question and a and b and c and d and answer in ['A', 'B', 'C', 'D']):
        messagebox.showerror("Input Error", "Please fill all fields and ensure correct answer is A, B, C, or D.")
        return

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([question, a, b, c, d, answer])
    
    messagebox.showinfo("Success", "Question added successfully!")
    
    # Clear fields
    entry_question.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_d.delete(0, tk.END)
    entry_answer.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Quiz Entry Form")

tk.Label(root, text="Question").grid(row=0, column=0)
entry_question = tk.Entry(root, width=60)
entry_question.grid(row=0, column=1, columnspan=3)

tk.Label(root, text="Option A").grid(row=1, column=0)
entry_a = tk.Entry(root, width=30)
entry_a.grid(row=1, column=1)

tk.Label(root, text="Option B").grid(row=1, column=2)
entry_b = tk.Entry(root, width=30)
entry_b.grid(row=1, column=3)

tk.Label(root, text="Option C").grid(row=2, column=0)
entry_c = tk.Entry(root, width=30)
entry_c.grid(row=2, column=1)

tk.Label(root, text="Option D").grid(row=2, column=2)
entry_d = tk.Entry(root, width=30)
entry_d.grid(row=2, column=3)

tk.Label(root, text="Correct Answer (A/B/C/D)").grid(row=3, column=0)
entry_answer = tk.Entry(root, width=10)
entry_answer.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=1, pady=10)

root.mainloop()