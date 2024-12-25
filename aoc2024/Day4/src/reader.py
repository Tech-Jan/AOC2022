import os

def read_input(file_int:int):
    if file_int==1:
        file_str= os.path.join(os.path.dirname(__file__), 'input.txt')
    else:
        file_str= os.path.join(os.path.dirname(__file__), 'testinput.txt')
    with open(file_str) as file:
        input=file.read()
        input=input.split("\n")
    return input
