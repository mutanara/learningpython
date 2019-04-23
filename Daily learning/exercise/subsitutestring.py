# SIMPLE DEMONSTRATION.

# text = "some people like {name} are crazy"
# text_sub= "some people like {name} are crazy".format(name="Silas")
# print(text_sub)

# # COMPLICATED DEMONSTRATION.

#first_way
# housemates  = ["Luka:Tallest one", "Silas:Black one", "Nara:Nice one"]
# message = " If either {name} is home,please tell him to fetch water".format(name=housemates)
# print(message)


# second_way
# hoe_members = ["Silas","Nara","Luka","Plante"]
# msg = "hey %s, how are you?." 
# print(msg %(hoe_members))


# third_way
# "hey %s, how are you?." %(hoe_members)
# print("hey %s, how are you?." %(hoe_members))


# fourth_way
# print("%s is workaholic coder, %s is a business dreammer, %s is a caring sinner, %s is a mysterious nice person."
# %("Luka", "Plante", "Silas", "Nara"))

#  fifth_way
# housemates  = ["Luka:Tallest one", "Silas:Black one", "Nara:Nice one"]
# message = f"If either {housemates} is home,please tell him to fetch water." # avoid spaces between between f and " or " and the starting of the sentence if you used this formating style in python3
# print(message)