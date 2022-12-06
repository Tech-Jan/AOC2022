def readfile(rawdata):
    data = open(rawdata, "r").read()
    # data = f.split()
    datalist = list(data)
    del datalist[-1]
    return datalist


def analyzefile(listdata, codelength):
    b = 0
    for b in range(0, len(listdata)):
        i = 0
        code = []
        for i in range(0, codelength):
            code.append(listdata[b + i])
        if len(set(code)) < codelength:
            b += 1
            # print((set(code)))
            # print((code))
        else:
            return [code, b + codelength]
    return
