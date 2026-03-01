#include <Arduino.h>

// ADC1 (evita ADC2 si usas WiFi en el futuro)
static const int PIN_S1 = 34;
static const int PIN_S2 = 35;

static const uint32_t SAMPLE_MS = 100; // 10 Hz (cumple >=2 Hz)
uint32_t last_ms = 0;

void setup() {
  Serial.begin(115200);
  delay(200);

  analogReadResolution(12); // 0..4095
  analogSetPinAttenuation(PIN_S1, ADC_11db); // ~0..3.3V
  analogSetPinAttenuation(PIN_S2, ADC_11db); // ~0..3.3V
}

void loop() {
  uint32_t now = millis();
  if (now - last_ms >= SAMPLE_MS) {
    last_ms = now;
    uint16_t s1 = analogRead(PIN_S1);
    uint16_t s2 = analogRead(PIN_S2);

    // CSV compacto
    Serial.printf("%lu,%u,%u\n", (unsigned long)now, (unsigned)s1, (unsigned)s2);
  }
}