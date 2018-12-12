# Sending sensor data to UDP Server.
#### Step 1 >> Upload a Bare Minimum Code for your Board.  
Choose your board that you will be using to program your ESP. e.g Arduino Nano.
#### Step 2 >> Download ESP8266 library & Board and add to the Arduino IDE.  
#### Step 3 >> Select Board as Generic ESP8266 and Upload the esp.ino file to the ESP
#### Connections  
 Tx - Tx  
 Rx - Rx  
 VCC- 5V  
 GND - 0V   
 GPIO0 -0V  
 CH_PD - 5V    
 Arduino Reset- Arduino GND 

 #### Step 4 >> Upload the esp.ino code.

 #### Step 5 >> Disconnect your Arduino Board, Make the Connection (Don't power now)

 #### Connections 
 Tx - Rx  
 Rx - Tx  
 VCC- 5V  
 GND - 0V   
 GPIO0 -open  
 CH_PD - 5V    
 Remove Arduino Reset from Ground.

 #### Step 6 >> Start Sending Data to Serial Monitor of the Arduino using sensor.ino file

 As we are using MPU6050, we need some extra libraries. Copy I2Cdev and MPU6050 to your libraies folder in Arduino.  
 Make connections according to conn.png  
 Open MPU6050_DMP6 example from MPU6050 Library.   
 Make this file ready to output YPR data. Remove waiting condition and extra strings.   
 Typical Output Format >> pitch_tab_roll   


