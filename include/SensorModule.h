#ifndef SENSOR_MODULE_H
#define SENSOR_MODULE_H

#include <stdint.h>

// variables
typedef struct SensorModule {
    float temperature;
    float ph;
    float turbidity;
    float dissolved_oxygen;
    float conductivity;
} SensorModule;

// Function declarations
void measureTemperature(SensorModule *sm);
void measurepH(SensorModule *sm);
void measureTurbidity(SensorModule *sm);
void measureDissolvedOxygen(SensorModule *sm);
void measureConductivity(SensorModule *sm);

#endif

