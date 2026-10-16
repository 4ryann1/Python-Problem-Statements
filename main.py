
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
