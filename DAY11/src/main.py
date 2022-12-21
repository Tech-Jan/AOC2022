from DAY11.src.filereader import readfile
from DAY11.src.statemachine import *
import argparse


def create_machine(m, monkey_list):
    m.add_state("Add_monkey", add_monkey, monkey_list)
    m.add_state("Starting_items", starting_items, monkey_list)
    m.add_state("Operation", operation, monkey_list)
    m.add_state("test", divisor, monkey_list)
    m.add_state("get_targets", get_targets, monkey_list)
    m.add_state("Endofmachine", endofmachine, monkey_list, end_state=1)
    m.startstate = "ADD_MONKEY"


def inspection_counter_p1(monkey_list):
    for monkey in monkey_list:
        for j in range(len(monkey.items)):
            item = monkey.operations()
            monkey.items.pop(0)
            monkey.inspections += 1
            if item % monkey.diviser == 0:
                monkey_list[monkey.targets[0]].items.append(item)
            else:
                monkey_list[monkey.targets[1]].items.append(item)


def inspection_counter_p2(monkey_list):
    mod_all = 1
    for monkey in monkey_list:
        mod_all *= monkey.diviser
        monkey.worry_divisor = 1
    for monkey in monkey_list:
        for j in range(len(monkey.items)):
            item = monkey.operations()
            monkey.items.pop(0)

            if item % monkey.diviser == 0:
                item = item % mod_all
                monkey_list[monkey.targets[0]].items.append(item)
            else:
                monkey_list[monkey.targets[1]].items.append(item)
            monkey.inspections += 1


def main():
    input_file = "input"
    # parser = argparse.ArgumentParser()
    # parser.add_argument("echo")
    # args = parser.parse_args()
    # print(args.echo)

    input_var = readfile(input_file)
    monkey_list_p1 = []
    m = StateMachine()
    create_machine(m, monkey_list_p1)

    while input_var is not None:
        input_var = m.run(input_var)

    for i in range(20):
        inspection_counter_p1(monkey_list_p1)

    inspections = sorted([monkey.inspections for monkey in monkey_list_p1], reverse=True)
    print("part1 ", inspections[0] * inspections[1])

    # START PART 2

    input_var = readfile(input_file)
    monkey_list_p2 = []
    m2 = StateMachine()
    create_machine(m2, monkey_list_p2)

    while input_var is not None:
        input_var = m2.run(input_var)

    for i in range(10000):
        inspection_counter_p2(monkey_list_p2)

    inspections = sorted([monkey.inspections for monkey in monkey_list_p2], reverse=True)
    print("part2 ", inspections[0] * inspections[1])


if __name__ == '__main__':
    main()
