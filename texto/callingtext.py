import re


we = "muta@email.com nara@gmail.com nm@yahoo.com"

def the_match(anyfx):
    rule_sha = re.match("\S+@\S+[a-b]\S+.com",anyfx)
    return rule_sha
print(the_match(we))

# Failed = True
# email = input("Please enter your email: ")

# count = 0
# while the_match(email) is None:
#     count += 1
#     if count > 3: 
#         print("Email does not exist")
#         break
#     email = input(f"{count}:re-enter your email again:  ")
# else:
#     Failed = False
# print("Calling RIB..." if Failed else "Access guaranteed")    