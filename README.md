# Solar-Powered IoT Water-Quality Buoy

![Project Banner](docs/banner.png)

Welcome to the **Solar-Powered IoT Water-Quality Buoy** project! This repository contains firmware, backend services, and a Python-based GUI dashboard for a self-sustaining buoy that measures and reports water-quality parameters in real time.

## 🔍 Overview

A floating station that:

* Monitors pH, turbidity, dissolved oxygen (DO), conductivity, and temperature
* Runs off a solar-powered LiFePO₄ battery system for multi-month deployments
* Communicates readings via LoRaWAN (with NB-IoT fallback)
* Stores data in an InfluxDB time-series database
* Provides a desktop GUI (PyQt5) for visualization and alerts

## 🚀 Features

* **Embedded Firmware** in C for STM32L4: low-power cycles, sensor calibration, LoRaWAN uplinks
* **Backend Microservice** in Go: high-performance REST API, MQTT ingestion, data validation
* **Python GUI Dashboard**: real-time plots (matplotlib), threshold alerts, offline caching (SQLite)
* **Modular Design**: clear separation of SensorModule, PowerManager, CommModule, and Firmware
* **UML & Documentation**: design doc, class diagrams, Go struct/interface examples

## 📂 Repository Structure

```
/firmware/          # STM32 C code and drivers
/backend/           # Go microservice and API code
/gui/               # Python GUI (PyQt5) application
/docs/              # Design documents, UML diagrams, schematics
/tests/             # Unit & integration tests for each module
/scripts/           # Build, deploy, and calibration scripts
README.md           # This welcome page
LICENSE             # MIT License
```

## 🛠️ Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/water-quality-buoy.git
   cd water-quality-buoy
   ```
2. **Set up your environment**

   * Firmware: install STM32CubeIDE or toolchain (arm-none-eabi)
   * Backend: Go 1.20+, `go mod tidy`
   * GUI: Python 3.8+, `pip install -r gui/requirements.txt`
3. **Build & Deploy**

   * Firmware: open `/firmware/Project.uvprojx`, build, and flash via ST-Link
   * Backend:

     ```bash
     cd backend
     go build -o buoy-server
     ./buoy-server --config config.yaml
     ```
   * GUI:

     ```bash
     cd gui
     python main.py
     ```
4. **Connect LoRa Gateway & DB**
   Configure your LoRaWAN keys in `backend/config.yaml` and point to your InfluxDB instance.

## 🔧 Configuration

* **Firmware**: edit `firmware/config.h` for reading intervals and calibration values
* **Backend**: `backend/config.yaml` holds MQTT broker URL, database connection, API port
* **GUI**: `gui/settings.ini` for API endpoint and alert thresholds

## 🖼️ Screenshots

![Dashboard Screenshot](docs/screenshots/dashboard.png)

## 🤝 Contributing

We welcome PRs! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/x`)
3. Commit changes with clear messages
4. Open a PR against `main`

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

*Happy monitoring!*
