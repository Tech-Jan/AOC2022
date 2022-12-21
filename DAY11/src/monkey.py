def add(value1, value2):
    return value1 + value2


def multipy(value1, value2):
    return value1 * value2


def substract(value1, value2):
    return value1 - value2


class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.operation = ""
        self.operators = {
            "+": add,
            "-": substract,
            "*": multipy,
        }
        self.worry_level = 0,
        self.diviser = 0,
        self.targets = []
        self.inspections = 0
        self.worry_divisor = 3

    def operations(self, ):
        my_operation = self.operation.split()
        operator = my_operation[1]
        value1 = my_operation[0]
        value2 = my_operation[2]
        value1 = self.transform_old(value1)
        value2 = self.transform_old(value2)
        value = self.operators[operator](value1, value2)
        self.worry_level = value // self.worry_divisor
        return value // self.worry_divisor

    def transform_old(self, value):
        if value == "old":
            value = self.items[0]
        return int(value)
