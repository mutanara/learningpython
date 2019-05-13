

# ################################################################



# Failed = False
# email = input("Please enter your email: ")
# password1 = input("Please enter your password: ")
# password2 = input("Please re-enter your password: ")

# count = 0
# while password1 != password2:
#     count += 1
#     if count > 2 : break
#     print("PASSWORDS ABOVE DO NOT MATCH")
#     password1 = input(f"{count}:re-enter your first password: ")
#     password2 = input(f"{count}:re-enter the same password as above: ")
# else:
#     Failed = True
# print("Access guaranteed" if Failed else "Calling RIB...")   




# answers = ["no","No","NO","yes","Yes","YES"]
# Failed = False
# instruction_read = input_("Did You First Read and Understand README.md File (Yes/No)?   ")
# count = 0
# while instruction_read in ("no","No","NO","yes","Yes","YES") and len(instruction_read) == 3 and instruction_read.isalpha():
#     count_yes = 0
#     while instruction_read in ("yes","Yes","YES"):
#         purpose = input_("are you tring to send a message for: training / interview OR invitation?   ".title())
#         count_yes += 1
#     count_no = 0
#     while instruction_read in ("no","No","NO"):
#         print("Kindly Go Back and Read a File In Texto Package Folder named README.md")
#         count_no += 1
#     count += 0
# else:
#     Failed = True
#     count_failed = 1
#     while instruction_read not in ("no","No","NO","yes","Yes","YES") and len(instruction_read) == 3 and instruction_read.isalpha():
#         count_failed += 1
#         if count_failed > 4 : break
#         warning_failed = input_(f"{count_failed}:Answers should be among:  yes/Yes/YES/no/No/NO ")
# print(purpose if Failed else "Kindly Look for Amazing Nara...")


## SETTING UP

def PRINT(anythhing):
    print("")
    return print(anythhing)
    print("")

def INPUT(anything):
    print("")
    return input(anything) 
    print("") 
