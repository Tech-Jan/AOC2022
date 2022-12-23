def readfile(rawdata):
    data = open(rawdata, "r").read()
    data = data.split("\n")
    data_split = [list(row) for row in data]
    return data_split
