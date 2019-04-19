
# A function which breaks one big list of different items into other different list depending on the  variable type, and sort each respective list. 
# Just add items inside the anylist below then see the magic happening.

list_a = []

list_a = ["nara","Gemma","Mahame","Vicky", 1995, 1991,1989,1985,19.95,19.91,19.89,19.95]

def part_sort(anymixedlist):
    str_list = []
    int_list = []
    float_list = []

    for x in list_a:
        if isinstance(x, int):
            int_list.append(x)
        int_list.sort(reverse = False)
       
    for x in list_a:
        if isinstance(x, float):
            float_list.append(x)
        float_list.sort(reverse = False)
    
    for x in list_a:  
        if isinstance(x, str):
            str_list.append(x)
        str_list.sort(key=str.lower)

    return str_list, float_list, int_list      
    
print(part_sort(list_a))


# Zipping function:

# x = [1, 2, 3]
# y = [4, 5, 6]

# zip(x, y)
# for i in zip(x, y):
#     print(i)
