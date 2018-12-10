void setup{

Serial.begin(115200);


}

void loop{

int a = analogRead(A0);
Serial.println(a);

}