package cmd

type BatteryState int

const ( //my fixed values what will never change
	On       BatteryState = iota // iota makes this state = 0
	Asleep                       // = 1
	Charging                     // = 2
)



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
