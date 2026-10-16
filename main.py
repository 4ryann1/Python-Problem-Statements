import tkinter as tk
from tkinter import messagebox

# 1. Create the main application window
root = tk.Tk()
root.title("My First Python UI")
root.geometry("1920x1080")  # Width x Height

# 2. Define a function for the button action
def on_submit():
    user_text = entry.get()  # Get text from the input box
    if user_text.strip():
        messagebox.showinfo("Success", f"Chal re laudya: {user_text}")
    else:
        messagebox.showwarning("Warning", "Please enter something first!")

# 3. Add widgets (components) to the window
# Text Label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)  # pady adds vertical spacing

# Input Box (Entry field)
entry = tk.Entry(root, width=30, font=("Arial", 11))
entry.pack(pady=5)

# Action Button
submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#4CAF50", fg="white")
submit_button.pack(pady=15)

# 4. Start the application's event loop
root.mainloop()
