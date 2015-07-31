#include <SPI.h>
#include <WiFi.h>

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
  // do nothing
}
