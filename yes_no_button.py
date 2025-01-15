import tkinter as tk

def on_yes_click():
    result_label.config(text="Okay!")

def on_no_click():
    result_label.config(text="Try again!")

# Set up the main window
root = tk.Tk()
root.title("Yes/No Button Game")

# Set the window size
root.geometry("500x300")

# Create the question label
question_label = tk.Label(root, text="Please give me your money", font=("Arial", 14))
question_label.pack(pady=20)

# Create the result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Calculate button positions
window_width = 500
window_height = 300
button_width = 80
button_height = 30

yes_button_x = (window_width // 2) - button_width - 10
no_button_x = (window_width // 2) + 10
buttons_y = window_height // 2

# Create Yes button
yes_button = tk.Button(root, text="Yes", command=on_yes_click, font=("Arial", 12))
yes_button.place(x=yes_button_x, y=buttons_y)

# Create No button
no_button = tk.Button(root, text="No", command=on_no_click, font=("Arial", 12))
no_button.place(x=no_button_x, y=buttons_y)

# Run the application
root.mainloop()
