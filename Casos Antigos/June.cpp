#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include <NimBLEDevice.h>

#include <WiFi.h>
#include <BluetoothSerial.h>
#include "driver/adc.h"
#include <esp_bt.h>

#include <vector>


//Definições para o usuário

int delay_BLE_ligado = 5000;     //Alterar a velocidade em que o BLE permanece ligado
int delay_BLE_desligado = 10000; //Alterar a velocidade em que o BLE permanece desligado
int delay_geracao_Dados = 3;     //Alterar a velocidade com que os dados são gerados pela ESP

const int clockSlower = 10; //10 20 40 80 160 240
const int clockTurbo = 240; //80 160 240
const int clockSuperSlow = 10; //10 20 40 80 160 240

boolean BLEON = false;

//Variáveis Globais

NimBLEServer* pServer = NULL;
NimBLECharacteristic* pCharacteristic = NULL;

boolean Connected = false;
boolean canStart = false;
boolean firstTime = true;

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"


int arquivoEnviar = 0; //int que sinaliza arquivos criados pela ESP
int arquivoEnviado = 0; //int que sinaliza arquivos enviados pela ESP
//naturalmente, os que faltam enviar é a diferença dos dois.

std::string ultimoDiretorio; //String global que contém o nome da pasta (leituraN).
//Em SETUP, a ESP32 lê o cartão SD e identifica qual a última pasta do tipo "leitura" existente, e então adiciona um número na frente.

//Funções de MicroSD Principais



//Funções do BLE

class MyServerCallbacks: public NimBLEServerCallbacks {
    void onConnect(NimBLEServer* pServer) {
           Serial.println("Connected");
     Connected = true;
     
     };

    void onDisconnect(NimBLEServer* pServer, NimBLEConnInfo& connInfo, int reason) {
                  Serial.println("Disconnected");
      firstTime = true;
      Connected = false;
};
};


class MyServerCallbacksFirst: public NimBLEServerCallbacks{
      void onConnect(NimBLEServer* pServer) {
      Serial.println("Connected");
   delay(1000);
     Connected = true;
     
     };

    void onDisconnect(NimBLEServer* pServer) {
            Serial.println("Disconnected");

      Connected = false;
    
    if(!canStart){
      NimBLEDevice::startAdvertising();
    }

};
};

class MyCallbacks: public NimBLECharacteristicCallbacks {
    void onWrite(NimBLECharacteristic *pCharacteristic) {
      std::string value = pCharacteristic->getValue();
if(value.length()<2){
  canStart = true;
  return;
}

  std::string coletadodaCaracteristica = pCharacteristic->getValue(); //braço para ler o valor da característica enviado pelo app

   int valoresColetadosdaSequencia[3];
   int h = 0;
      std::string w = "";
    for (auto x : coletadodaCaracteristica)
    {
        if (x == '-')
        {
            valoresColetadosdaSequencia[h] = atoi(w.c_str());
            w = "";
            h++;
        }
        else {
            w = w + x;
        }
    }
    valoresColetadosdaSequencia[h] = atoi(w.c_str());

    delay_BLE_ligado = valoresColetadosdaSequencia[1]*1000;
    delay_BLE_desligado = valoresColetadosdaSequencia[2]*1000;
    delay_geracao_Dados =  valoresColetadosdaSequencia[0];

     canStart = true;
    }
};

void createFirstNimBLEDevice(){
  // Create the BLE Device
  NimBLEDevice::init("AD8232");
  // Create the BLE Server
  pServer = NimBLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacksFirst());

  // Create the BLE Service
  NimBLEService *pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Characteristic
  pCharacteristic = pService->createCharacteristic(
                      CHARACTERISTIC_UUID,
                      NIMBLE_PROPERTY::WRITE 
                    );                  
  pCharacteristic->setCallbacks(new MyCallbacks());
  // Start the service
  pService->start();
    NimBLEAdvertising* pAdvertising = NimBLEDevice::getAdvertising();
    pAdvertising->addServiceUUID(pService->getUUID());
    pAdvertising->setScanResponse(true);
    pAdvertising->start();

    
  
}

void createNimBLEDevice(){
  
    setCpuFrequencyMhz(clockTurbo);
  // Create the BLE Device
  NimBLEDevice::init("AD8232");
  NimBLEDevice::setMTU(512);

  // Create the BLE Server
  pServer = NimBLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  // Create the BLE Service
  NimBLEService *pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Characteristic
  pCharacteristic = pService->createCharacteristic(CHARACTERISTIC_UUID, NIMBLE_PROPERTY::NOTIFY);                    
                                    
  

  // Start the service
  pService->start();
  
    BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(false);
  /** Note, this could be left out as that is the default value */
  pAdvertising->setMinPreferred(0x0);  // set value to 0x00 to not advertise this parameter
  
  NimBLEDevice::startAdvertising();

}

void destroyNimBLEDevice(){
  
  NimBLEDevice::deinit(true);
  
    setCpuFrequencyMhz(clockSlower); 
    BLEON = false;
  
}

//Funções para Avaliar Existência de Arquivo + Encontrar último arquivo para se criar (removido)



std::vector<int> leiturasESP32; //Vetor global onde é armazenado os dados da ESP.
//em gerarDados dados são colocados nesse vetor.
//em gravarSD esse vetor é clonado e resetado, e a sua cópia é armazenada nos arquivos upload.

//looperI //<- Dado coletado da ESP32.
int looperI = 0;
void gerarDados(void * parameters){ //Task1
  for( ;; ){
looperI++;
leiturasESP32.push_back(looperI);
vTaskDelay(delay_geracao_Dados /portTICK_PERIOD_MS);
  }
}

void gerenciamentoBLE(void * parameters){ //Task3
for( ; ;){
  if(!Connected){
    destroyNimBLEDevice(); //destroy BLE Device
    delay(delay_BLE_desligado);
    createNimBLEDevice(); //Create BLE Device
    
    vTaskDelay(delay_BLE_ligado /portTICK_PERIOD_MS);
  }else{

    vTaskDelay(5 /portTICK_PERIOD_MS); //Esperar até ele se desconectar.
  }
  }
  }
  
//Em gravarSD, dados são armazenados sempre em pacotes de 600 ints.
//Esse valor ser definido sempre em 600 ajuda na função de envio.

void setup(){

Serial.begin(115200);
  setCpuFrequencyMhz(clockTurbo);
  WiFi.setSleep(true);
  analogReadResolution(10);
  
  pinMode(41, INPUT);
  pinMode(40, INPUT);
  
createFirstNimBLEDevice();

while(!canStart){
  delay(1000);
  } //loopar notConnected
  
destroyNimBLEDevice();

xTaskCreate(gerarDados, "Task 1", 2000, NULL, 1, NULL); //Postar TASK 1 - GERAR DADOS

xTaskCreate(gerenciamentoBLE, "Task 3", 8000, NULL, 1, NULL);  //Postar TASK 3 - LIGAR E DESLIGAR BLE

}

void loop(){


if(Connected){
  if(firstTime){
      delay(2000);
      firstTime = false;
    
  }



while(leiturasESP32.size() >= 100){

int arr[100];
std::copy(leiturasESP32.begin(), leiturasESP32.begin()+100, arr);
leiturasESP32.erase(leiturasESP32.begin(), leiturasESP32.begin() +100);

	//Enquanto ainda estiverem arquivos para serem enviados

  if(!Connected){
    ESP.restart();
  }
uint8_t arrayBytes[200];
int i = 0;



int j = 0;
while(i<200){

arrayBytes[i] = (uint8_t)(arr[j] & 0x00FF);
i++;
arrayBytes[i] = (uint8_t)((arr[j] & 0xFF00) >> 8);
i++;

j++;
}



      pCharacteristic->setValue(arrayBytes, 200);
      pCharacteristic->notify();
    delay(10);
	
	
	
	
}







firstTime = true;
Connected = false;

} 
  
}