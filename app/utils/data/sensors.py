sensors = {
    "Temperatura": {
        # "_id": "65dd080111bbe96dbfe4b2d2",
        "arduinoIp": "",
        "type": "Sensor",
        "name": "Temperatura y Humedad",
        "brand": "Genérico",
        "model": "DHT11",
        "specifications": [
            {
                "name": "Rango de medición de temperatura",
                "minValue": 0.0,
                "maxValue": 50.0,
                "unit": "°C",
            },
            {
                "name": "Rango de medición de humedad",
                "minValue": 20.0,
                "maxValue": 90.0,
                "unit": "%",
            },
            {
                "name": "Voltage de operación",
                "value": 5.5,
                "unit": "V",
            },
            {
                "name": "Corriente de operación",
                "value": 2.5,
                "unit": "mA",
                "type": "VCD",
            },
            {
                "name": "Consumo eléctrico",
                "value": 0.00125,
                "unit": "W",
            },
        ],
        "location": "",
        "status": "",
        "owner": "",
        "readings": [
            {
                "name": "Detección de Temperatura",
                "value": 0.00,
                "measurementUnit": "°C",
            },
            {
                "name": "Detección de Humedad",
                "value": 0.00,
                "measurementUnit": "%",
            },
        ],
    },
    "Fotorresistencia": {
        # "_id": {"$oid": "65dd0b0611bbe96dbfe4b2d4"},
        "arduinoIp": "",
        "type": "Sensor",
        "name": "Fotorresistencia",
        "brand": "Genérico",
        "model": "LDR",
        "specifications": [
            {
                "name": "Rango espectral",
                "minValue": 400.0,
                "maxValue": 700.0,
                "unit": "nm",
            },
            {"name": "Rango de respuesta", "minValue": 0, "maxValue": 1024},
            {
                "name": "Voltage de operación",
                "value": 5.0,
                "unit": "V",
            },
            {
                "name": "Corriente de operación",
                "value": 0.45,
                "unit": "mA",
                "type": "VCD",
            },
            {
                "name": "Consumo de operación",
                "value": 1.56,
                "unit": "W",
            },
        ],
        "location": "",
        "status": "Disponible",
        "owner": "",
        "readings": [
            {
                "name": "Detección de iluminación",
                "value": 0,
            }
        ],
    },
    "Presencia": {
        "type": "Sensor",
        "name": "Presencia",
        "brand": "Rantec",
        "model": "HC-SR501",
        "specifications": [
            {
                "name": "Rango de distancia",
                "maxValue": 700,
                "minValue": 200,
                "measurementUnit": "cm",
            },
            {
                "name": "Alimentacion de Energía",
                "maxValue": 12,
                "minValue": 5,
                "measurementUnit": "V",
            },
        ],
        "location": "",
        "status": "",
        "owner": "",
    },
    "Proximidad": {
        "type": "Sensor",
        "name": "Proximidad",
        "brand": "AEDIKO",
        "model": "HC-SR04",
        "specifications": [
            {
                "name": "Rango de distancia",
                "maxValue": 400,
                "minValue": 2,
                "measurementUnit": "cm",
                "acurracy": "+-0.3",
            },
            {
                "name": "Alimentacion de Energía",
                "maxValue": 5,
                "minValue": 3.3,
                "measurementUnit": "V",
            },
        ],
        "location": "",
        "status": "",
        "owner": "",
    },
    "Gas": {
        "type": "Sensor",
        "name": "Gas",
        "brand": "Steren",
        "model": "K 1015",
        "specifications": [
            {"name": "Consumo", "minValue": 5, "maxValue": 5, "unit": "volts"},
            {"name": "Amoníaco", "minimum": 10, "maximum": 300, "units": "ppm"},
        ],
        "location": "",
        "status": "",
        "owner": "",
        "readings": [
            {"name": "Detección de Gas", "vale": 0.0, "measurementUnit": "ppm"}
        ],
    },
}
