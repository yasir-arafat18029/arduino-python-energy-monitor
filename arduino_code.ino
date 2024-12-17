// Arduino Code: Energy Monitoring
const int currentPin = A0;  // Pin connected to ACS712 current sensor
float currentValue;         // Variable to hold current sensor reading

void setup() {
  Serial.begin(9600);       // Initialize serial communication
  pinMode(currentPin, INPUT);
}

void loop() {
  // Read analog value from current sensor
  int sensorValue = analogRead(currentPin);
  
  // Convert to current (adjust sensitivity for your ACS712 version)
  currentValue = (sensorValue * 5.0 / 1023.0 - 2.5) / 0.066;  // ACS712-30A version
  
  // Send current value over serial port
  Serial.println(currentValue);
  
  delay(1000);  // Wait for 1 second
}
