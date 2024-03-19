# Generar una función que nos devuelva el total de sensores o actuadores en una habitación (Recámaras, Baños, Sala, Cocina y Garajes).
from ..models.rooms import rooms, roomsData

def fn_count_components(location: str, component: str) -> dict:
    total_components = 0

    for key in roomsData:
        room_data_list = roomsData[key]

        for room in room_data_list:
            if "location" in room and "type" in room:
                room_location = room["location"]
                room_type = room["type"]

                if room_location == location and room_type == component:
                    total_components += 1

    return {"result": f"{location} tiene {total_components} {component}es"}