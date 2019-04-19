#First way of doing it at once.


# list_fam = [
#     "Nara","mahame","Gemma","gustave","Vicky",
#     1995,1991,1989,1986,1985,19.95,19.91,19.89,19.86,19.85
#     ]

# list_names = []
# list_bd = []
# list_dec = []

# for i in list_fam:
#     if isinstance(i,str):
#         list_names.append(i)
#     list_names.sort(key=str.lower)
# print(list_names)

# for i in list_fam:
#     if isinstance(i, int):
#         list_bd.append(i)
#     list_bd.sort(reverse = False)
# print(list_bd)

# for i in list_fam:
#     if isinstance(i, float):
#         list_dec.append(i)
#     list_dec.sort(reverse = False)
# print(list_dec)


#Second way of doing it

initial_list = ["Nara","mahame","Gemma","gustave","Vicky"]  
organized_list = sorted (initial_list, key=str.lower, reverse = False) # you can add reverse or not, just like you can chooise to use the key or not.
print(organized_list)
