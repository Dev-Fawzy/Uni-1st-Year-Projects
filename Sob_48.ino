#include <SD.h>

const int ldrPin = A1;
const int tempPin = A0;

File dataFile;

void setup() {
  Serial.begin(9600); // Start serial communication
  SD.begin(10); // Initialize SD card (assuming pin 10 for CS)
}

void loop() {
  // Log sensor data to CSV file
  dataFile = SD.open("sensor_data.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(millis());
    dataFile.print(",");
    dataFile.print(analogRead(ldrPin));
    dataFile.print(",");
    dataFile.println(analogRead(tempPin));
    dataFile.close();
  } else {
    Serial.println("Error opening file for writing.");
  }

  int randomNumber = random(100); // Generate random number up to 100
  Serial.print("Random number: ");
  Serial.println(randomNumber);

  int ldrValue = analogRead(ldrPin);
  int tempValue = analogRead(tempPin);
  
  Serial.print("LDR= ");
  Serial.println(ldrValue);
  Serial.print("Temperature= ");
  Serial.println(tempValue);
  
  Serial.println(); // Send newline to Serial port
  delay(3000); // Wait for 3 sec
}
