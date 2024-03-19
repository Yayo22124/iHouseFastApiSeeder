import random

def fn_random_ip():
    seccion1 = str(random.randint(1, 255))
    seccion2 = str(random.randint(0, 255))
    seccion3 = str(random.randint(0, 255))
    seccion4 = str(random.randint(0, 255))
    
    direccion_ip = f"{seccion1}.{seccion2}.{seccion3}.{seccion4}"
    
    return direccion_ip