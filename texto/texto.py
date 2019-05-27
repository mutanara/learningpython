              ###################
################### SET-UP #######################
             ###################

#Python_Libraries_used
import pandas as pd
import numpy as np

#Python_modules_used
import os
import re

#input_parameters
path_text = "Templates/message.txt"
path_csv = "Templates/data.csv"
PathError = "the text file edited should be named 'message.txt' and should be placed inside 'Templates' folder"
max_attempt_msg = "Kindly seek a Python guy nearby for help...".title()
Welcome = "Welcome to Texto Python Script, a script designed to help you send SMS to a bunch of people at once in a short time.".upper()
headers = ["invitee_name","event_name","event_room","event_start","event_end","event_hour"]
headers_format = sorted(headers,key=str.lower,reverse=False)
read_no = "kindly go back and first read a file in Texto Package Folder called README.md"
headers_str = "( invitee_name,event_name,event_room,event_start,event_end,event_hour )"
conf_message_no = "kindly go back and first edit message.txt file in Templates folder..."


### Functions_for_displaying arrogantly_the_preliminaries_questions
def PRINT(anythhing):
    print("")
    print("")
    return print(anythhing)
    print("")
    print("")
def INPUT(anything):
    print("")
    print("")
    return input(anything) 
    print("")
    print("")


###  FUNCTIONS_FOR_CALLING_A_STRING_OUT_OF_MESSAGE_TEXT_WE_EDITED
def message_path(path_text):
    file_path = os.path.join(os.getcwd(), path_text)
    if not os.path.isfile(file_path):
        raise PathError
    return file_path
def our_message(path_text):
    file_path = message_path(path_text)
    return open (file_path).read()
source_message = our_message(path_text)


### string_substitution_functions
def make_messages (list_A=None,list_B=None,list_C=None,list_D=None,list_E=None,list_F=None):
        if (list_A,list_B,list_C,list_D,list_E,list_F) is not None:
                if len(list_A)==len(list_B)==len(list_C)==len(list_D)==len(list_E)==len(list_F):
                        i = 0
                        for invitee_name1 in list_A:
                                event_name1 = list_B[i]
                                event_start1 = list_C[i]
                                event_end1 = list_D[i]
                                event_hour1 = list_E[i]
                                event_room1= list_F[i]
                                new_message = source_message.format(invitee_name = invitee_name1,event_name = event_name1,event_room = event_room1,
                                event_start = event_start1,event_end = event_end1,event_hour = event_hour1)
                                i += 1
                                print(new_message)
        elif (list_A,list_B,list_C,list_E,list_F) is not None:
                if len(list_A)==len(list_B)==len(list_C)==len(list_E)==len(list_F):
                        i = 0
                        for invitee_name1 in list_A:
                                event_name1 = list_B[i]
                                event_start1 = list_C[i]
                                event_hour1 = list_E[i]
                                event_room1= list_F[i]
                                new_message = source_message.format(invitee_name = invitee_name1,event_name = event_name1,event_room = event_room1,
                                event_start = event_start1,event_hour = event_hour1)
                                i += 1
                                print(new_message)
        elif (list_A,list_B,list_C,list_E) is not None:
                if len(list_A)==len(list_B)==len(list_C)==len(list_E):
                        i = 0
                        for invitee_name1 in list_A:
                                event_name1 = list_B[i]
                                event_start1 = list_C[i]
                                event_hour1 = list_E[i]
                                new_message = source_message.format(invitee_name = invitee_name1,event_name = event_name1,
                                event_start = event_start1,event_hour = event_hour1)
                                i += 1
                                print(new_message)
        elif (list_A,list_B,list_E) is not None:
                if len(list_A)==len(list_B)==len(list_E):
                        i = 0
                        for invitee_name1 in list_A:
                                event_name1 = list_B[i]
                                event_hour1 = list_E[i]
                                new_message = source_message.format(invitee_name = invitee_name1,event_name = event_name1,event_hour = event_hour1)
                                i += 1
                                print(new_message)
        else:
                pass
        return new_message
         

#### CONFIRMATION_ ! _
#confirm_reading_catalog
Auth_read = False
PRINT(Welcome)
instruction_read = INPUT("I.Did You First Read and Understand README.md File (Yes/No)?  ").title()
max_attempt = 2
count = 0
while instruction_read not in ("Yes", "No"):
        count += 1
        if count > max_attempt:
                PRINT(max_attempt_msg)
                break 
        instruction_read = input(f"({count})Try again~Answers For The Above Should Be Among (yes/Yes/YES/no/No/NO) : ").title()
else:
        if instruction_read in ("No"):
                        print(read_no)
        elif instruction_read in ("Yes"): 
                Auth_read = True
                PRINT(headers_str)
                headers_input = input("II.Which of the above are the headers of your data.csv file? (leave space between headers'names you are writing) : ").lower()
                headers_used = re.findall("\S+", headers_input)
                headers_cleaning = list(set(headers_used) & set(headers_format)) # to only remain with the intersection
                headers_cleaned = sorted (headers_cleaning,key=str.lower,reverse=False)


#confirmation _of_edited_message
msg_confirmed = False
if Auth_read == True:
        PRINT(source_message)
        confirm_message = INPUT("Is the message above the one you want to use (Yes/No)?  ".upper()).title()
        count_conf = 0
        while confirm_message not in ("Yes", "No"):
                count_conf += 1
                if count > max_attempt:
                        print(max_attempt_msg)
                        break 
                confirm_message = input(f"({count})Try again ~ Answers For The Above Should Be Among (yes/Yes/YES/no/No/NO) : ").title()
        else:
                if confirm_message in ("No"):
                        print(conf_message_no)
                elif confirm_message in ("Yes"):
                        msg_confirmed = True


Lists_created = True
if msg_confirmed == True:
        csv_data = pd.read_csv(path_csv, delimiter = ",", usecols=headers_cleaned)
        print(csv_data)
        if headers_cleaned == headers_format:
                invitee_name = csv_data["invitee_name"].values.tolist()
                event_name = csv_data["event_name"].values.tolist()
                event_room = csv_data["event_room"].values.tolist()
                event_start = csv_data["event_start"].values.tolist()
                event_end = csv_data["event_end"].values.tolist()
                event_hour = csv_data["event_hour"].values.tolist() 
        elif headers_cleaned == ["event_hour","event_name","event_room","event_start","invitee_name"]:  # making sure that this list is sorted is crucial for the matching.
                invitee_name = csv_data["invitee_name"].values.tolist()
                event_name = csv_data["event_name"].values.tolist()
                event_room = csv_data["event_room"].values.tolist()
                event_start = csv_data["event_start"].values.tolist()
                event_hour = csv_data["event_hour"].values.tolist()
        elif headers_cleaned == ["event_hour","event_name","event_start","invitee_name"]:  # making sure that this list is sorted is crucial for the matching.
                invitee_name = csv_data["invitee_name"].values.tolist()
                event_name = csv_data["event_name"].values.tolist()
                event_start = csv_data["event_start"].values.tolist()
                event_hour = csv_data["event_hour"].values.tolist()
        elif headers_cleaned == ["event_hour","event_name","invitee_name"]:  # making sure that this list is sorted is crucial for the matching.
                invitee_name = csv_data["invitee_name"].values.tolist()
                event_name = csv_data["event_name"].values.tolist()
                event_hour = csv_data["event_hour"].values.tolist()
        else:
                Lists_created = False
                print(max_attempt_msg)
                print("Dear python guy, kindly look at the conditionals that produces lists or")

if Lists_created == True:
        if headers_cleaned == headers_format:
                send = make_messages(invitee_name,event_name,event_start,event_end,event_hour,event_room) #make sure order of this is same as in the make_message function
                print(send)
        elif headers_cleaned == ["event_hour","event_name","event_room","event_start","invitee_name"]:  
                send = make_messages(invitee_name,event_name,event_start,event_hour,event_room)
                print(send)
        elif headers_cleaned == ["event_hour","event_name","event_start","invitee_name"]:
                send = make_messages(invitee_name,event_name,event_start,event_hour) #make sure order of this is same as in the make_message function
                print(send)
        elif headers_cleaned == ["event_hour","event_name","invitee_name"]:
                send = make_messages(invitee_name,event_name,event_hour) #make sure order of this is same as in the make_message function
                print(send)
        else:
                Lists_created = False
                print(max_attempt_msg)
                print("Dear python guy, kindly look at the conditionals that produces do string substitution")


