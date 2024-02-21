#include <AccelStepper.h>

// Define motor interface type and pin connections
#define motorInterfaceType 1
#define stepPin 2
#define dirPin 5
#define limitSwitchPin 9

// Initialize the AccelStepper library
AccelStepper stepper(motorInterfaceType, stepPin, dirPin);

bool isHoming = false; // Flag to indicate if the system is currently in the homing process

void setup()
{
  Serial.begin(9600);                    // Start serial communication at 9600 baud
  pinMode(limitSwitchPin, INPUT_PULLUP); // Configure the limit switch pin as input with pull-up resistor

  // Set initial speed and acceleration:
  stepper.setMaxSpeed(1000);    // steps per second
  stepper.setAcceleration(500); // steps per second squared
}

void loop()
{
  // Homing process logic

  if (isHoming)
  {
    // Perform homing by moving the stepper until the limit switch is triggered
    if (digitalRead(limitSwitchPin) == LOW)
    {                                // Check if limit switch is pressed
      Serial.println("HOME");        // Send homing completion message
      stepper.stop();                // Stop the stepper motor
      stepper.setCurrentPosition(0); // Set the current position as 0 (home)
      stepper.moveTo(24);            // Ensure the stepper is stopped
      isHoming = false;              // Exit homing mode
    }
    stepper.run(); // Continuously run the stepper motor towards the home position
    return;        // Skip the rest of the loop while homing
  }

  // Regular operation for handling serial commands
  if (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n'); // Read the incoming command

    if (command == "HOME")
    {
      isHoming = true;              // Set the homing flag
      stepper.moveTo(-1000000);     // Move stepper to trigger limit switch, adjust as necessary
      stepper.setMaxSpeed(200);     // Use a lower speed for homing
      stepper.setAcceleration(100); // Use a lower acceleration for homing
    }
    else if (command.startsWith("SPEED "))
    {
      stepper.setMaxSpeed(command.substring(6).toInt()); // Set max speed
      Serial.println("NOT_HOME");                        // ERIC ADDED**************************
    }
    else if (command.startsWith("ACCEL "))
    {
      stepper.setAcceleration(command.substring(6).toInt()); // Set acceleration
      Serial.println("NOT_HOME");                            // ERIC ADDED**************************
    }
    else if (command.startsWith("MOVE "))
    {
      long steps = command.substring(5).toInt(); // Parse the number of steps to move
      stepper.move(steps);                       // Move the stepper a relative distance
      Serial.println("NOT_HOME");                // ERIC ADDED**************************
    }
  }

  stepper.run(); // Execute step movement
}