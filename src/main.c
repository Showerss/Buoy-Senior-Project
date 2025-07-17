package cmd

import (
    "fmt"
    "os/exec"
    "log"
)

func main() {
    fmt.Println("Buoy Project")
    
    // Run Python script
    cmd := exec.Command("python", "cmd/MainScreen.py")
    
    // Capture output
    output, err := cmd.CombinedOutput()
    if err != nil {
        log.Printf("Error running Python script: %v", err)
    }
    
    fmt.Printf("Python script output: %s", output)
}