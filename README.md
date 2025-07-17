Solar-Powered IoT Water-Quality Buoy


Welcome to the Solar-Powered IoT Water-Quality Buoy project! This repository contains embedded C firmware for STM32, a Python-based GUI dashboard, and configuration/scripts for deploying a self-sustaining buoy that monitors and reports water quality in real time.

🔍 Overview
A floating station that:

Monitors pH, turbidity, dissolved oxygen (DO), conductivity, and temperature

Runs on a solar-powered LiFePO₄ battery for multi-month deployments

Communicates sensor data via LoRaWAN (with NB-IoT fallback)

Stores data in a time-series database

Provides a desktop GUI (Tkinter-based) for visualization and alerts

🚀 Features
Embedded Firmware in C for STM32L4: sensor polling, calibration, power cycling, LoRa uplinks

Python GUI Dashboard: real-time data plots (matplotlib), sensor health indicators, alert system with offline caching (SQLite)

Modular Architecture: clear separation of SensorModule, PowerManager, CommModule, and main loop

Extensive Documentation: design diagrams, architecture breakdowns, and UML specs

📂 Repository Structure
bash
Copy
Edit
/firmware/          # STM32 C code and peripheral drivers
/gui/               # Python GUI (Tkinter) application
/docs/              # Design documents, UML diagrams, schematics
/tests/             # Unit & integration tests for C modules
/scripts/           # Build and deployment scripts for firmware
README.md           # This welcome page
LICENSE             # MIT License
🛠️ Getting Started
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/water-quality-buoy.git
cd water-quality-buoy
Set up your environment

Firmware: install STM32CubeIDE or the arm-none-eabi toolchain

GUI: Python 3.8+ with Tkinter, pip install -r gui/requirements.txt

Build & Deploy

Firmware:

Open the STM32Cube project in /firmware/

Build and flash via ST-Link to STM32L4 MCU

GUI:

bash
Copy
Edit
cd gui
python main.py
Connect LoRa Gateway & Database
Configure LoRa keys in firmware/config.h and ensure your database backend (e.g., InfluxDB) is reachable for downstream ingestion.

🔧 Configuration
Firmware: firmware/config.h – set read intervals, thresholds, and sensor calibration constants

GUI: gui/settings.ini – define API endpoint, alert thresholds, and local cache preferences

🖼️ Screenshots


🤝 Contributing
We welcome pull requests! To contribute:

Fork the repo

Create a new branch (git checkout -b feature/x)

Commit changes with clear messages

Submit a pull request targeting the main branch

More info in CONTRIBUTING.md

📄 License
This project is licensed under the MIT License.
