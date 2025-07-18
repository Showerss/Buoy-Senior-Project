## 1. Ensure file only keeps one concept. 
    sensor_module.c/.h only knows how to read and calibrate sensors.
    power_manager.c/.h only knows how to manage sleep/wake and battery/solar.
    comm_module.c/.h only knows how to package, encrypt, and send data.
    firmware_main.c orchestrates high-level cycles, but delegates every job to those modules.

    please do this to reduce coupling and make the files easy to maintain, read and replace

## 2. Interface segregation
    do "Pure" interfaces in headers
    never do #include if possible to keep with abstract interface styling, dont do many concerte .c files 

## 3. Open-Closed Strategies
    create seperate .c files for each protocol ( such as using iot_comm.c but all interfacing comminterface)
    so for if we do a new sensor, just implement a new sensorinterface in its own file

## 4. Documentation and commenting
    document each modules contract in the header to demonstrate i know the value of clear API docs as a professional

## 5. real time and state patterns
    make sure i have good state machine switching between sleep, active, charging, scanning, etc 

## 6. encapsulation 
    keep static variables within .c files when possible,
    expose only whats necessary via extern in my headers