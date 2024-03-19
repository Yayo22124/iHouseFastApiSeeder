from ..data.rooms import rooms_components;
from .fn_generate_rand_int import fn_generate_rand_int as rand_int;
import random

def fn_get_sensor_name(location: str) -> str :
    sensor_name = random.choice(rooms_components[location].get("sensors"));
    print(sensor_name)
    
    return sensor_name;