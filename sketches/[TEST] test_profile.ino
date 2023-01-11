void setup(){
	pinMode(0, INPUT);
	pinMode(15, OUTPUT);

	Serial.begin(38400);
}
void loop(){
	int val = analogRead(0);
	Serial.print("Analog 0 is: ");
	Serial.println(val);
	delay(250);

	digitalWrite(15, HIGH);
	delay(500);
	digitalWrite(15, LOW);
	delay(500);

}