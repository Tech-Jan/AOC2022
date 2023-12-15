RESULT1 = []
RESULT2 = []


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.data = []
        self.parent = None
        self.level = 0
        self.totalsum = 0
        self.totalsum2 = 0

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
        abc = 0
        currentlevel = self.get_level()
        emptystring = "!__" * currentlevel
        print(f"{emptystring}{self.name}")
        print(f"{emptystring}{self.get_sum()}")
        # if self.get_sum() <10000:
        #     abc+=self.get_sum()
        for data in self.data:
            print(f"{emptystring}[{data}]")
        for child in self.children:
            child.print_tree()
        return (abc)

    def get_sum(self):
        self.totalsum = 0
        for item in self.data:
            kilobyte = int(item.split(" ")[0])
            self.totalsum += kilobyte
        for child in self.children:
            self.totalsum += child.get_sum()
        # if self.totalsum > 8690120:
        #     print(self.totalsum)
        return self.totalsum

    def get_sum10000(self):

        self.totalsum2 = 0
        for child in self.children:
            a = child.get_sum()
            if a <= 100000:
                RESULT1.append(a)
            child.get_sum10000()
        return RESULT1

    def get_highfoldersize(self, searched_size):
        self.totalsum = 0
        for item in self.data:
            kilobyte = int(item.split(" ")[0])
            self.totalsum += kilobyte
        for child in self.children:
            self.totalsum += child.get_highfoldersize(searched_size)[0]
        if self.totalsum > searched_size:
            # print(self.totalsum)
            RESULT2.append(self.totalsum)
            # print(RESULT2)
        return self.totalsum, RESULT2
