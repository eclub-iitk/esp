#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "13:6";
const char* password = "123456789";
const char* udpAddress = "";

const int udpPort = 3333;
String buff;

WiFiUDP udp;
void setup(){

Serial.begin(115200);
Serial.println();
Serial.printf("Connecting to %s ", ssid);

WiFi.begin(ssid, password);
while (WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print(".");
}
Serial.println(" connected"); 
Serial.printf("Web server started, open %s in a web browser\n", WiFi.localIP().toString().c_str());
}

void loop(){
if(Serial.available()){
buff = Serial.readStringUntil('\n'); 
char charBuf[buff.length() + 1]; 
buff.toCharArray(charBuf, buff.length() + 1); 
udp.beginPacket(udpAddress,udpPort); 
udp.printf("%s",charBuf); 
udp.endPacket();
}
}
