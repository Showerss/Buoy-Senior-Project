#ifndef POWER_MANAGER_H
#define POWER_MANAGER_H

#include <stdint.h>
#include <stdbool.h>

/**
 * @file PowerManager.h
 * @brief Pure interface for power management operations
 * 
 * This module handles all power-related operations including:
 * - Battery state management (ON, ASLEEP, CHARGING, UNKNOWN)
 * - Battery level monitoring (0.0 to 1.0)
 * - Solar voltage monitoring
 * - Sleep/wake cycle management
 * - Charging state management
 * 
 */

//enum for battery states
typedef enum {
    BATTERY_STATE_ON,
    BATTERY_STATE_ASLEEP,
    BATTERY_STATE_CHARGING,
    BATTERY_STATE_UNKNOWN
} BatteryState;


// variables
typedef struct {
    BatteryState battery_state;
    float battery_level;
    float solar_voltage;
} PowerManager;

// Actions:
void pm_sleep(PowerManager *pm);
void pm_wake(PowerManager *pm);
void pm_manage_charging(PowerManager *pm);

// State-query
BatteryState pm_get_battery_state(const PowerManager *pm);
float pm_get_battery_level(const PowerManager *pm);
float pm_get_solar_voltage(const PowerManager *pm);

// Life-Cycle 
PowerManager *pm_create(void);
void pm_destroy(PowerManager *pm);

#endif //POWER_MANAGER_H
