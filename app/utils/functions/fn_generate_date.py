# Generar una función que nos permita generar fechas aleatorias en formato requerido en Mongo, considerar fecha y hora límites válidos.
from datetime import datetime as dt
from .fn_generate_rand_int import fn_generate_rand_int as randInt
import random;

def fn_generate_date(
    yearMinLimit: int,
    yearMaxLimit: int,
    monthMinLimit: int,
    monthMaxLimit: int,
    dayMinLimit: int,
    dayMaxLimit: int,
    hoursMinLimit: int,
    hoursMaxLimit: int,
    minutesMinLimit: int,
    minutesMaxLimit: int,
    secondsMinLimit: int,
    secondsMaxLimit: int,
) -> dict:
    randomTimestamp = dt(
        randInt(yearMinLimit, yearMaxLimit),
        randInt(monthMinLimit, monthMaxLimit),
        randInt(dayMinLimit, dayMaxLimit),
        randInt(hoursMinLimit, hoursMaxLimit),
        randInt(minutesMinLimit, minutesMaxLimit),
        randInt(secondsMinLimit, secondsMaxLimit),
    ).timestamp()

    return {"$date": {"$numberlong": str(randomTimestamp)}}


def generar_fecha_aleatoria_mongodb(fecha_inicio, fecha_fin, hora_inicio, hora_fin):
    fecha_inicio = dt.datetime.strptime(
        fecha_inicio + " " + hora_inicio, "%Y-%m-%d %H:%M: %S"
    )
    fecha_fin = dt.datetimestrptime(fecha_fin + " " + hora_fin, "%Y-%m-%d %H:%M:%S")
    # Calcular el rango de tiempo en segundos entre fechaInicio y fechaFin
    rango_tiempo = (fecha_fin - fecha_inicio).total_seconds()

    # Genera un número aleatorio dentro del rango de tiempo
    tiempo_aleatorio = random.uniform(0, rango_tiempo)

    # Calcula la fecha aleatoria dentro del rango de tiempo
    fecha_aleatoria = fecha_inicio + dt.timedelta(seconds=tiempo_aleatorio)

    # Formatea la fecha en el formato compatible con MongoDB (ISO 8601)
    fecha_aleatoria_mongodb = fecha_aleatoria.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return {
        "$date": str(fecha_aleatoria_mongodb)
    }
