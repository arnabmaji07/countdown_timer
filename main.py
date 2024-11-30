import tkinter as tk
from tkinter import messagebox
import time

# Function to start the countdown timer
def start_timer():
    try:
        countdown_time = int(entry.get())
        for t in range(countdown_time, -1, -1):
            mins, secs = divmod(t, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}",bg="aqua")
            root.update()
            time.sleep(1)

        # Show a message box when the timer completes
        messagebox.showinfo("Countdown Timer", "Time's up!")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")
root.configure(bg="blue")
# Create and configure a Label widget for displaying the timer
timer_label = tk.Label(root, text="00:00", font=("Arial", 36),bg="aqua")
timer_label.pack(pady=20)

# Create and configure an Entry widget for entering the countdown time
entry = tk.Entry(root, font=("Arial", 18))
entry.pack()

# Create and configure a Start button to begin the countdown
start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack(pady=10)

# Start the GUI application
root.mainloop()
