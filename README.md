# Solar-Powered IoT Water-Quality Buoy

> A solar-powered, self-sustaining buoy that continuously measures water quality (pH, turbidity, dissolved oxygen, conductivity, temperature) and transmits data via LoRaWAN to your dashboard.

---

## 🌊 Introduction

Water quality monitoring is vital for environmental conservation, research, and public health. Traditional monitoring methods are often labor-intensive and expensive, especially in remote or hard-to-reach locations. This project introduces a **solar-powered IoT buoy** designed to autonomously collect and transmit real-time water quality data. By leveraging renewable energy, robust sensors, and long-range communication (LoRaWAN), our buoy provides a scalable, low-maintenance solution for continuous aquatic monitoring.

Whether you’re a researcher, educator, or community organizer, this open-source project can help you deploy affordable water-quality monitoring stations in lakes, rivers, and reservoirs.

---

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/water-quality-buoy.git
   cd water-quality-buoy
   ```
2. **Firmware Setup (STM32)**
   - Open `/firmware/` in STM32CubeIDE or install `arm-none-eabi` toolchain.
   - Configure `config.h` (sampling interval, calibration).
   - Build & flash via ST‑Link.
3. **Backend Setup (Go)**
   ```bash
   cd backend
   go mod tidy
   go build -o buoy-server
   ./buoy-server --config config.yaml
   ```
4. **GUI Dashboard (Python)**
   ```bash
   cd gui
   pip install -r requirements.txt
   python main.py
   ```
5. **Connect LoRa Gateway**
   - Configure LoRaWAN keys in `backend/config.yaml`
   - Ensure MQTT broker endpoint is reachable.

---

## 📂 Repository Structure

```
/firmware/          # STM32 C firmware (Cube HAL, CMSIS)
/backend/           # Go microservice (Gorilla/Mux, MQTT client)
/gui/               # Python GUI (PyQt5, matplotlib)
/docs/              # Design docs, UML diagrams, BOM
/tests/             # Unit & integration tests
/scripts/           # Build & deployment scripts
README.md           # This landing page
LICENSE             # MIT License
CONTRIBUTING.md     # Contribution guidelines
```

---

## 🌟 Key Features

- **Continuous Monitoring:** Multi-parameter sensing at configurable intervals.
- **Solar-Powered:** 5 W panel + LiFePO₄ battery for months of autonomy.
- **LoRaWAN & NB‑IoT Fallback:** Reliable uplink in remote areas.
- **Modular Design:** Firmware in C, backend in Go, GUI in Python.
- **Outreach-Ready:** Integrate with community dashboards and school projects.

---

## 📖 Documentation & Diagrams

- **Design Document:** `/docs/Design_Document.md`
- **UML Class Diagrams:** `/docs/UML_Diagrams.md`
- **Hardware Schematics & BOM:** `/docs/BOM_and_Schematics.pdf`

---

## 🤝 Contributing

We welcome contributions! Please review [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on setting up your environment, coding standards, and pull-request workflow.

---

## 📄 License

This project is licensed under the MIT License © 2025.

*Happy Monitoring!*

