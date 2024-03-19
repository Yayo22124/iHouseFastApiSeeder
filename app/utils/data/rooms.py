rooms = [
    "Recámara 1",
    "Recámara 2",
    "Recámara 3",
    "Baño 1",
    "Baño 2",
    "Cocina",
    "Garaje",
    "Sala",
]

collections = ["bedrooms", "bathrooms", "livingrooms", "garages", "kitchens"]

rooms_by_collection = {
    "bedrooms": [
        "Recámara 1",
        "Recámara 2",
        "Recámara 3",
    ],
    "bathrooms": [
        "Baño 1",
        "Baño 2",
    ],
    "kitchens": [
        "Cocina",
    ],
    "garages": [
        "Garaje",
    ],
    "livingrooms": [
        "Sala",
    ],
}

rooms_components = {
    "bedrooms": {
        "sensors": ["Temperatura", "Fotorresistencia"],
        "actuators": [
            "Puerta",
            "VentanaDoble",
            "Ventilador",
            "LED_Interior",
            "LED_Exterior",
        ],
    },
    "livingrooms": {
        "sensors": ["Temperatura", "Fotorresistencia"],
        "actuators": [
            "Ventilador",
            "LED_Interior",
            "LED_Exterior",
            "VentanaDoble",
            "Puerta",
        ],
    },
    "kitchens": {
        "sensors": ["Gas", "Temperatura", "Fotorresistencia"],
        "actuators": [
            "VentanaDoble",
            "Ventilador",
            "LED_Interior",
            "LED_Exterior",
            "Puerta",
        ],
    },
    "bathrooms": {
        "sensors": ["Presencia", "Proximidad", "Fotorresistencia"],
        "actuators": [
            "Puerta",
            "BombaAgua",
            "LED_Interior",
            "LED_Exterior",
        ],
    },
    "garages": {
        "sensors": ["Fotorresistencia"],
        "actuators": ["Puerta", "LED_Interior", "LED_Exterior", "PuertaGaraje"],
    },
}
