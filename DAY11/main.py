from filereader import readfile
import typing as t

input = readfile("testinput")

mylist=[]
for item in input:
    item=item.split(":")
    mylist.append(item)


print(input)
print(mylist)