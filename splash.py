import tkinter as tk

def close_splash():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("")

# Set the window size and position
root.geometry("225x65+500+300")  # Adjusted size

# Create a label with the splash screen message
splash_label = tk.Label(root, text="CW is loading...", font=("Helvetica", 16))
splash_label.pack(pady=20)

# Schedule the splash screen to close after 5 seconds
root.after(3000, close_splash)

# Run the Tkinter event loop
root.mainloop()
