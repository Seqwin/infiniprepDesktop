#include <AccelStepper.h>

// Define motor interface type and pins used for the motor driver
#define motorInterfaceType 1 // For A4988 or similar driver, this is usually set to 1
#define stepPin 2 // Connect this to the step pin on the CNC shield
#define dirPin 5  // Connect this to the direction pin on the CNC shield

// Initialize the AccelStepper library
AccelStepper stepper(motorInterfaceType, stepPin, dirPin);

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 bauds
  
  // Set the maximum speed and acceleration of the motor.
  stepper.setMaxSpeed(10000); // Maximum steps per second, adjust as needed
  stepper.setAcceleration(500); // Steps per second per second, adjust as needed

  // Move to the initial position, which is 0 in this case
  stepper.moveTo(0);
}

void loop() {
  // Continuously moves the motor towards the target position
  stepper.run();

  // Check if the stepper has reached its target position

    // If the current position is 0, move to 123. Otherwise, move to 0.
  if (stepper.currentPosition() == 0) {
    stepper.moveTo(1000); // Move from 0 to 123
  } else if (stepper.currentPosition() == 1000) {
    stepper.moveTo(0); // Move from 123 back to 0
  }

}
