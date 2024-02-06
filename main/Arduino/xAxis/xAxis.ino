#include <AccelStepper.h>

// Define motor interface type and pins used for the motor driver
#define motorInterfaceType 1
#define stepPin 2
#define dirPin 5

// Initialize the AccelStepper library
AccelStepper stepper(motorInterfaceType, stepPin, dirPin);

void setup()
{
  Serial.begin(9600);
  while (!Serial)
    ; // Wait for serial port to connect

  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);
}

void loop()
{
  if (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n');

    if (command.startsWith("SPEED "))
    {
      int speed = command.substring(6).toInt();
      stepper.setMaxSpeed(speed);
      Serial.println("Speed set");
    }
    else if (command.startsWith("ACCEL "))
    {
      int acceleration = command.substring(6).toInt();
      stepper.setAcceleration(acceleration);
      Serial.println("Acceleration set");
    }
    else if (command.startsWith("MOVE "))
    {
      long steps = command.substring(5).toInt();
      stepper.moveTo(steps);
      Serial.println("Moving");
    }
    else if (command.startsWith("DIR "))
    {
      int direction = command.substring(4).toInt();
      long currentPosition = stepper.currentPosition(); // Get current position
      // Set the direction by moving to a position relative to the current one
      if (direction == 1)
      {
        stepper.moveTo(currentPosition + 10000); // Arbitrary large number for continuous movement
      }
      else if (direction == -1)
      {
        stepper.moveTo(currentPosition - 10000); // Move in the opposite direction
      }
      Serial.println("Direction set");
    }
  }
  stepper.run();
}
