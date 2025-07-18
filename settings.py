class Config:
    WINDOW_SIZE = "800x600"
    SENSOR_CHECK_INTERVAL = 1000
    LOG_LEVEL = "INFO"

# Missing: Data storage and retrieval
class DataManager:
    def save_sensor_data(self, data)
    def load_historical_data(self)
    def export_data(self, format)