import filereader
from harddisktree import TreeNode

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
