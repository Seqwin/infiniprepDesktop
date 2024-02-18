import tkinter as tk
from tkinter import messagebox
import serial
import threading

try:
    ser = serial.Serial('COM7', 9600, timeout=1)  # Adjust the COM port as needed
except serial.SerialException:
    messagebox.showerror("Serial Connection Error", "Could not open port COM7. Check your connection and try again.")
    exit()

def send_command(command):
    ser.write(f"{command}\n".encode())

def listen_for_limit_switch():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            if line == "HOME":
                status_box.config(bg="green")
            elif line == "NOT_HOME":
                status_box.config(bg="red")

def send_parameters():
    speed = speed_entry.get()
    acceleration = acceleration_entry.get()
    steps = steps_entry.get()
    send_command(f"SPEED {speed}")
    send_command(f"ACCEL {acceleration}")
    send_command(f"MOVE {steps}")
    messagebox.showinfo("Info", "Commands sent")

def home_system():
    send_command("HOME")

root = tk.Tk()
root.title("Stepper Motor Controller")

tk.Label(root, text="Speed (steps/sec):").grid(row=0, column=0)
speed_entry = tk.Entry(root)
speed_entry.grid(row=0, column=1)

tk.Label(root, text="Acceleration (steps/sec^2):").grid(row=1, column=0)
acceleration_entry = tk.Entry(root)
acceleration_entry.grid(row=1, column=1)

tk.Label(root, text="Number of steps to move:").grid(row=2, column=0)
steps_entry = tk.Entry(root)
steps_entry.grid(row=2, column=1)

send_button = tk.Button(root, text="Send Commands", command=send_parameters)
send_button.grid(row=3, column=0, columnspan=2)

home_button = tk.Button(root, text="Home", command=home_system)
home_button.grid(row=4, column=0, columnspan=2)

status_box = tk.Label(root, text="Homed Status", bg="red")
status_box.grid(row=5, column=0, columnspan=2, sticky="ew")

# Start the thread to listen for limit switch status updates
threading.Thread(target=listen_for_limit_switch, daemon=True).start()

root.mainloop()
