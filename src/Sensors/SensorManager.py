import random

class SensorManager:
    """Manages sensor functionality checks and status monitoring"""
    
    def __init__(self):
        self.sensor_types = ["Temperature", "pH", "Turbidity", "Dissolved Oxygen"]
    
    def check_sensor_functionality(self):
        """
        Comprehensive sensor functionality check
        Returns a dictionary with sensor status: 'functional', 'disabled', 'error', or 'needs_calibration'

        Returns: 
            sensor_status: Dictionary with sensor status: 'functional', 'disabled', 'error', or 'needs_calibration'
        """
        sensor_status = {}
        
        # Temperature sensor check
        temp_status = self._check_temperature_sensor()
        sensor_status["Temperature"] = temp_status
        
        # pH sensor check
        ph_status = self._check_ph_sensor()
        sensor_status["pH"] = ph_status
        
        # Turbidity sensor check
        turbidity_status = self._check_turbidity_sensor()
        sensor_status["Turbidity"] = turbidity_status
        
        # Dissolved Oxygen sensor check
        do_status = self._check_dissolved_oxygen_sensor()
        sensor_status["Dissolved Oxygen"] = do_status
        
        return sensor_status
    
    def _check_temperature_sensor(self):
        """
        Check temperature sensor functionality
        
        Returns: 
            "functional" if the sensor is working correctly
            "disabled" if the sensor is not connected
            "error" if the sensor is not responding
            "needs_calibration" if the sensor needs to be calibrated
        """
        try:
            # Simulate reading temperature sensor
            # In real implementation, you would communicate with the actual sensor
            # temperature_value = self._read_temperature_sensor()
            
            # Simulated conditions for demonstration
            sensor_response = random.choice([True, False, "error", "calibration_needed"])
            
            if sensor_response == True:
                return "functional"
            elif sensor_response == False:
                return "disabled"
            elif sensor_response == "error":
                return "error"
            elif sensor_response == "calibration_needed":
                return "needs_calibration"
            else:
                return "error"
                
        except Exception as e:
            print(f"Temperature sensor error: {e}")
            return "error"
    
    def _check_ph_sensor(self):
        """Check pH sensor functionality"""
        try:
            # Simulate pH sensor check
            sensor_response = random.choice([True, False, "error", "calibration_needed"])
            
            if sensor_response == True:
                return "functional"
            elif sensor_response == False:
                return "disabled"
            elif sensor_response == "error":
                return "error"
            elif sensor_response == "calibration_needed":
                return "needs_calibration"
            else:
                return "error"
                
        except Exception as e:
            print(f"pH sensor error: {e}")
            return "error"
    
    def _check_turbidity_sensor(self):
        """Check turbidity sensor functionality"""
        try:
            # Simulate turbidity sensor check
            sensor_response = random.choice([True, False, "error", "calibration_needed"])
            
            if sensor_response == True:
                return "functional"
            elif sensor_response == False:
                return "disabled"
            elif sensor_response == "error":
                return "error"
            elif sensor_response == "calibration_needed":
                return "needs_calibration"
            else:
                return "error"
                
        except Exception as e:
            print(f"Turbidity sensor error: {e}")
            return "error"
    
    def _check_dissolved_oxygen_sensor(self):
        """Check dissolved oxygen sensor functionality"""
        try:
            # Simulate dissolved oxygen sensor check
            sensor_response = random.choice([True, False, "error", "calibration_needed"])
            
            if sensor_response == True:
                return "functional"
            elif sensor_response == False:
                return "disabled"
            elif sensor_response == "error":
                return "error"
            elif sensor_response == "calibration_needed":
                return "needs_calibration"
            else:
                return "error"
                
        except Exception as e:
            print(f"Dissolved Oxygen sensor error: {e}")
            return "error"
    
    def get_sensor_types(self):
        """Return list of available sensor types"""
        return self.sensor_types.copy()