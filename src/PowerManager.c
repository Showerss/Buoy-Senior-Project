package cmd

type BatteryState int

const ( //my fixed values what will never change
	On       BatteryState = iota // iota makes this state = 0
	Asleep                       // = 1
	Charging                     // = 2
)

type PowerManager struct { // my actual values that can change
	// Public variables (capitalized for export)
	BatteryLevel float32
	SolarVoltage float32
	BatteryState BatteryState //this is a custom type so i can use String or other methods such as int
}

// String method for better debugging and logging
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
