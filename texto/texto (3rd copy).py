import csv
import datetime
import os


#################################################################



## SET-UP:
file_ = "templates/message.txt"
 

## LOADING CSV WITH DATA [Working:checked]

def csv_data(path):
    
    with open("data.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter = ",")
        line_count = 0
        for row in csv_reader:
            if row == row["enum_name"]:
                enum_name = enum_name[0].upper() + enum_name[1:].lower()
            elif row == row["interviewee"]:
                interviewee = interviewee[0].upper() + interviewee[1:].lower()
            elif  row == row["date_start"] and row == row ["date_end"]:
                date_start = {month}/{day}/{year}
            else:
                pass
        print(enum_name)
        print(interviewee)
        print(date_start)
    # def user_details(self,enum_name = None,project_name = None,date_start = None,date_end = None,training_hour = None,
    # training_room = None,interviewee = None,position_applied = None,interview_date = None,interview_hour = None):
    
    # enum_name = enum_name[0].upper() + enum_name[1:].lower()

    # #setting parameters so that this f(x) can react depending on inputs in the excel file
    # if enum_name != None: 

    # enum_name=None,project_name=None,date_start=None,date_end=None,training_hour=None,
    # training_room=None,interviewee=None,position_applied=None,interview_date=None,interview_hour=None

    # with open("data.csv") as csvfile:
    #     csv_reader = csv.DictReader(csvfile, delimiter = ",")
    #     line_count = 0
    #     # for row in csv_reader:
    #     #     print(f'\t{row["enum_name"]} is in the project called {row["project_name"]} from department, and was born in {row["date_start"]}')
    #     for row in csv_reader:
    #         if row == row["enum_name"]:
    #             enum_name = enum_name[0].upper() + enum_name[1:].lower()
    #         elif row == row["interviewee"]:
    #             interviewee = interviewee[0].upper() + interviewee[1:].lower()
    #         elif  row == row["date_start"] and row == row ["date_end"]:
    #             date_start = {month}/{day}/{year}
    #         else:
    #             pass

##  FUNCTIONS FOR CALLING OUR MESSAGE TEMPLATE INTO OUR CLASS [Working:checked]
def template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception (the file should name "message.txt" and it should be inside "templates" folder)
    return file_path
print(file_path)
def template(path):
    file_path = template_path(path)
    return open (file_path).read()
message = template(file_)
    

#
       


        
