# Author: CMOB 3/7/2022

def factorial(num):
    total = 1 
    counter = 1
    if num != 0:
        while counter <= num:
            total *= counter
            counter += 1
    elif num == 0 :
        print("0 cannot be used for a factorial")
        
    return total



print(factorial(5))