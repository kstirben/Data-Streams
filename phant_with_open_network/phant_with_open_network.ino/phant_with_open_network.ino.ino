#include <SPI.h>
#include <WiFi.h>

#include <Phant.h>

// Arduino example stream
// http://data.sparkfun.com/streams/JxKL26QavvIEnompV5vl
// hostname, public key, private key
Phant phant("data.sparkfun.com", "JxKL26QavvIEnompV5vl", "gzNJAw10GGUrj6a9k7Av");

char ssid[] = "disstirbens";     // the name of your network
char pass[] = "Justme42";        // your network password
int status = WL_IDLE_STATUS;     // the Wifi radio's status

byte mac[6];                     // the MAC address of your Wifi shield

WiFiServer server(80);

void setup() {
  // initialize serial:
  Serial.begin(9600);

  // attempt to connect to an open network:
  Serial.println("Attempting to connect to open network...");
  status = WiFi.begin(ssid,pass);

  // if you're not connected, stop here:
  if ( status != WL_CONNECTED) {
    Serial.println("Couldn't get a wifi connection");
    while(true);
  }
  // if you are connected :
  else {
      Serial.println("Connected to the network");
      WiFi.macAddress(mac);
      Serial.println("Your MAC address is ");
      Serial.print("MAC: ");
      Serial.print(mac[5],HEX);
      Serial.print(":");
      Serial.print(mac[4],HEX);
      Serial.print(":");
      Serial.print(mac[3],HEX);
      Serial.print(":");
      Serial.print(mac[2],HEX);
      Serial.print(":");
      Serial.print(mac[1],HEX);
      Serial.print(":");
      Serial.println(mac[0],HEX);
  }
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
