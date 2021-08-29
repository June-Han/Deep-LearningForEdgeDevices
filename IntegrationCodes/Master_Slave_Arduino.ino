#include <Servo.h>

const int sw = 8;

Servo Myservo;

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT); // Fan
  pinMode(12, OUTPUT); // Pump
  pinMode(11, OUTPUT); // LED Light Strips
  pinMode(10, OUTPUT); // LED RED
  pinMode(9, OUTPUT); // LED GREEN
  // Switch [Not Required For RSPB Master- Arduino Slave] pinMode(sw, INPUT); 
  Myservo.attach(7); //servo.attach(pin) set pin to motor
}

void loop() {  
  
  if (Serial.available() > 0) {  
  
    String data = (Serial.readStringUntil('\n'));  
  
    Serial.print("Status ");   
    Serial.println(data);  
  
    if (data.equals("StartWash")) {  
      washing();
      drying();
    } 
    else if(data.equals("StartSter"))
    {
      ster();
      done(); 
    }
    else if(data.equals("Abort")) 
    { 
      exit(0);
    } 
}
}

void washing ()
{
  // Start of Operation (WASHING)
  Serial.println("Job Operation Starts\n"); 
  Serial.println("Process 1: Washing Starts");
        
  digitalWrite(13, LOW); // Fan off (WASHING)
  digitalWrite(11, LOW); // LED Light Strips off
  digitalWrite(9, LOW);  // Green LED off (In Process)
  digitalWrite(12, HIGH); // Pump on (WASHING)
  digitalWrite(10, HIGH); // Red LED ON (In Process)
      
  delay(20000); // Wait for x min (WASHING)
  Serial.println("Process 1: Washing Completed\n");
        
}

void drying ()
{
  // Washing Done, Now Drying
  Serial.println("Process 2: Drying Starts");
  Serial.println("Drying Starts -> Both Fan ON");
        
  digitalWrite(13, HIGH); // Fan ON (DRYING)
  digitalWrite(10, HIGH); // Red LED ON (In Process)
  digitalWrite(12, LOW); // Pump off (DRYING)
  digitalWrite(11, LOW); // LED Light Strips off (DRYING)
  digitalWrite(9, LOW); // Green LED off (In Process)
      
  delay(20000); // Wait for x min (DRYING)
  Serial.println("Process 2: Drying Completed\n");         
}

void ster ()
{
  // Drying Done, Now Sterilisation
  Serial.println("Process 3: Sterilisation Starts");
  Serial.println("Sterilisation Starts -> UV Lights ON");
        
  digitalWrite(13, LOW); // Fan off (Sterilisation)
  digitalWrite(12, LOW); // Pump off (Sterilisation)
  digitalWrite(11, HIGH); // LED Light Strips off (Sterilisation)
  digitalWrite(10, HIGH); // Red LED ON (In Process)
  digitalWrite(9, LOW); // Green LED off (In Process)
        
  delay(20000); // Wait for x min (Sterilisation)
  Serial.println("Process 3: Sterilisation Completed\n");
  
}

        
void done ()
{
  // Sterilisation Done, Process Completed
  Serial.println("Job Operation Completed");
  digitalWrite(13, LOW); // Fan off (Sterilisation)
  digitalWrite(12, LOW); // Pump off (Sterilisation)
  digitalWrite(11, LOW); // LED Light Strips off (Sterilisation)
  digitalWrite(10, LOW); // Red LED ON (In Process)
  digitalWrite(9, HIGH); // Green LED off (In Process)
  delay(5000);
        
  Myservo.write(0); // Original Position (No Process Currently)
  delay (1000); // Close Lid  
       
}