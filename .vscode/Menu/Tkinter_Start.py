import tkinter as tk

# Function to change the background color on hover
def on_enter(e):
    button.config(bg="lightgreen")  # Change background color on hover

# Function to reset the background color when hover ends
def on_leave(e):
    button.config(bg="lightblue")  # Reset background color when mouse leaves

# Create the main window
root = tk.Tk()
root.title("Button Hover Effect")

# Create the button
button = tk.Button(root, text="Hover Me!", font=("Helvetica", 20), bg="lightblue", fg="black")
button.pack(pady=50)

# Bind hover events to the button
button.bind("<Enter>", on_enter)  # Mouse enter
button.bind("<Leave>", on_leave)  # Mouse leave

# Run the application
root.mainloop()
