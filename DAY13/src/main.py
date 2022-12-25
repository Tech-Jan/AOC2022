from DAY13.src.statemachine import *
from filereader import readfile
from my_signal import MySignal, WinCounter


# ToDO use from itertools import zip_longest and def compare(l, r) -> bool:
# or make TuDo from statemachine


def create_machine(m, input):
    m.add_state("Starting_items", starting_items)
    m.add_state("compare_signal", compare_signal)
    m.add_state("remove_item", remove_item)
    m.add_state("win_condition1", win_condition1)
    m.add_state("win_condition2", win_condition2)
    m.add_state("win_condition3", win_condition3)
    m.add_state("Endofmachine", endofmachine, end_state=1)
    m.startstate = "STARTING_ITEMS"


def main():
    input_file = "..\input\\input"
    input = readfile(input_file)
    m = StateMachine()
    wincounter = WinCounter()
    mysignal1 = MySignal()
    mysignal2 = MySignal()
    create_machine(m, input)
    while input is not None:
        input = m.run(input, mysignal1, mysignal2, wincounter)
        print(mysignal1.signal)
        print(mysignal2.signal)
        print(f"wincounter index= {wincounter.index}")

    print(f"wincounter winners= {wincounter.winner}")
    print(sum(wincounter.winner))


if __name__ == "__main__":
    main()
