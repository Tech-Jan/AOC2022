from DAY11.src.monkey import Monkey


class StateMachine:
    def __init__(self):
        self.monkey_list = None
        self.handlers = {}
        self.startstate = None
        self.endstate = []

    def add_state(self, name, handler, monkey_list, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        self.monkey_list = monkey_list
        if end_state:
            self.endstate.append(name)

    def run(self, cargo):
        handler = self.handlers[self.startstate]
        while True:
            try:
                handler(cargo)
            except TypeError:
                (newState, cargo) = handler(cargo, self.monkey_list)
            else:
                (newState, cargo) = handler(cargo)
            if newState.upper() in self.endstate:
                # executing endstate
                handler = self.handlers[newState.upper()]
                handler(cargo)
                if len(cargo) > 0:
                    return cargo
                else:
                    print("Monkeys created and equiped. All monkeys are in monkey_list_pX")
                    break
            else:
                handler = self.handlers[newState.upper()]


def add_monkey(txt, monkey_list):
    splitted_txt = txt[0].split(":", 1)
    word = splitted_txt[0]
    txt.pop(0)
    if word[0:6] == "Monkey":
        newState = "starting_items"
        my_monkey = Monkey(word)
        monkey_list.append(my_monkey)
    else:
        newState = "error_state"
    return newState, txt


def starting_items(txt, monkey_list):
    splitted_txt = txt[0].split(":", 1)
    word, items = splitted_txt
    items = items.split(",")
    items = [int(item) for item in items]
    txt.pop(0)
    word = word.lstrip()
    if word == "Starting items":
        newState = "Operation"
        monkey_list[-1].items = items
    else:
        newState = "error_state2"
    return newState, txt


def operation(txt, monkey_list):
    splitted_txt = txt[0].split(":", 1)
    word, operation_var = splitted_txt
    operation_var = operation_var.split("=")
    txt.pop(0)
    word = word.lstrip()

    if word == "Operation":
        newState = "test"
        monkey_list[-1].operation = operation_var[1]
        monkey_list[-1].operations()
    else:
        newState = "error_state3"
    return newState, txt


def divisor(txt, monkey_list):
    splitted_txt = txt[0].split(":", 1)
    word, operation_var = splitted_txt
    diviser = operation_var.split()[2]
    txt.pop(0)
    word = word.lstrip()
    if word == "Test":
        newState = "get_targets"
        monkey_list[-1].diviser = int(diviser)
    else:
        newState = "error_state"
    return newState, txt


def get_targets(txt, monkey_list):
    splitted_txt = txt[0].split(":", 1)
    word, operation_var = splitted_txt
    word = word.lstrip()
    txt.pop(0)
    target = None
    if word == "If true":
        target = operation_var.split()[-1]
        newState = "get_targets"
    elif word == "If false":
        target = operation_var.split()[-1]
        newState = "endofmachine"
    else:
        newState = "error_state"

    monkey_list[-1].targets.append(int(target))
    return newState, txt


def endofmachine(txt):
    separator = txt.index("")
    for i in range(separator + 1):
        txt.pop(0)
