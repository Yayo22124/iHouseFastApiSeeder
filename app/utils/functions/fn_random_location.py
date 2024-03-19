from app.utils.functions import fn_generate_rand_int as rand_int;
from ..data.rooms import rooms;


def fn_random_location ():
    random_location = rand_int(0, len(rooms) - 1);
    
    return rooms[random_location];