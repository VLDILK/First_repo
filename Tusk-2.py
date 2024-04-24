from random import sample

def get_numbers_ticket(min, max, quantity):
    if min <= 0 or max > 1000 or min >= max or quantity < 1 or quantity > max or quantity > (max-min+1):
        return []
    result_array = sample(range(min, max + 1), quantity)

    return result_array
   
   
        


