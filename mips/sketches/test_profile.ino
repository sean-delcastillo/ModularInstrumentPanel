// THIS SKETCH HAS BEEN GENERATED BY ModularInstrumentPanel
//      https://github.com/sean-delcastillo/ModularInstrumentPanel
// 18/01/2023 16:47:45

#include <Metro.h>
#include <Bounce.h>

int pot_01 = 0;
int red_led = 15;
int green_led = 16;
int blue_led = 17;

Metro serialMetro = Metro(250);
Metro delayMetro = Metro(200);

void setup() {
    pinMode(0, INPUT);
    pinMode(15, OUTPUT);
    pinMode(16, OUTPUT);
    pinMode(17, OUTPUT);

    Serial.begin(38400);
}

void loop() {
    if (serialMetro.check() == 1) {
        Serial.print("[Potentionmeter] pot_01 on pin 0 is: ");
        Serial.println(analogRead(pot_01));
    }


    if (delayMetro.check() == 1) {
        digitalToggle(red_led);
    }


    if (delayMetro.check() == 1) {
        digitalToggle(green_led);
    }


    if (delayMetro.check() == 1) {
        digitalToggle(blue_led);
    }

}