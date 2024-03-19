# Generate a "random" number with max and min limits, but also with a number of decimals
import random as r;  

def fn_generate_rand_decimal(minLimit: int, maxLimit: int, decimalsNumber: int) -> float:
    return round(r.uniform(minLimit, maxLimit), decimalsNumber);