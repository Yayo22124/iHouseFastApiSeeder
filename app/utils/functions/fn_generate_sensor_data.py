import random
import datetime as dt

from app.utils.functions.fn_random_ip import fn_random_ip
from .fn_random_owner import fn_random_owner
from .fn_component_random_status import fn_component_random_status 
from .fn_generate_rand_decimal import fn_generate_rand_decimal as randDecimal
from .fn_generate_rand_int import fn_generate_rand_int as randInt
from ..data.sensors import sensors

def fn_generate_sensor_data(location: str, sensor_name: str, num_datas: int = 1) -> list:
    sensor = sensors.get(sensor_name)
    
    if not sensor:
        return [{"msg": f"{sensor_name} not found in sensors list."}]

    data_list = []
    for _ in range(num_datas):
        if sensor_name == "Temperatura":
            readings = [
                {"name": "Detección de Temperatura", "value": randDecimal(0, 50, 2), "measurementUnit": "˚C"},
                {"name": "Detección de Humedad", "value": randInt(0, 90), "measurementUnit": "%"}
            ]
        elif sensor_name == "Fotorresistencia":
            readings = [{"name": "Detección de Iluminación", "value": randInt(0, 1024)}]
        elif sensor_name == "Gas":
            readings = [{"name": "Detección de Gas", "value": randInt(10, 300), "measurementUnit": "ppm"}]
        elif sensor_name == "Presencia":
            readings = [{"name": "Detección de Presencia", "value": randInt(0, 1)}]
        elif sensor_name == "Proximidad":
            readings = [{"name": "Detección de Proximidad", "value": randInt(2, 400), "measurementUnit": "cm"}]
        else:
            readings = []

        sensor_data = {
            "arduinoIp": fn_random_ip(),
            "type": sensor["type"],
            "name": sensor["name"],
            "brand": sensor["brand"],
            "model": sensor["model"],
            "specifications": sensor["specifications"],
            "location": location,
            "status": fn_component_random_status(),
            "owner": fn_random_owner(),
            "readings": readings,
        }

        data_list.append(sensor_data)

    return data_list
