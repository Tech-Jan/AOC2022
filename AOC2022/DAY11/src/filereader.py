def readfile(rawdata):
    data = open(rawdata, "r").read()
    data = data.split("\n")
    return data
