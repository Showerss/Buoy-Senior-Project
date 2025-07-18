
class Config:
    APP_TITLE = "Water Quality Buoy Control"
    WINDOW_SIZE = "800x600"
    SENSORS = ["Temperature", "pH", "Turbidity", "Dissolved Oxygen"]
    LOG_LEVEL = "INFO"

# Missing: Data storage and retrieval
class DataManager:
    def save_sensor_data(self, data)
    def load_historical_data(self)
    def export_data(self, format)