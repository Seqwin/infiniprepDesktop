import serial
import time

def send_axes_values(ser, axes_values):
    message = ",".join(f"{axis}:{value}" for axis, value in axes_values.items()) + "\n"
    ser.write(message.encode())
    time.sleep(1)  # Adjust this delay based on your needs

if __name__ == "__main__":
    # Replace with your actual serial port and baudrate
    serial_port = "/dev/ttyUSB0"
    baud_rate = 9600

    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        time.sleep(2)  # Allow time for the Arduino to initialize

        # Example: Send values for X, Y, Z, and A axes to Arduino
        axes_values = {"X": 42, "Y": 30, "Z": 15, "A": 60}
        send_axes_values(ser, axes_values)
