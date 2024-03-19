from .fn_generate_rand_int import fn_generate_rand_int as rand_int;

def fn_component_random_status() :
    if rand_int(0, 1) == 1:
        return "Disponible"
    return "No disponible"
    