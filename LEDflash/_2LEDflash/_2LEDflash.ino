void setup() {  
  // initialize the digital pins as an output.  
  pinMode(8, OUTPUT);  
  pinMode(9, OUTPUT);  
}  
  
void loop() {  
    digitalWrite(8, HIGH); 
    // set the LED on  
    digitalWrite(9, LOW); 
    // set the LED on  
    delay(1000); 
    // wait for a second  
    digitalWrite(8, LOW); 
    // set the LED off  
    digitalWrite(9, HIGH); 
    // set the LED on  
    delay(1000); 
    // wait for a second  
}


