def read_input(file_int:int):
    if file_int==1:
        file_str="input.txt"
    else:
        file_str="testinput.txt"
    with open(file_str) as file:
        input=file.read()
        input=input.split("\n")
    return input
