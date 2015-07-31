void setup() {  
  // initialize the digital pin as an output.  
  // Pin 8 is our output pin  
  pinMode(8, OUTPUT);  
}  

void loop() {  
  digitalWrite(8, HIGH); 
  // set the LED on  
  delay(1000); 
  // wait for a second  
  digitalWrite(8, LOW); 
  // set the LED off  
  delay(1000);                  
  // wait for a second  
}

