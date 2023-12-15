


def filereader(FILE):
    with open(FILE, "r") as f:
        data = f.read().split("\n")
        datalist = []
        for line in data:
            splitdata = line.split(":")
            linelist = []
            for splits in splitdata:
                posx = splits.index("x=")
                posy= splits.index("y=")
                xy=[int(splits[posx+2:posy-2]),int(splits[posy+2:])]
                linelist.append(xy)
            datalist.append(linelist)

    return datalist


if __name__ == "__main__":
    filereader()
