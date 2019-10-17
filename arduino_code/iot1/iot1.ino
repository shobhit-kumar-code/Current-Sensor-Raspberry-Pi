const int analogIn = A1;
int mVperAmp = 185; //use 100 for 20A Module and 66 for 30A Module
int RawValue= 0;
int ACSoffset = 2500; 
double Voltage = 0;
double Amps = 0;

void setup(){ 
 Serial.begin(9600);
}

void loop(){
 
 RawValue = analogRead(analogIn);
 Voltage = (RawValue / 1024.0) * 5000; //mV
 Amps = ((Voltage - ACSoffset) / mVperAmp);
 Serial.println(Amps,5);
 delay(2500); 
 
}
