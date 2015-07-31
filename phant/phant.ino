#include <Phant.h>

// Arduino example stream
// http://data.sparkfun.com/streams/JxKL26QavvIEnompV5vl
// hostname, public key, private key
Phant phant("data.sparkfun.com", "JxKL26QavvIEnompV5vl", "gzNJAw10GGUrj6a9k7Av");

void setup() {
  Serial.begin(9600);
}

void loop() {

  phant.add("val1", "well...");
  phant.add("val2", "that");
  phant.add("val3", "sucks");

  Serial.println("----TEST URL-----");
  Serial.println(phant.url());

  Serial.println();

  phant.add("val1", "sucks");
  phant.add("val2", "to");
  phant.add("val3", "post");
  
  Serial.println("----HTTP POST----");
  Serial.println(phant.post());

  Serial.println();

  Serial.println("----HTTP GET----");
  Serial.println(phant.get());

  Serial.println("----HTTP DELETE----");
  Serial.println(phant.clear());

  delay(2000);

}
