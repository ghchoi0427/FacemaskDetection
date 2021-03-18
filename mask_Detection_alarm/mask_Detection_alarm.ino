#define motion 8
#define MaskOff 5
#define MaskOn 6
#define alertLED 11
#define chillLED 12
#define buzzer 3

void setup() {
 
  pinMode(motion, INPUT);
  pinMode(MaskOff, INPUT);
  pinMode(alertLED,OUTPUT);
  pinMode(chillLED,OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
  
}

void loop() {
  
  int PIRState = digitalRead(motion);
  int isMaskOff = digitalRead(MaskOff);
  int isMaskOn = digitalRead(MaskOn);

  
    if(isMaskOff&&PIRState){
      
        alert();    
      }
    else if(isMaskOn){
    normal();
  
  }
    
  else blank();

}

void alert(){
  digitalWrite(alertLED,HIGH);
  for(int i = 0; i<2;i++){
    for(int j=600;j<1200;j++){
    tone(buzzer,j);
    delay(1);  
    }
    
    
    for(int j=1200;j>600;j--){
    tone(buzzer,j);
    delay(1);  
    }
    
  }
  digitalWrite(alertLED,LOW);
}


void normal(){
  noTone(buzzer);

  digitalWrite(alertLED,LOW);
  digitalWrite(chillLED,HIGH);
}

void blank(){
  noTone(buzzer);
  
 digitalWrite(alertLED,LOW);
  digitalWrite(chillLED,LOW);
}
