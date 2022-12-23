def readfile(rawdata):
    data = open(rawdata, "r").read()
    data = data.split("\n")
    if rawdata == "mypath":
        return data
    data_split = [list(row) for row in data]
    return data_split
