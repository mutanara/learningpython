import pandas as pd
import numpy as np 
import os



print(len("training"))
purpose = input("are you tring to send a message for: training / interview OR invitation?   ".title())
print(len(purpose))


#FIRST_WAY
def number(x):
    if len(x) in (4,6,8) and x.isdigit():
        print ("True")
    else:
        print ("False")
    return "Done"
print(number("123456789"))

#SECOND_WAY
def number(x):
    if len(x) in range(10) and x.isdigit():
        print ("True")
    else:
        print ("False")
    return "Done"
print(number("12345678"))



i = 0
while i < 10:
    j = 0 
    while j < 10:
        if j <= i:
            print(j+1, end ="")
        j += 1
    print("")
    i += 1 



if len(x) in (4,6,8) and x.isdigit():
        print ("True")
    else:
        print ("False")
    return "Done"

## SETTING UP

def PRINT(anythhing):
    print("")
    return print(anythhing)
    print("")

def INPUT(anything):
    print("")
    return input(anything) 
    print("")


tex = INPUT("").title()
text = "Yes"
text_A = ["Yes", "yes", "YES"]
print(tex)
# print(tex == text)
print(tex is text)
# print(tex in text_A)

instruction_read = INPUT("Did You First Read and Understand README.md File (Yes/No)?   ").title()
print(True if instruction_read in "Yes" else False)






max_attempt = 3
count = 1
while instruction_read not in ("Yes", "No"):
    count += 1
    if count > max_attempt : break 
    warning_failed1 = INPUT(f"({count})Answers For The Above Should Be Among (yes/Yes/YES/no/No/NO) : ").title()
    if count > max_attempt:
        PRINT("Kindly look for amazing Nara for help...".title())
else:
    if instruction_read in ("No"):
        PRINT("Kindly Go Back and Read a File In Texto Package Folder named README.md")
    elif instruction_read in ("Yes"):
        purpose = INPUT("are you tring to send a message for: training / interview OR invitation?   ".title()).title()
        count_prp = 1
        while purpose not in ("Training", "Interview", "Invitation"):
            count_prp += 1
            if count_prp > max_attempt : break 
            warning_failed2 = INPUT(f"({count_prp})Answers For The Above Should Be Among (Training/Interview/Invitation) : ").title()
            if count_prp > max_attempt:
                PRINT("Kindly look for amazing Nara for help...".title())
        else:
            Auth2 = True
            PRINT("Done" if Auth2 else "Kindly look for amazing Nara for help...".title())
    else:
        pass 