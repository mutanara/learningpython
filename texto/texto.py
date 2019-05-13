import pandas as pd
import numpy as np 
import os

#########################################

### OWN_FUNCTIONS_FOR_ARROGANCE_DISPLAY
def PRINT(anythhing):
    print("")
    return print(anythhing)
    print("")

def INPUT(anything):
    print("")
    return input(anything) 
    print("")

### PRELIMINARIES
PRINT("Welcome to Texto Python Script, a script designed to help you send SMS to a bunch of people at once in a short time.".upper())
instruction_read = INPUT("Did You First Read and Understand README.md File (Yes/No)?   ").title()
max_attempt = 3
count = 1
while instruction_read not in ("Yes", "No"):
    count += 1
    if count > max_attempt:
        PRINT("kindly seek The Amazing Nara for help...")
        break 
    warning_failed1 = INPUT(f"({count})Answers For The Above Should Be Among (yes/Yes/YES/no/No/NO) : ").title()   
else:
    if instruction_read in ("No"):
        PRINT("Kindly Go Back and Read a File In Texto Package Folder named README.md")
    elif instruction_read in ("Yes"):
        purpose = INPUT("are you tring to send a message for: training / interview OR invitation?   ".title()).title()
        count_prp = 1
        while purpose not in ("Training", "Interview", "Invitation"):
            count_prp += 1
            if count_prp > max_attempt :
                PRINT("kindly seek The Amazing Nara for help...")
                break 
            warning_failed2 = INPUT(f"({count_prp})Answers For The Above Should Be Among (Training/Interview/Invitation) : ").title()


###  FUNCTIONS_FOR_CALLING_A_STRING_OUT_OF_MESSAGE_TEXT_WE_EDITED
def message_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise PathError ("The Text File edited Should Be Inside 'Templates' Folder")
    return file_path
def our_message(path):
    file_path = message_path(path)
    return open (file_path).read()
message1 = our_message("Templates/interview.txt")
message2 = our_message("Templates/training.txt")
message3 = our_message("Templates/invitation.txt") 


###  LOADING_CSV_DATA_AND_USING_THEM (BY THE HELP OF DATAFRAME)