#include <AccelStepper.h>
#include <Encoder.h>

#define motorInterfaceType 1
#define stepPin 2
#define dirPin 5
#define limitSwitchPin 9
#define encoderPinA 18
#define encoderPinB 19

AccelStepper stepper(motorInterfaceType, stepPin, dirPin);
Encoder myEnc(encoderPinA, encoderPinB);

bool isHoming = false;
unsigned long lastEncoderRead = 0;
const unsigned long encoderReadInterval = 100; // Interval to read the encoder (ms)

void setup()
{
  Serial.begin(9600);
  pinMode(limitSwitchPin, INPUT_PULLUP);
  stepper.setMaxSpeed(1000);    // Default max speed, will be adjusted for homing
  stepper.setAcceleration(500); // Default acceleration, will be adjusted for homing
}

void loop()
{
  unsigned long currentMillis = millis();
  if (currentMillis - lastEncoderRead > encoderReadInterval)
  {
    long position = myEnc.read();
    Serial.print("Position: ");
    Serial.println(position);
    lastEncoderRead = currentMillis;
  }

  if (isHoming)
  {
    // Check if limit switch is pressed
    if (digitalRead(limitSwitchPin) == LOW)
    {
      stepper.setCurrentPosition(0); // Reset stepper position to 0
      stepper.stop();                // Stop the stepper
      stepper.move(20);              // Move a bit to ensure the limit switch is reset
      while (stepper.distanceToGo() != 0)
      {
        stepper.run();
      }
      delay(1000);    // Wait for 1 second
      myEnc.write(0); // Then reset encoder position to 0
      isHoming = false;
      Serial.println("HOMED");
      // Restore default speed and acceleration after homing
      stepper.setMaxSpeed(1000);
      stepper.setAcceleration(500);
    }
    else
    {
      stepper.run();
    }
    return;
  }
  // Process serial commands
  while (Serial.available() > 0)
  {
    String command = Serial.readStringUntil('\n');
    if (command == "HOME")
    {
      isHoming = true;
      stepper.moveTo(-1000000);     // Move to trigger the limit switch
      stepper.setMaxSpeed(500);     // Set homing speed
      stepper.setAcceleration(500); // Set homing acceleration
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
      stepper.move(command.substring(5).toInt());
    }
  }

  if (!isHoming)
    stepper.run();
}
