from ..data.owners import owners;
from .fn_generate_rand_int import fn_generate_rand_int as rand_int;
def fn_random_owner() :
    rand_owner = rand_int(0, len(owners) - 1);

    return owners[rand_owner]