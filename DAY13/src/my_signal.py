class MySignal(object):
    def __init__(self):
        self.signal = []
        self.index = 1
        self.root = True
        self.parent = None
        self.children = []
        self.has_children = False
        self.current_items = "X"
        self.current_index = "Y"
        self.add_child()
        self.current_item()

    def add_child(self):
        for signal in self.signal:
            if type(signal) == list:
                child = MySignal()
                child.signal = signal
                child.index = self.index + 1
                self.children.append(child)
                self.has_children = True
                child.root = False
                child.parent = self
                child.add_child()
            else:
                child = MySignal()
                child.signal = signal
                child.root = False
                ####not needed?
                for item in self.signal:
                    if type(item) == list:
                        self.has_children = True
                ####
                child.parent = self
                child.index = self.index + 1
                self.children.append(child)

    def refresh(self):
        self.caught_signal = []
        self.index = 1
        self.root = True
        self.parent = None
        self.children = []
        self.has_children = False
        self.current_items = "X"
        self.add_child()
        self.current_item()
        return self


    def current_item(self):
        if self.has_children:
            child = self.children[0]
            child.current_item()
        else:
            abc = self
            while abc.parent is not None:
                abc = abc.parent
            abc.current_items = self.signal
            abc.current_index = self.index


    def remove_child(self):
        if self.has_children:
            child = self.children[0]
            child.remove_child()
        elif self.signal == []:
            self.parent.signal.pop(0)
            self.parent.children.pop(0)
        elif type(self.signal) == list:
            self.signal.pop(0)
            if self.has_children:
                self.children.pop(0)
            if len(self.signal) == 0:
                self.parent.signal.pop(0)
            return self.signal
        else:
            if len(self.parent.signal) > 1:
                self.parent.signal.pop(0)
                self.parent.children.pop(0)
            else:
                self.parent.signal.pop(0)
                self.parent.children.pop(0)
                self.parent.has_children = False
                if self.parent.root == False:
                    self.parent.remove_child()
            return self.signal


class WinCounter():
    def __init__(self):
        self.index = 1
        self.winner = []
