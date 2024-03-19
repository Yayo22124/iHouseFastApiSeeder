from app.utils.functions.fn_random_ip import fn_random_ip
from app.utils.functions.fn_random_owner import fn_random_owner
from app.utils.functions.fn_component_random_status import fn_component_random_status
from app.utils.functions.fn_generate_rand_int import fn_generate_rand_int as randInt
from app.utils.data.actuators import actuators


def fn_generate_actuator_data(location: str, actuator_name: str, num_datas: int = 1) -> list:
    actuator = actuators.get(actuator_name)
    
    if not actuator:
        return [{"msg": f"{actuator_name} not found in actuators list."}]

    data_list = []
    if actuator_name == "VentanaDoble":
        for _ in range(num_datas):
            for sub_actuator_name in ["Ventana Doble Izquierda", "Ventana Doble Derecha"]:
                windows_actions = []  # Inicializar la lista de acciones para cada iteración del bucle
                if randInt(0, 1) == 1:
                    windows_actions.append({
                        "name": "Activación mecánica",
                        "value": True,
                    })
                windows_actions.append({
                    "name": "Activación mecánica",
                    "value": False,
                })
                sub_actuator_data = generate_single_actuator_data(location, sub_actuator_name, fn_component_random_status(), windows_actions)
                data_list.append(sub_actuator_data)
    else:
        for _ in range(num_datas):
            actuator_data = generate_single_actuator_data(location, actuator_name)
            data_list.append(actuator_data)

    return data_list



def generate_single_actuator_data(location: str, actuator_name: str, status: str = None, actions: dict = None) -> dict:
    if actuator_name.startswith("Ventana Doble"):
        windows = actuators["VentanaDoble"]
        for window in windows:
            if window["name"] == actuator_name:
                actuator = window
                break
        else:
            raise ValueError(f"Subactuador '{actuator_name}' no encontrado en VentanaDoble.")

    else:
        actuator = actuators[actuator_name]

    if actions is None:        
        actions = []
        if actuator_name == "Puerta" or actuator_name == "Ventilador" or actuator_name == "BombaAgua" or actuator_name == "Ventilador":
            if randInt(0, 1) == 1:
                actions.append({
                    "name": "Activación mecánica",
                    "value": True
                })
            else:
                actions.append({
                    "name": "Activación mecánica",
                    "value": False
                })
        elif actuator_name == "LED_Interior" or actuator_name == "LED_Exterior" or actuator_name == "Alarma":
            if randInt(0, 1) == 1:
                actions.append({
                    "name": "Activación eléctrica",
                    "value": True
                })
            else:
                actions.append({
                    "name": "Activación eléctrica",
                    "value": False
                })
    
    if status is None:
        status = fn_component_random_status()

    actuator_data = {
        "arduinoIp": fn_random_ip(),
        "type": actuator["type"],
        "name": actuator["name"],
        "brand": actuator["brand"],
        "model": actuator["model"],
        "specifications": actuator["specifications"],
        "location": location,
        "status": status,
        "owner": fn_random_owner(),
        "actions": actions,
    }

    return actuator_data
