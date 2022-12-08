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
        self.data.append(data)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        indent= ""
        indent += "!__ " * self.get_level()
        print(f"{indent}+ {self.name}")
        print(f"{indent}+ {self.data}")
        print(f"{indent}+ {self.get_sumdata()}")
        for child in self.children:
            child.print_tree()

    def get_sumdata(self):
        data=0
        sumdata=0
        for data2 in self.data:
            data += int(data2)
        for child in self.children:
            data += child.get_sumdata()
        #print(data)
        return data


root = TreeNode("my_harddisk")
root.add_data(148514)
root.add_data(85156)

dir_a  = TreeNode("dir_a")
root.add_child((dir_a))

dir_d  = TreeNode("dir d")
root.add_child((dir_d))

dir_d.add_data(2911660)
dir_d.add_data(2557)

dir_e = TreeNode("dir e")
dir_a.add_child(dir_e)
dir_e.add_data(737225)



print(f"asd {root.get_sumdata()}")
root.print_tree()