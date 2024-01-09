

#include <stdint.h>
#include <avr/io.h>
#include <util/delay.h>

//I used P2 of FS1000a. 0 is P0, 1 is P1, 2 is P2, etc.
#define  FS1000A_DATA_PIN    2

void setup() {                
  pinMode(FS1000A_DATA_PIN, OUTPUT);       
}



// sending sequence of pulses which is described by single hexadecimal digit
void sendhexdigit(char c , uint16_t  pulse) 
      {
      switch (c) {
      
      // hex = 0, send 4 low pulses
         case '0':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 4);
         break;

         // hex = 1, send 3 low pulses and 1 high pulse
         case '1':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 3);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = 2, send 2 low pulses,  1 high pulse, 1 low pulse
         case '2':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         break;

         // hex = 3, send 2 low pulses,  2 high pulses
         case '3':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = 4, send 1 low pulses,  1 high pulse, 2 low pulse
         case '4':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 2);
         break;

         // hex = 5, send 1 low pulses,  1 high pulse, 2 low pulse
         case '5':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = 6, send 1 low pulses,  2 high pulse, 1 low pulse
         case '6':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         break;

         // hex = 7, send 1 low pulse,  3 high pulse
         case '7':
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 3);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = 8, send 1 high pulse,  3 low pulses
         case '8':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 3);
         break;

         // hex = 9, send 1 high pulse,  2 low pulses, 1 high pulse
         case '9':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = a, send 1 high pulse,  1 low pulses, 1 high pulse, 1 low pulse
         case 'a':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         break;

         // hex = b, send 1 high pulse,  1 low pulses, 2 high pulses
         case 'b':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = c, send 2 high pulse,  2 low pulses
         case 'c':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 2);
         break;

         // hex = d, send 2 high pulse,  1 low pulses, 1 high pulses
         case 'd':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 2);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 1);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         // hex = e, send 3 high pulses,  1 low pulses
         case 'e':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 3);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         delayMicroseconds(pulse * 1);
         break;

         // hex = f, send 4 high pulses
         case 'f':
         digitalWrite(FS1000A_DATA_PIN, HIGH);
         delayMicroseconds(pulse * 4);
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;

         default:
         digitalWrite(FS1000A_DATA_PIN, LOW);
         break;
         
      };
       
  }





void loop() {

   // After collecting the sequence, I defined it here.
  char sequence1[] = "bbbbb5"; // sequence1 is to define the control signal
  char sequence2[] = "3b5c7e9f0a2b4c6e8f1a3b5c7e9f0a2b4c6e897"; // sequence2 defined the rolling codes.
  uint16_t pulse = 371;
  uint8_t i;

  // first sequence
  for (i = 0; i<sizeof(sequence1);  i++) 
   {  
    sendhexdigit(sequence1[i], pulse);
   }

  // first pause
  delayMicroseconds(3723);

  //second sequence
  for (i = sizeof(sequence2)-1; i >=0; i--) 
   {  
    sendhexdigit(sequence2[i], pulse);
   }
  // second pause 
  delayMicroseconds(15230);

}
