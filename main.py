from random import randint



def get_numbers_ticket(min, max, quantity):
    result_array = set()
    while len(result_array) != quantity:
        www = result_array.add(randint(min, max))  
    result_array = sorted(list(result_array))
    return result_array
        
    

lottery_numbers = get_numbers_ticket(1, 49, 5)
print("Ваші лотерейні числа:", lottery_numbers)

