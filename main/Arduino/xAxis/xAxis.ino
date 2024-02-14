#include <AccelStepper.h>

#define stepPin 2
#define dirPin 5
#define motorInterfaceType 1
#define limitSwitchPin 9 // Pin connected to the limit switch

AccelStepper stepper(motorInterfaceType, stepPin, dirPin);

void setup()
{
  Serial.begin(9600);
  pinMode(limitSwitchPin, INPUT_PULLUP);
  stepper.setMaxSpeed(1000);    // Set the maximum steps per second
  stepper.setAcceleration(500); // Set the acceleration in steps per second squared
}

void loop()
{
  // Check the status of the limit switch
  if (digitalRead(limitSwitchPin) == LOW)
  {
    // Limit switch is pressed
    Serial.println("LIMIT_PRESSED");
    stepper.stop(); // Optional: Stop the stepper immediately or take other actions
  }
  else
  {
    // Limit switch is unpressed
    Serial.println("LIMIT_RELEASED");
  }

  // Process incoming serial commands
  if (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n');
    if (command.startsWith("SPEED "))
    {
      stepper.setMaxSpeed(command.substring(6).toInt());
    }
    else if (command.startsWith("ACCEL "))
    {
      stepper.setAcceleration(command.substring(6).toInt());
    }
    else if (command.startsWith("MOVE "))
    {
      long steps = command.substring(5).toInt();
      stepper.move(steps); // 'move' for relative movement
    }
  }

  stepper.run();
  delay(100); // Add a small delay to reduce constant sending of the limit switch status
}
