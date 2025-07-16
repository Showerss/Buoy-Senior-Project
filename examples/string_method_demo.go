package main

import (
	"encoding/json"
	"fmt"
)

// Your BatteryState enum
type BatteryState int

const (
	On BatteryState = iota
	Asleep
	Charging
)

// The magic String() method
func (bs BatteryState) String() string {
	switch bs {
	case On:
		return "On"
	case Asleep:
		return "Asleep"
	case Charging:
		return "Charging"
	default:
		return "Unknown"
	}
}

type PowerManager struct {
	BatteryLevel float32
	SolarVoltage float32
	BatteryState BatteryState
}

func main() {
	// Create a PowerManager instance
	pm := PowerManager{
		BatteryLevel: 85.5,
		SolarVoltage: 12.3,
		BatteryState: Charging,
	}

	// Example 1: Direct printing - String() method is called automatically!
	fmt.Println("Battery state:", pm.BatteryState) // Prints: "Battery state: Charging"

	// Without String() method, this would print: "Battery state: 2"

	// Example 2: String formatting
	fmt.Printf("Power Status: %s at %.1f%% battery\n", pm.BatteryState, pm.BatteryLevel)
	// Prints: "Power Status: Charging at 85.5% battery"

	// Example 3: Logging scenarios
	fmt.Printf("[DEBUG] System transitioning from %s to %s\n", On, Asleep)
	// Prints: "[DEBUG] System transitioning from On to Asleep"

	// Example 4: Comparisons still work with the underlying int values
	if pm.BatteryState == Charging {
		fmt.Println("Battery is currently charging")
	}

	// Example 5: JSON marshaling (bonus!)
	jsonData, _ := json.Marshal(pm)
	fmt.Printf("JSON: %s\n", jsonData)
	// The BatteryState will be serialized as its int value (2), but you can customize this too

	// Example 6: Array/slice of states
	states := []BatteryState{On, Asleep, Charging}
	fmt.Println("All possible states:", states)
	// Prints: "All possible states: [On Asleep Charging]"

	// Example 7: Switch statements work perfectly
	switch pm.BatteryState {
	case On:
		fmt.Println("System is active")
	case Asleep:
		fmt.Println("System is in sleep mode")
	case Charging:
		fmt.Println("System is charging - limited functionality")
	}
}
