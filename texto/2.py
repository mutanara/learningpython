import pandas as pd
import numpy as np 
import os

def print_(anythhing):
    print("")
    print(anythhing)
    print("")

def input_(anything):
    print("")
    input(anything)
    print("")

print_("Welcome to Texto Python Script, a script designed to help you send SMS to a bunch of people at once in a short time.".upper())
instruction_read = str(input_("Did You First Read and Understand README.md File (Yes/No)?  : ")).lower()
print_(instruction_read)
purpose = str(input_("are you tring to send a message for: training / interview OR invitation?  : ".title())).lower()
print_(instruction_read)
