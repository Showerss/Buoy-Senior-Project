#include "PowerManager.h"

void pm_sleep(PowerManager *pm) {
    pm->battery_state = BATTERY_STATE_ASLEEP;
}

void pm_wake(PowerManager *pm) {
    pm->battery_state = BATTERY_STATE_ON;
}

void pm_manage_charging(PowerManager *pm) {
    if (pm->battery_state == BATTERY_STATE_CHARGING) {
        pm->battery_state = BATTERY_STATE_ON;
    }
}

BatteryState pm_get_battery_state(PowerManager *pm) {
    return pm->battery_state;
}

float pm_get_battery_level(PowerManager *pm) {
    return pm->battery_level;
}

float pm_get_solar_voltage(PowerManager *pm) {
    return pm->solar_voltage;
}

PowerManager *pm_create(void) {
    PowerManager *pm = (PowerManager *)malloc(sizeof(PowerManager));
    pm->battery_state = BATTERY_STATE_UNKNOWN;
    pm->battery_level = 0.0;
    pm->solar_voltage = 0.0;
    return pm;
}

void pm_destroy(PowerManager *pm) {
    free(pm);
}
    