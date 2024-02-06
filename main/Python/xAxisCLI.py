import tkinter as tk
from tkinter import messagebox
import serial
import time

# Establish serial connection
try:
    ser = serial.Serial('COM7', 9600, timeout=1)
    time.sleep(2)  # Wait for the connection to establish
except serial.SerialException:
    messagebox.showerror("Serial Connection Error", "Could not open port COM7. Check your connection and try again.")
    exit()

def send_command(command):
    print(f"Sending: {command}")
    ser.write(f"{command}\n".encode())
    time.sleep(0.1)  # Short delay to ensure command is sent

def send_parameters():
    speed = speed_entry.get()
    acceleration = acceleration_entry.get()
    steps = steps_entry.get()
    
    # Send commands to the Arduino
    send_command(f"SPEED {speed}")
    send_command(f"ACCEL {acceleration}")
    send_command(f"MOVE {steps}")
    
    messagebox.showinfo("Info", "Commands sent")

# Set up the GUI
root = tk.Tk()
root.title("Stepper Motor Controller")

tk.Label(root, text="Speed (steps/sec):").grid(row=0, column=0)
speed_entry = tk.Entry(root)
speed_entry.grid(row=0, column=1)

tk.Label(root, text="Acceleration (steps/sec^2):").grid(row=1, column=0)
acceleration_entry = tk.Entry(root)
acceleration_entry.grid(row=1, column=1)

tk.Label(root, text="Absolute position, 0 is Home:").grid(row=2, column=0)
steps_entry = tk.Entry(root)
steps_entry.grid(row=2, column=1)

send_button = tk.Button(root, text="Send Commands", command=send_parameters)
send_button.grid(row=3, column=0, columnspan=2)

root.mainloop()

# Close serial connection on exit
ser.close()
