# Author: CMOB 3/7/2022

def r_max(nested_num_lst):
    total = 0
    for element in nested_num_lst:
        if type(element) == list:
            if type(element) > total:
                total = r_max(element) 

    return total

print(r_max([1,2,3[23,44],55]))