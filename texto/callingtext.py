import os


#################################################################


##  FUNCTIONS_FOR_CALLING_A_STRING_FROM_OUR_MESSAGE_TEXT_IN_THE_FOLDER
def message_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise PathError ("The Text File edited Should Be Named 'message.txt' And Should Be Inside 'Templates' Folder")
    return file_path
def our_message(path):
    file_path = message_path(path)
    return open (file_path).read()
message = our_message("Templates/message.txt")

print(message)



        
