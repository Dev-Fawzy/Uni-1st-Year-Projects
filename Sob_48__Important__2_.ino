int ldr = A1;
int tem = A2;
  
int ldrValue=0;
int temValue=0;

void setup() {
Serial.begin(9600); // Start serial communication at this speed 
}

void loop()
{
  ldrValue= analogRead(ldr);
  temValue= analogRead(tem);
  Serial.print("LDR= ");
  Serial.print(ldrValue);
  Serial.println();
  Serial.print("TEM= ");
  Serial.print(temValue);
  Serial.println();
  
  
Serial.println();// send the number to Serial port
Serial.println();// send New Line to Serial port
delay(1000);  // wait for 3 sec
}
