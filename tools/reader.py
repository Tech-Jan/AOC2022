import os
import sys

def read_input(file_int:int):
    if file_int==1:
        file_str= os.path.dirname(sys.argv[0])+ '\\input.txt'

    else:
        file_str= os.path.dirname(sys.argv[0])+ '\\testinput.txt'
    with open(file_str) as file:
        input=file.read()
        input=input.split("\n")
    return input
