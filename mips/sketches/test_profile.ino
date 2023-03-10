// THIS SKETCH HAS BEEN GENERATED BY ModularInstrumentPanel
//      https://github.com/sean-delcastillo/ModularInstrumentPanel
// 20/01/2023 19:44:18

#include <stdlib.h>

#include <Metro.h>
#include <Bounce.h>

int pot_01 = 0;
int red_led = 15;
int green_led = 16;
int blue_led = 17;
int but_01 = 18;


Metro serialMetro = Metro(250);
Metro delayMetro = Metro(200);

byte previousState = HIGH;

int pot_01_last_read = 0;
Bounce button_but_01 = Bounce(but_01, 10);

void setup() {
    pinMode(pot_01, INPUT);
    pinMode(red_led, OUTPUT);
    pinMode(green_led, OUTPUT);
    pinMode(blue_led, OUTPUT);
    pinMode(but_01, INPUT_PULLUP);

    Serial.begin(38400);
}

void loop() {
    if (serialMetro.check() == 1) {
        int pot_01_current_read = analogRead(pot_01);
        if (abs(pot_01_last_read - pot_01_current_read) >= 3) {
            Serial.print("[Potentionmeter] pot_01 on pin 0 is: ");
            Serial.println(pot_01_current_read);
            pot_01_last_read = pot_01_current_read;
        }
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

    if (button_but_01.update()) {
        if (button_but_01.fallingEdge()) {
            Serial.println("[Button] but_01 on pin 18 pressed");
        }
    }


}