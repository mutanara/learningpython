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


###  FUNCTIONS_FOR_CALLING_A_STRING_OUT_OF_MESSAGE_TEXT_WE_EDITED
def message_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise PathError ("the text file edited should be named 'message.txt' and should be placed inside 'Templates' folder")
    return file_path


def our_message(path):
    file_path = message_path(path)
    return open (file_path).read()
message = our_message("Templates/message.txt")


###class_confirm_information
class confirm_():
        PRINT("Welcome to Texto Python Script, a script designed to help you send SMS to a bunch of people at once in a short time.".upper())
        #setting-up
        headers_format = ["invitee-name", "event-name", "event-start", "event-end", "event-hour"]
        read_no = "kindly go back and first read a file in Texto Package Folder called README.md"
        headers_str = "( invitee-name, event-name, event-start, event-end, event-hour )"
        max_attempt_msg = "kindly seek help from The Amazing Nara..."
        conf_message_no = "kindly go back and first edit message.txt file in Templates folder..."

        #confirm_reading_catalog
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
                        PRINT(headers_str)
                        headers_input = input("II.Which of the above are the headers of your data.csv file? (leave space between headers'names you are writing) : ").lower()
                        headers_input2 = headers_input.split()
                        headers_used = list(set(headers_input2) & set(headers_format)) # to only remain with the intersection
        # confirmation _of_edited_message
                        PRINT(message)
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
                                        csv_data = pd.read_csv("data.csv", delimiter = ",", usecols=headers_used)
                                        print(csv_data)


### Function_for_loading_and_using_csv_data

# def load_csv (invitee-name=None, event-name=None, event-start=None, event-end=None, event-hour=None):
#         if invitee-name != None and invitee 

#  invitee-name, event-name, event-start, event-end, event-hour )




# # # Advanced CSV loading example
# # data = pd.read_csv(
# # "data/files/complex_data_example.tsv", ## relative python path to subdirectory
# # sep='\t' ## Tab-separated value file.
# # quotechar="'",  ## single quote allowed as quote character
# # dtype={"salary": int},  ## Parse the salary column as an integer 
# # usecols=['name', 'birth_date', 'salary']. ## Only load the three columns specified.
# # parse_dates=['birth_date'], ## Intepret the birth_date column as a date
# # skiprows=10, ## Skip the first 10 rows of the file
# # na_values=['.', '??']  ## Take any '.' or '??' values as NA
# #     )


# # # class load_csv():
# # #     name = []
# # #     event = []
# # #     date_end = []
# # #     date_start = []
# # #     hour_start = []
# # #     event_room = []
# # #     position_applied = []


# if confirm_message in ("Yes"):
#         csv_data = pd.read_csv("data.csv", delimiter = ",", usecols=headers_used)
#         print(csv_data)