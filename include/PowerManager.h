#ifndef POWER_MANAGER_H
#define POWER_MANAGER_H

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
typedef struct PowerManager {
    BatteryState battery_state;
    float battery_level;
    float solar_voltage;
} PowerManager;

// non getter functions 
void pm_sleep(PowerManager *pm);
void pm_wake(PowerManager *pm);
void pm_manage_charging(PowerManager *pm);

// getters and setters 
BatteryState pm_get_battery_state(PowerManager *pm);
float pm_get_battery_level(PowerManager *pm);

// constructor and destructor
PowerManager *pm_create(void);
void pm_destroy(PowerManager *pm);

#endif 
