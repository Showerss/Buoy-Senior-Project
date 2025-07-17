#ifndef POWER_MANAGER_H
#define POWER_MANAGER_H

#include <stdint.h>

typedef struct PowerManager PowerManager;

//enum for battery states
typedef enum {
    BATTERY_STATE_ON,
    BATTERY_STATE_ASLEEP,
    BATTERY_STATE_CHARGING,
    BATTERY_STATE_UNKNOWN
} BatteryState;


//functions 
void pm_sleep(PowerManager *pm);
void pm_wake(PowerManager *pm);
void pm_manage_charging(PowerManager *pm);
float pm_get_battery_level(PowerManager *pm);

//constructors 
PowerManager *pm_create(void);
void pm_destroy(PowerManager *pm);

//getter
BatteryState pm_get_battery_state(PowerManager *pm);
float pm_get_battery_level(PowerManager *pm);
float pm_get_solar_voltage(PowerManager *pm);

#endif
