void setup(){
	pinMode(0, INPUT);
	pinMode(15, OUTPUT);
	pinMode(16, OUTPUT);
	pinMode(17, OUTPUT);

	Serial.begin(38400);
}
void loop(){
	int val = analogRead(0);
	Serial.print("Analog 0 is: ");
	Serial.println(val);
	delay(10);

	digitalWrite(15, HIGH);
	delay(500);
	digitalWrite(15, LOW);
	delay(500);

	digitalWrite(16, HIGH);
	delay(500);
	digitalWrite(16, LOW);
	delay(500);

	digitalWrite(17, HIGH);
	delay(500);
	digitalWrite(17, LOW);
	delay(500);

}