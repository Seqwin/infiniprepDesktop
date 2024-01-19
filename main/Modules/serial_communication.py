import serial
import time

def communicate_with_arduino():
    port = "COM6"
    baud_rate = 9600

    try:
        with serial.Serial(port, baud_rate, timeout=5) as ser:
            time.sleep(2)

            # Send message as bytes
            message_to_arduino = b"Hello Arduino!"
            ser.write(message_to_arduino)

            print(f"Sent to Arduino: {message_to_arduino.decode()}")

            # Read the response from the Arduino
            response_from_arduino = ser.readline().decode().strip()
            print(f"Received from Arduino: {response_from_arduino}")

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    communicate_with_arduino()