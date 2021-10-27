list_=[1,1,2,2]
set(list_)
set_1={1,2,3,4,5,6}
set_2={4,5,6,7,8,9}
def unique_numbers(set_1):
       return list(set(set_1))
print(unique_numbers(set_1))

def intersection_lists(set_1, set_2):
       return list(set(set_1) and set(set_2))
print(intersection_lists(set_1, set_2))