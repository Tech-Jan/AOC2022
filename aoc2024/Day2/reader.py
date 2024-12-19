def read_input(file_str:str):
    with open(file_str) as file:
        input=file.read().split("\n")
    return input
