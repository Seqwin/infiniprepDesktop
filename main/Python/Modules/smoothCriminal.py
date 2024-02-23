import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graphs(a, b, c, d, time_period):
    t = np.linspace(0, time_period, num=500)
    velocity = a * t**3 + b * t**2 + c * t + d
    acceleration = 3*a * t**2 + 2*b * t + c
    jerk = 6*a * t + 2*b
    position = a * t**4 / 4 + b * t**3 / 3 + c * t**2 / 2 + d * t
    
    fig, axs = plt.subplots(4, 1, figsize=(8, 12))
    
    axs[0].plot(t, position, label='Position')
    axs[0].set_title('Position over Time')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Position (steps)')
    
    axs[1].plot(t, velocity, label='Velocity')
    axs[1].set_title('Velocity over Time')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Velocity (steps/s)')
    
    axs[2].plot(t, acceleration, label='Acceleration')
    axs[2].set_title('Acceleration over Time')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Acceleration (steps/s²)')
    
    axs[3].plot(t, jerk, label='Jerk')
    axs[3].set_title('Jerk over Time')
    axs[3].set_xlabel('Time (s)')
    axs[3].set_ylabel('Jerk (steps/s³)')
    
    for ax in axs:
        ax.grid(True)
        ax.legend()
    
    plt.tight_layout()
    plt.show()

def calculate_and_plot():
    target_velocity = float(target_velocity_entry.get())
    time_period = float(time_period_entry.get())
    
    # Calculate coefficients
    a = -2 * target_velocity / (time_period ** 3)
    b = 3 * target_velocity / (time_period ** 2)
    c = 0
    d = 0
    
    # Update the GUI with calculated values
    coefficients_var.set(f"Velocity Coefficients:\na: {a}\nb: {b}\nc: {c}\nd: {d}")
    
    # Plot graphs
    plot_graphs(a, b, c, d, time_period)

# Create the main window
root = tk.Tk()
root.title("Acceleration Profile Calculator")

# Create and grid the layout frames
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variables
target_velocity_var = tk.StringVar()
time_period_var = tk.StringVar()
coefficients_var = tk.StringVar()

# Create widgets
target_velocity_label = ttk.Label(mainframe, text="Target Steps/Second:")
target_velocity_label.grid(column=1, row=1, sticky=tk.W)
target_velocity_entry = ttk.Entry(mainframe, width=7, textvariable=target_velocity_var)
target_velocity_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

time_period_label = ttk.Label(mainframe, text="Time Period (Seconds):")
time_period_label.grid(column=1, row=2, sticky=tk.W)
time_period_entry = ttk.Entry(mainframe, width=7, textvariable=time_period_var)
time_period_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

calculate_button = ttk.Button(mainframe, text="Calculate", command=calculate_and_plot)
calculate_button.grid(column=2, row=3, sticky=tk.W)

coefficients_label = ttk.Label(mainframe, textvariable=coefficients_var)
coefficients_label.grid(column=1, row=4, columnspan=2, sticky=tk.W)

# Add padding to the widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the application
if __name__ == "__main__":
    root.mainloop()
