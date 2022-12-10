import filereader
from harddisktree import TreeNode
from collections import defaultdict
from pprint import pprint

list = filereader.readfile("input")

my_harddisk = TreeNode("my_harddisk")

selected_node = my_harddisk
i = 1
for item in list:
    if item[0:4] == "$ cd":
        code = item.split(" ")
        if code[2] == "/":
            print("backtoharddisk")
        elif code[2] == "..":
            print("levelup")
            print(item)
            print(selected_node.name)
            selected_node = selected_node.parent
        else:
            for child in selected_node.children:
                if child.name == "dir " + str(code[2]):
                    print("leveldown")
                    print(item)
                    print(selected_node.name)
                    selected_node = child
    if item[0:4] == "$ ls":
        i = list.index(item, i) + 1
        while list[i][0] != "$":
            a = list[i]
            if a[0:3] == "dir":
                selected_node.add_child(TreeNode(list[i]))
            else:
                selected_node.add_data(list[i])
            i += 1

print(my_harddisk.print_tree())
print(my_harddisk.get_sum10000())
# print(sum(my_harddisk.get_sum10000()))

# part 2
a = 70000000 - my_harddisk.get_sum()
b = 30000000 - a
c = [b]
print(sorted(my_harddisk.get_highfoldersize(b)[1]))

def readfile(rawdata):
    data = open(rawdata, "r").read()
    return data
l=readfile("input")
sizes=defaultdict(int)
stack = []
for l in list:
    match l.split():
        case [_, _, "/"]:
            stack = []
        case [_, _, ".."]:
            stack.pop()
        case [_, _, b]:
            print(l)
            stack.append(b)
        case [a, _] if a.isdigit():
            for i in range(len(stack) + 1):
                path = "/" + "/".join(stack[:i])
                sizes[path] += int(a)

pprint(sizes)
print(sum(filter(lambda v: v <= 100000, sizes.values())))
unused = 70000000 - sizes["/"]
need = 30000000 - unused
print(min(filter(lambda v: v >= need, sizes.values())))