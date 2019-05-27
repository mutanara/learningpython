import pandas as pd
import numpy as np 
import os



# print(len("training"))
# purpose = input("are you tring to send a message for: training / interview OR invitation?   ".title())
# print(len(purpose))


# #FIRST_WAY
# def number(x):
#     if len(x) in (4,6,8) and x.isdigit():
#         print ("True")
#     else:
#         print ("False")
#     return "Done"
# print(number("123456789"))

# #SECOND_WAY
# def number(x):
#     if len(x) in range(10) and x.isdigit():
#         print ("True")
#     else:
#         print ("False")
#     return "Done"
# print(number("12345678"))



# i = 0
# while i < 10:
#     j = 0 
#     while j < 10:
#         if j <= i:
#             print(j+1, end ="")
#         j += 1
#     print("")
#     i += 1 



# if len(x) in (4,6,8) and x.isdigit():
#         print ("True")
#     else:
#         print ("False")
#     return "Done"

# ## SETTING UP

# def PRINT(anythhing):
#     print("")
#     return print(anythhing)
#     print("")

# def INPUT(anything):
#     print("")
#     return input(anything) 
#     print("")


# tex = INPUT("").title()
# text = "Yes"
# text_A = ["Yes", "yes", "YES"]
# print(tex)
# # print(tex == text)
# print(tex is text)
# # print(tex in text_A)

# instruction_read = INPUT("Did You First Read and Understand README.md File (Yes/No)?   ").title()
# print(True if instruction_read in "Yes" else False)

# txt = "welcome to the jungle"
# x = txt.split()
# print(x) 

# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x)

# txt = "apple#banana#cherry#orange"
# # setting the max parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)
# print(x)

# b = input()
# print(b)
# print(type(b))
# list_b = b.split(",")
# print(list_b)
# list_a = ["a", "b", "c", "d"]
# list_c = list(set(list_b) | set(list_a))
# print(list_c)

# headers_format = ["invitee-name", "event-name", "event-start", "event-end", "event-hour"]
# PRINT("( invitee-name, event-name, event-start, event-end, event-hour )")
# headers_input = input("Which of the above are the headers of your data.csv file? (add a colon between what you type) : ").lower()
# headers_input2 = headers_input.split(",")
# print(headers_input)


# df_main = pd.DataFrame({'Product': ['Tablet','iPhone','Laptop','Monitor'],'Price': [250,800,1200,300]})

# list_product = df_main["Product"].values.tolist()
# print(list_product)
# list_Price = df_main["Price"].values.tolist()
# print(list_Price)



y = ["invitee_name","event_name","event_room","event_start","event_end","event_hour"]
list_y = sorted(y,key=str.lower,reverse=False)
print(list_y)
x = ['event_hour', 'event_start', 'invitee_name', 'event_end', 'event_name', 'event_room']
list_x = sorted(y,key=str.lower,reverse=False)
print(list_x)
print(list_x == list_y)


# initial_list = ["Nara","mahame","Gemma","gustave","Vicky"]  
# organized_list = sorted (initial_list, key=str.lower, reverse = True) # you can add reverse or not, just like you can chooise to use the key or not.
# print(organized_list)