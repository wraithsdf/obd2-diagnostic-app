import obd
from typing import Optional, List
import time

class OBDReader:
    def __init__(self, port: str = "COM3"):
        self.connection = None
        self.port = port
        self.supported_commands = []
    
    def connect(self) -> bool:
        try:
            print(f"Connecting to OBD on port {self.port}...")
            self.connection = obd.OBD(self.port)
            if self.connection.is_connected():
                self.supported_commands = self.connection.supported_commands
                print("Connected successfully!")
                return True
            return False
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def get_rpm(self) -> Optional[int]:
        if not self.connection:
            return None
        response = self.connection.query(obd.commands.RPM)
        return int(response.value.magnitude) if not response.is_null() else None
    
    def get_speed(self) -> Optional[float]:
        if not self.connection:
            return None
        response = self.connection.query(obd.commands.SPEED)
        return float(response.value.magnitude) if not response.is_null() else None
    
    def get_coolant_temp(self) -> Optional[float]:
        if not self.connection:
            return None
        response = self.connection.query(obd.commands.COOLANT_TEMP)
        return float(response.value.magnitude) if not response.is_null() else None
    
    def get_dtc_codes(self) -> List[str]:
        if not self.connection:
            return []
        response = self.connection.query(obd.commands.GET_DTC)
        if not response.is_null():
            return [f"{code[0]}: {code[1]}" for code in response.value]
        return []
    
    def clear_dtc(self) -> bool:
        if not self.connection:
            return False
        try:
            response = self.connection.query(obd.commands.CLEAR_DTC)
            return not response.is_null()
        except:
            return False
    
    def get_load(self) -> Optional[float]:
        if not self.connection:
            return None
        response = self.connection.query(obd.commands.ENGINE_LOAD)
        return float(response.value.magnitude) if not response.is_null() else None
    
    def get_fuel_status(self) -> Optional[str]:
        if not self.connection:
            return None
        response = self.connection.query(obd.commands.FUEL_STATUS)
        return str(response.value) if not response.is_null() else None
        return None

    def get_engine_temperature(self):
        response = self.connection.query(obd.commands.COOLANT_TEMP)
        if response.value is not None:
            return response.value.magnitude
        return None

    def get_dtc(self):
        response = self.connection.query(obd.commands.GET_DTC)
        if response.value is not None:
            return response.value
        return None

    def close_connection(self):
        self.connection.close()