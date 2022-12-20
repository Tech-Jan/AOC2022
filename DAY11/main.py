from filereader import readfile
import typing as t

input = readfile("testinput")

mylist2 = []
mydict2 = {}
lista = []
i = -1
for item in input:
    mydict2 = {}
    level = (len(item) - len(item.lstrip("  "))) // 2
    item = item.lstrip((" "))
    item = item.split(":")

    mydict2[item[0]] = item[1]
    if level == 2:
        if type(mylist2[i][monkey]["Test"]) != dict:
            mylist2[i][monkey]["Test"] = mydict2
        else:
            mylist2[i][monkey]["Test"].update(mydict2)

    if level == 1:
        if type(mylist2[i][monkey]) != dict:
            mylist2[i][monkey] = mydict2
        else:
            mylist2[i][monkey].update(mydict2)
    if level == 0:
        mylist2.append(mydict2)
        monkey = item[0]
        i += 1

print(input)

print(mylist2)
for item in mylist2:
    print(list(item.keys())[0])
    print(item[list(item.keys())[0]])
    print(item[list(item.keys())[0]]["Starting items"])
