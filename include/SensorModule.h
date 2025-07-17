//SensorModule.h

#ifndef SENSOR_MODULE_H
#define SENSOR_MODULE_H


#include <stdint.h> //for uint32_t

//Struct for sensor data
typedef struct {
	float Temperature;
	float pH;
	float Turbidity;
	float DissolvedOxygen;
	float Conductivity;
	uint32_t Timestamp;
} SensorModule;

//function prototypes
void measureTemperature(SensorModule *sm);
void measurepH(SensorModule *sm);
void measureTurbidity(SensorModule *sm);
void measureDissolvedOxygen(SensorModule *sm);
void measureConductivity(SensorModule *sm);

#endif

