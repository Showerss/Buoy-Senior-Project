#include "../include/PowerManager.h"
#include <stdlib.h>

#ifdef HOST_BUILD
   #include <stdio.h>
#endif

void pm_sleep(PowerManager *pm) {
	#ifdef HOST_BUILD
	    //Practice
		printf("[HOST] pm_sleep: battery_state = ASLEEP\n");
		pm->battery_state = BATTERY_STATE_ASLEEP;
	#else
		//Actual
		pm->battery_state = BATTERY_STATE_ASLEEP;
	#endif
}

void pm_wake(PowerManager *pm) {
	#ifdef HOST_BUILD
		//Practice
		printf("[HOST] pm_wake: battery_state = ON\n");
		pm->battery_state = BATTERY_STATE_ON;
	#else
		//Actual
		pm->battery_state = BATTERY_STATE_ON;
	#endif
}

void pm_manage_charging(PowerManager *pm) {
	#ifdef HOST_BUILD
		//Practice
		printf("[HOST] pm_manage_charging: battery_state = CHARGING\n");
		pm->battery_state = BATTERY_STATE_CHARGING;
	#else
		//Actual
		pm->battery_state = BATTERY_STATE_CHARGING;
	#endif
}

BatteryState pm_get_battery_state(const PowerManager *pm) {
	#ifdef HOST_BUILD
		//Practice
		printf("[HOST] pm_get_battery_state: battery_state = %d\n", pm->battery_state);
		return pm->battery_state;
	#else
		//Actual
		return pm->battery_state;
	#endif
}

float pm_get_battery_level(const PowerManager *pm) {
	#ifdef HOST_BUILD
		//Practice
		printf("[HOST] pm_get_battery_level: battery_level = %f\n", pm->battery_level);
		return pm->battery_level;
	#else
		//Actual
		return pm->battery_level;
	#endif
}

float pm_get_solar_voltage(const PowerManager *pm) {
	#ifdef HOST_BUILD
		//Practice
		printf("[HOST] pm_get_solar_voltage: solar_voltage = %f\n", pm->solar_voltage);
		return pm->solar_voltage;
	#else
		//Actual
		return pm->solar_voltage;
	#endif
}

PowerManager *pm_create(void) {
		PowerManager *pm = malloc(sizeof(PowerManager));
		pm->battery_state = BATTERY_STATE_UNKNOWN;
		pm->battery_level = 0.0f;
		pm->solar_voltage = 0.0f;
	#ifdef HOST_BUILD
		printf("[HOST] pm_create: state= %d, level= %.2f, voltage= %.2f\n", pm->battery_state, pm->battery_level, pm->solar_voltage);
	#endif
	    return pm;
}

void pm_destroy(PowerManager *pm) {
	#ifdef HOST_BUILD
		printf("[HOST] pm_destroy\n");
	#endif 
		free(pm);
}