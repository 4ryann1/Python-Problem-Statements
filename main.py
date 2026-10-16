import tkinter as tk
from tkinter import messagebox

# 1. Create the main application window
root = tk.Tk()
root.title("My First Python UI")
root.geometry("1920x1080")  # Width x Height


submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#4CAF50", fg="white")
submit_button.pack(pady=15)

# 4. Start the application's event loop
root.mainloop()
