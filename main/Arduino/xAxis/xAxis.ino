#include <AccelStepper.h>

#define motorInterfaceType 1
#define stepPin 2
#define dirPin 5
#define limitSwitchPin 9 // Change this to the pin connected to the limit switch

AccelStepper stepper(motorInterfaceType, stepPin, dirPin);

void setup()
{
  Serial.begin(9600);
  pinMode(limitSwitchPin, INPUT_PULLUP); // Set the limit switch pin as input with internal pull-up
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);
}

void loop()
{
  // Ensure this part is included in your loop() function
  if (digitalRead(limitSwitchPin) == LOW)
  { // Limit switch is pressed
    // Your existing code to stop the motor
    Serial.println("LIMIT_PRESSED");
    while (digitalRead(limitSwitchPin) == LOW)
      ;                               // Wait for the switch to be released
    Serial.println("LIMIT_RELEASED"); // Send a message when the switch is released
  }

  if (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n');
    if (command.startsWith("SPEED "))
    {
      int speed = command.substring(6).toInt();
      stepper.setMaxSpeed(speed);
    }
    else if (command.startsWith("ACCEL "))
    {
      int acceleration = command.substring(6).toInt();
      stepper.setAcceleration(acceleration);
    }
    else if (command.startsWith("MOVE "))
    {
      long steps = command.substring(5).toInt();
      stepper.moveTo(steps);
    }
  }
  stepper.run();
}
