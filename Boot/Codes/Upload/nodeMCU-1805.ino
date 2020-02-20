#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Servo.h>

// Multi-colored LED pins
#define R 1
#define G 3
#define B 15

// Servos
Servo S1, S2;
int mapping[4][20] = {
  {3, 11, 18, 26, 34, 42, 49, 57, 65, 73, 81, 89, 97, 106, 114, 122, 131, 138, 146, 154}, 
  {4, 16, 26, 36, 47, 57, 67, 78, 89, 100, 110, 122, 132, 142, 154, 0, 0, 0, 0, 0},
  {6, 22, 36, 52, 67, 84, 102, 120, 137, 154, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {18, 55, 96, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};

int vertical[4] = {62, 55, 45, 32};

// UDP Object
WiFiUDP Udp;

// UDP Variables
unsigned int localUdpPort = 4210;
char incomingPacket[2];
char replyPacket[] = "Done!";

// Array to store computed path from Laptop
char path[130];
unsigned int path_length = 0;

// Raspberry station variables
const char *STAssid = "RPi";
const char *STApassword = "firebird"; 
IPAddress STAlocal_IP(192, 168, 10, 27);
IPAddress STAgateway(192, 168, 10, 1);
IPAddress STAsubnet(255, 255, 255, 0);

/*
 * Functions
 */
// Receive packet
int receive_packet()
{
  while(true)
  {
    int packetSize = Udp.parsePacket();
    if (packetSize)
    {
      // receive incoming UDP packets
      // Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
      int len = Udp.read(incomingPacket, 255);
      if (len > 0)
      {
        incomingPacket[len] = 0;
      }
      break;
    }
  }
  return (int)incomingPacket[0];
}

// Send message
void send_packet(char msg)
{
  Serial.printf("\nSending message: %c\n", msg); 
  Udp.beginPacket(STAgateway, 5005);
  Udp.write(msg);
  Udp.endPacket();
  Serial.println("Sent");
}

void setup()
{
  Serial.begin(9600);
  
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);

  // Turn off LED
  digitalWrite(R, HIGH);
  digitalWrite(G, HIGH);
  digitalWrite(B, HIGH);
  
  // Set WiFi Mode as Access Point
  WiFi.mode(WIFI_AP);

  // Soft Ap variables
  const char *APssid = "NMCU-1805";
  const char *APpassword = "1805pwd";
  IPAddress APlocal_IP(192, 168, 4, 1);
  IPAddress APgateway(192, 168, 4, 1);
  IPAddress APsubnet(255, 255, 255, 0);

  // Configure the Access Point
  Serial.print("Configuring AP ... ");
  Serial.println(WiFi.softAPConfig(APlocal_IP, APgateway, APsubnet) ? "OK" : "Failed!"); // configure network
  Serial.print("Starting AP ... ");
  delay(1);
  Serial.println(WiFi.softAP(APssid, APpassword) ? "OK" : "Failed!"); // Setup the Access Point
  Serial.print("AP IP address = ");
  Serial.println(WiFi.softAPIP()); // Confirm AP IP address

  // Setup the UDP port
  Serial.println("Starting UDP");
  Udp.begin(localUdpPort);
  Serial.print("UDP Port: ");
  Serial.println(localUdpPort );

  // Receive Path
  Serial.println("Waiting for Path ...");
  while(true)
  {
    path_length = Udp.parsePacket();
    if (path_length)
    {
      // receive incoming UDP packets
      Serial.printf("Receiving Path ...", path_length, Udp.remoteIP().toString().c_str(), Udp.remotePort());
      int len = Udp.read(path, 255);
      if (len > 0)
      {
        path[len] = 0;
      }
      Serial.println("Done!");
      break;
    }
  }

  delay(1);
  // Set Wifi mode as Station
  WiFi.mode(WIFI_STA);
  
  // Connect to Raspberry-pi
  Serial.printf("Connecting to Raspberry Pi with SSID: %s", STAssid);
  WiFi.begin(STAssid, STApassword);
  WiFi.config(STAlocal_IP, STAgateway, STAsubnet);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Raspberry connected, IP address: ");
  Serial.println(WiFi.localIP());
  Serial.printf("Signal Strength: %d dBm\n", WiFi.RSSI());

  // Initialize variables for motor movement algorithm
  int prev1 = 'A', prev2 = 'A';
    
  /* Attach Servos to pins
   * GPIO4 = Pin D2
   * GPIO5 = Pin D1
   */
  S1.attach(4);
  S2.attach(5);

  S1.write(0);
  delay(1000);
  S2.write(10);
  delay(1000);
  S2.write(vertical[0]);
  
  // Keep track of direction
  int clockwise = 0;

  Serial.printf("\nPath Length = %d\n", path_length);

  // Send a dummy message
  send_packet('5');
  delay(100);

  // Turn off LED
  digitalWrite(R, LOW);
  digitalWrite(G, LOW);
  digitalWrite(B, LOW);
 
  // Motor code
  for(int i = 0; i < path_length - 1; i = i + 2)
  {
    // Checkpoint check
    if(prev2 == path[i] && prev1 == path[i+1])
    {
      send_packet('1');
      delay(1);
      S2.write(10);
      delay(1000);
      int color = receive_packet();
      
      // Logic to glow LED
      if(color == 'R')
      {
        digitalWrite(R, LOW);
        digitalWrite(G, HIGH);
        digitalWrite(B, HIGH);
      }
      else if(color == 'G')
      {
        digitalWrite(R, HIGH);
        digitalWrite(G, LOW);
        digitalWrite(B, HIGH);
      }
      else if(color == 'B')
      {
        digitalWrite(R, HIGH);
        digitalWrite(G, HIGH);
        digitalWrite(B, LOW);
      }
      else if(color == 'S')
      {
        digitalWrite(R, HIGH);
        digitalWrite(G, LOW);
        digitalWrite(B, LOW);
      }
      else if(color == 'P')
      {
        digitalWrite(R, LOW);
        digitalWrite(G, HIGH);
        digitalWrite(B, LOW);
      }
      else if(color == 'Y')
      {
        digitalWrite(R, LOW);
        digitalWrite(G, LOW);
        digitalWrite(B, HIGH);
      }
      else if(color == 'W')
      {
        digitalWrite(R, LOW);
        digitalWrite(G, LOW);
        digitalWrite(B, LOW);
      }

      delay(3000);
      // Turn off LED
      digitalWrite(R, HIGH);
      digitalWrite(G, HIGH);
      digitalWrite(B, HIGH);
      
      // Tell Pi to turn off LED
      send_packet('5');
      S2.write(vertical[path[i] - 65]);
      delay(1000);
    }
    Serial.printf("\n%c,%c    %c,%c\n", prev2, prev1, path[i], path[i+1]);
    char temp1, temp2;
    
    // Change of circles
    if(prev2 != path[i])
    {
      Serial.println("Change circle");
      S2.write(10);
      delay(1000);
      S2.write(vertical[(int)path[i+2] - 65]);
      delay(1000);

      /*temp1 = prev1;
      temp2 = prev2;
      prev2 = path[i+2];*/
      
      // Turning command after circle changes
      // Running anti - clockwise
      if(prev2 > path[i] && clockwise == 0) // Turn left
      {
        // Make right
        send_packet('2');
        receive_packet();
        if(path[i + 1] < path[i + 3])
        {
          // Make left
          send_packet('3');
          receive_packet();
        }
        else if(path[i + 1] > path[i + 3])
        {
          // Make right
          send_packet('2');
          receive_packet();
          clockwise = 1;
        }
      }
      else if(prev2 < path[i] && clockwise == 0) // Turn right
      {
        // Make left
        send_packet('3');
        receive_packet();

        if(path[i + 1] < path[i + 3])
        {
          // Make right
          send_packet('2');
          receive_packet();
        }
        else if(path[i + 1] > path[i + 3])
        {
          // Make left
          send_packet('3');
          receive_packet();
          clockwise = 1;
        }
      }

      // Running clockwise
      else if(prev2 < path[i] && clockwise == 1) // Turn right
      {
        send_packet('2');
        receive_packet();

        if(path[i + 1] < path[i + 3])
        {
          // Make right
          send_packet('2');
          receive_packet();
          clockwise = 0;
        }
        else if(path[i + 1] > path[i + 3])
        {
          // Make left
          send_packet('3');
          receive_packet();
        }
      }
      else if(prev2 > path[i] && clockwise == 1) // Turn left
      {
        send_packet('3');
        receive_packet();

        if(path[i + 1] < path[i + 3])
        {
          // Make left
          send_packet('3');
          receive_packet();
          clockwise = 0;
        }
        else if(path[i + 1] > path[i + 3])
        {
          // Make right
          send_packet('2');
          receive_packet();
        }
      }
    }
    //Serial.println("Motor Movement");
    if(mapping[prev2 - 65][prev1 - 65] > mapping[path[i] - 65][path[i + 1] - 65])
    {
      if(!clockwise)
      {
        send_packet('6');
      }
      clockwise = 1;
      for(int j = mapping[prev2 - 65][prev1 - 65]; j > mapping[path[i] - 65][path[i + 1] - 65]; j--)
      {
        //Serial.println(j);
        S1.write(j);
        delay(425);  
      }
    }
    else
    {
      if(clockwise)
      {
        send_packet('6');
      }
      clockwise = 0;
      for(int j = mapping[prev2 - 65][prev1 - 65]; j < mapping[path[i] - 65][path[i + 1] - 65]; j++)
      {
        //Serial.println(j);
        S1.write(j);
        delay(425);  
      }
    }
    prev1 = path[i+1];
    prev2 = path[i];
  }
}

void loop()
{
}
