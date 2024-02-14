#include <AccelStepper.h>

#define motorInterfaceType 1
#define stepPin 2
#define dirPin 5
#define limitSwitchPin 9

AccelStepper stepper(motorInterfaceType, stepPin, dirPin);

void setup()
{
  Serial.begin(9600);
  pinMode(limitSwitchPin, INPUT_PULLUP);
  stepper.setMaxSpeed(1000);    // Default speed
  stepper.setAcceleration(500); // Default acceleration
}

void loop()
{
  static bool isHoming = false;

  if (isHoming)
  {
    stepper.run();
    if (digitalRead(limitSwitchPin) == LOW)
    {
      stepper.setCurrentPosition(0); // Reset position to 0
      stepper.stop();                // Stop the motor
      isHoming = false;
      Serial.println("HOMED");
      // Optionally reset speed and acceleration to default or last known values
    }
    return; // Prevent processing other commands during homing
  }

  if (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n');
    if (command == "HOME")
    {
      isHoming = true;
      stepper.moveTo(-1000000);     // Move to ensure hitting the limit switch
      stepper.setMaxSpeed(200);     // Lower speed for homing
      stepper.setAcceleration(100); // Lower acceleration for homing
    }
    else if (command.startsWith("SPEED "))
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
      stepper.move(steps); // Use 'move' for relative movement
    }
  }

  stepper.run();
}
