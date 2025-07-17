**Project Title**: Solar-Powered IoT Water-Quality Buoy

---

## 1. Introduction

A floating, self-powered station that periodically measures key water-quality parameters (pH, turbidity, dissolved oxygen, conductivity, temperature) and transmits data wirelessly to an online dashboard. Designed for long‐term deployment in ponds, lakes, or slow-moving rivers.

## 2. Objectives

- **Continuous Monitoring**: Capture multi-parameter water quality at configurable intervals.
- **Low-Power Operation**: Use solar energy and efficient power management for autonomous operation ≥ 6 months.
- **Long-Range Communication**: Transmit data via LoRaWAN (or NB‑IoT) to gateways up to several kilometers away.
- **Outreach & Education**: Provide real-time data visualization for community and school engagement.

## 3. System Overview

1. **Sensors**: pH probe, optical turbidity sensor, optical dissolved-oxygen (DO) sensor, conductivity probe, DS18B20 temperature sensor.
2. **Controller**: STM32L4 microcontroller running **C firmware** with STM32Cube HAL.
3. **Power**: 5 W solar panel charging a 6 Ah LiFePO₄ battery through an MPPT charge controller.
4. **Comms**: LoRaWAN radio module (e.g., RFM95) via SPI; fallback NB‑IoT modem (SIM800C).
5. **Enclosure**: IP67-rated waterproof housing with buoyant float and tether.

## 4. Hardware Components

| Component               | Model/Spec                 | Qty | Est. Cost |
| ----------------------- | -------------------------- | --- | --------- |
| Microcontroller         | STM32L476RG (Cortex‑M4)    | 1   | \$15      |
| pH Probe                | Analog 0–14 pH probe       | 1   | \$80      |
| Turbidity Sensor        | Optical 0–1000 NTU         | 1   | \$50      |
| Dissolved Oxygen Sensor | Optical DO (0–20 mg/L)     | 1   | \$120     |
| Conductivity Probe      | 0–2000 µS/cm               | 1   | \$40      |
| Temperature Sensor      | DS18B20 waterproof module  | 1   | \$5       |
| LoRaWAN Module          | RFM95W (915 MHz)           | 1   | \$12      |
| LiFePO₄ Battery         | 6 Ah, 12.8 V               | 1   | \$40      |
| Solar Panel             | 5 W, 12 V                  | 1   | \$20      |
| MPPT Charge Controller  | 1 A @ 12 V LiFePO₄ support | 1   | \$15      |
| Waterproof Enclosure    | IP67 ABS plastic           | 1   | \$25      |
| Floats & Hardware       | PVC, stainless fasteners   | 1   | \$15      |
| **Total (est.)**        |                            |     | **\$437** |

## 5. Software Architecture

1. **Firmware (STM32)**
   - Written in **C** using STM32Cube HAL and CMSIS.
   - Sensor drivers (I²C/SPI/ADC), calibration routines, and power state logic.
   - LoRaWAN communication via MCCI LoRaMAC library.
2. **Backend & Server**
   - **Go microservice** (e.g., Gorilla/Mux) for REST API and MQTT ingestion.
   - MQTT broker (Eclipse Mosquitto) routes packets from LoRa gateway.
   - Persists data to InfluxDB time-series database.
3. **GUI Dashboard**
   - **Python** desktop application (PyQt5) for real-time plots (matplotlib) and alerts.
   - SQLite local cache for offline operation.

## 6. Power Management

- **Harvesting**: Solar panel → MPPT → LiFePO₄ battery.
- **Budget**: MCU sleep ∼5 µA; per-sensor read ∼80 mA for 2 s; LoRa transmit ∼120 mA for 2 s.
- **Estimation**: ∼10 mAh per cycle; hourly → ∼240 mAh/day; battery + solar for months.

## 7. Communication Strategy

- **Primary**: LoRaWAN (915 MHz) uplinks every 15 min.
- **Fallback**: NB‑IoT/2G (SIM800C) on comm failure.
- **Security**: AES‑128 (LoRaWAN) and HTTPS/TLS for backend.

## 8. Mechanical & Enclosure Design

- **Buoyancy**: Dual-part closed-cell foam housing electronics.
- **Mounting**: Tether line allows vertical float motion.
- **Sensor Probes**: 3D-printed arm with cable glands and spring-loaded depth control.

## 9. Data Management & Dashboard

- **Time-Series DB**: InfluxDB for high-frequency data.
- **Visualization**: Optional React dashboard; primary Python GUI.
- **Alerts**: Threshold-based notifications via Twilio/email.

## 10. Development Plan & Timeline

| Phase                 | Duration | Deliverables                                |
| --------------------- | -------- | ------------------------------------------- |
| Requirements & Design | 3 weeks  | Final design doc, BOM                       |
| Hardware Prototype    | 6 weeks  | PCB, enclosure, sensor basics               |
| Firmware Development  | 4 weeks  | C drivers, power mgmt, LoRa comms           |
| Backend & Dashboard   | 4 weeks  | Go service, InfluxDB schema, Python GUI MVP |
| Integration & Testing | 3 weeks  | Field calibration, endurance tests          |
| Outreach Prep         | 2 weeks  | Guides, demos, community materials          |

## 11. Testing & Validation

- **Lab calibration** against known standards.
- **Field trials**: ≥ 30 days deployment.
- **Environmental tests**: thermal cycling, waterproof soak.

## 12. Outreach & Community Engagement

- Partner with local schools/watershed councils.
- Host live data demos and hands-on workshops.
- Distribute monthly water-quality reports.

## 13. Budget & Resources

- **Hardware**: ≈\$450/unit (recommend 2 units).
- **Hosting**: \$10–\$20/month.
- **Total**: ≈\$920 for 2 units + 6 months hosting.

## 14. Risks & Mitigation

| Risk                          | Impact          | Mitigation                    |
| ----------------------------- | --------------- | ----------------------------- |
| Sensor drift/calibration loss | Data inaccuracy | Scheduled recalibration       |
| Winter power shortfall        | Downtime        | Adjust panel size or interval |
| Comms failure (no gateway)    | Data gaps       | NB‑IoT fallback               |

## 15. C Module Interactions (UML)
classDiagram
    class sensor_module_h {
        +latestTemperature : float {extern}
        +latestPH : float {extern}
        +latestTurbidity : float {extern}
        +latestDissolvedO2 : float {extern}
        +latestConductivity : float {extern}
        +measure_temperature() : float
        +measure_ph() : float
        +measure_turbidity() : float
        +measure_do() : float
        +measure_conductivity() : float
    }

    class power_manager_h {
        +batteryLevel : float {extern}
        +solarVoltage : float {extern}
        +isCharging : bool {extern}
        +powerState : PowerState {extern}
        +pm_sleep() : void
        +pm_wake() : void
        +pm_manage_charging() : void
        +pm_get_battery_level() : float
    }

    class comm_module_h {
        +lastCommStatus : bool {extern}
        -encryptionKey : char* {static}
        -lastAttemptTime : uint32_t {static}
        +comm_send_data(packet : DataPacket*) : bool
        +comm_encrypt(packet : DataPacket*) : DataPacket
        +comm_fallback_send(packet : DataPacket*) : bool
    }

    class firmware_main_c {
        -cycleIntervalSec : uint32_t {static}
        -dataBuffer : DataPacket[BUFFER_SIZE] {static}
        +main() : int
        +run_cycle() : void
        +calibrate_sensors() : void
        +power_state_machine() : void
        +enqueue_data() : void
    }

    sensor_module_h --> firmware_main_c : calls
    power_manager_h --> firmware_main_c : calls
    comm_module_h --> firmware_main_c : uses
    firmware_main_c --> gateway_server : "LoRaWAN uplink"
    gateway_server --> dashboard_py : "API feed"

*End of Design Document.*

