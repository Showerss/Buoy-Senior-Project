#ifndef SENSOR_MODULE_H
#define SENSOR_MODULE_H

#include <stdint.h>

/**
* @file SensorModule.h
* @brief Pure interface for sensor operations
* 
* This module handles all sensor-related operations including:
* - Temperature measurement
* - pH measurement
* - Turbidity measurement
* - Dissolved oxygen measurement
* - Conductivity measurement
*/

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

