class TreeNode:
    def __init__(self, name):
        self.name = name
        self.data = []
        self.children = []
        self.parent = None
        self.sumdata = self.get_sumdata()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def add_data(self, data):
        test = self.name
        print(test)
        self.data.append(data)
        self.sumdata = self.get_sumdata()
        if self.parent != None:
            # self.parent.sumdata = self.parent.get_sumdata()
            test = self.parent.name
            self.parent.add_data(0)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            print(p.name)
            p = p.parent
        return level

    def print_tree(self):
        indent = ""
        indent += "!__ " * self.get_level()
        print(f"{indent}+ {self.name}")
        print(f"{indent}+ {self.data}")
        print(f"{indent}+ {self.get_sumdata()}")
        for child in self.children:
            child.print_tree()

    def get_sumdata(self):
        data = 0
        for data2 in self.data:
            data += int(data2)
        for child in self.children:
            data += child.get_sumdata()
        # print(data)
        return data

    def print_sum(self):
        print(self.get_sumdata())
        for child in self.children:
            child.print_sum()


root = TreeNode("my_harddisk")

root.add_data(148514)
root.add_data(85156)

dir_a = TreeNode("dir_a")
root.add_child((dir_a))

dir_d = TreeNode("dir d")
root.add_child((dir_d))

dir_d.add_data(2911660)
dir_d.add_data(2557)


dir_e = TreeNode("dir e")
dir_a.add_child(dir_e)
dir_e.add_data(737225)
dir_e.add_data(3223)

dir_f=TreeNode("dir_f")
root.add_child(dir_f)
dir_g=TreeNode("dir_g")
dir_f.add_child(dir_g)
dir_g.add_data(23234)
dir_g.add_data(934)
dir_g.add_data(32)
# dir_f.add_data(1)
# dir_a.add_data(1)

a = "dir lolol"


dir_g.add_child(TreeNode(a))


# print(f"asd {root.get_sumdata()}")
root.print_tree()

print(root.sumdata)
print(dir_d.sumdata)
print(root.get_sumdata())

x = root
for child in x.children:
    if child.name == "dir d":
        y = child

print(y.name)

y = y.parent
print(y.name)

print(dir_e.get_level())

# for child in root.children:
#     print(child.name)
#
