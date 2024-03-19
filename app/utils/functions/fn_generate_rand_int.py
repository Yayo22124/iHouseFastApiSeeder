# Generate a random number in a range (min and max limit)
import random as r # Random library lets to generate "random" numbers

def fn_generate_rand_int(minLimit: int, maxLimit: int) -> int : 
    return  r.randint(minLimit, maxLimit);