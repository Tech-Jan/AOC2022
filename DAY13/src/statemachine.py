import ast

from my_signal import MySignal, WinCounter


class StateMachine:
    def __init__(self):
        self.signal1 = None
        self.signal2 = None
        self.handlers = {}
        self.startstate = None
        self.endstate = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endstate.append(name)

    def run(self, cargo, mysignal1: MySignal, mysignal2: MySignal, wincounter: WinCounter):
        handler = self.handlers[self.startstate]
        while True:
            (newState, cargo) = handler(cargo, mysignal1, mysignal2, wincounter)
            if newState.upper() in self.endstate:
                # executing endstate
                handler = self.handlers[newState.upper()]
                handler(cargo, mysignal1, mysignal2, wincounter)
                if len(cargo) > 0:
                    return cargo
                else:
                    break
            else:
                handler = self.handlers[newState.upper()]


def starting_items(txt: list, mysignal1: MySignal, mysignal2: MySignal, wincounter: WinCounter):
    mysignal1.signal = ast.literal_eval(txt[0])
    mysignal1.refresh()
    mysignal1.current_item()
    txt.pop(0)
    mysignal2.signal = ast.literal_eval(txt[0])
    mysignal2.refresh()
    mysignal2.current_item()
    txt.pop(0)
    newState = "compare_signal"
    return newState, txt


def compare_signal(txt: list, mysignal1: MySignal, mysignal2: MySignal, wincounter: WinCounter):
    print("comparing SIGNAL")
    print(mysignal1.current_items)
    print(mysignal2.current_items)
    if mysignal1.current_items == mysignal2.current_items:
        print("SAME SIGNAL")
        if mysignal1.current_items == [] and mysignal2.current_items == []:
            newState = "win_condition3"
            return newState, txt
        elif mysignal1.has_children and mysignal2.has_children and mysignal1.current_index == mysignal2.current_index:
            newState = "remove_item"
            return newState, txt
        else:
            newState = "win_condition1"
            return newState, txt

        return newState, txt
    else:
        # ToDo: in class MySignal, not only have attribute currentitem,
        #  expand attributes with current parent list if
        #  currentitem is an integer and not a list
        #  this helps for cases where 1 is an int and 2 is an list or viseversa
        ff = ""
        if type(mysignal1.current_items) == int:
            mysignal1.current_items = [mysignal1.current_items]
            abc = mysignal1
            while abc.has_children:
                abc = abc.children[0]
            abc.parent.signal[0] = [abc.signal]
            ff += "int1"
        if type(mysignal2.current_items) == int:
            mysignal2.current_items = [mysignal2.current_items]
            abc = mysignal2
            while abc.has_children:
                abc = abc.children[0]
            abc.parent.signal[0] = [abc.signal]
            ff += "int2"
        if ff == "int1int2":
            newState = "win_condition2"
            return newState, txt
        if mysignal1.current_items == mysignal2.current_items:
            if ff == "int1" and abs(mysignal1.current_index - mysignal2.current_index) > 1:
                wincounter.winner.append(wincounter.index)
                print("SIGNALE1 WON")
                return "endofmachine", txt
            elif ff == "int2" and abs(mysignal1.current_index - mysignal2.current_index) > 1:
                print("SIGNALE1 LOST")
                return "endofmachine", txt
            else:
                wincounter.winner.append(wincounter.index)
                print("SIGNALE1 LOSSSS")
                return "endofmachine", txt

                return "remove_item", txt
        if mysignal1.current_items < mysignal2.current_items:
            wincounter.winner.append(wincounter.index)
            print("SIGNALE1 WON")
            return "endofmachine", txt
        else:
            print("SIGNALE1 LOST")
            return "endofmachine", txt


def win_condition3(txt: list, mysignal1: MySignal, mysignal2: MySignal, wincounter: WinCounter):
    if mysignal1.current_index == mysignal2.current_index:
        return "remove_item", txt
    elif mysignal1.current_index > mysignal2.current_index:
        print("SIGNALE1 LOST")
        return "endofmachine", txt
    else:
        wincounter.winner.append(wincounter.index)
        print("SIGNALE1 WON")
        return "endofmachine", txt


def win_condition2(txt: list, mysignal1: MySignal, mysignal2: MySignal, wincounter: WinCounter):
    if mysignal1.current_items == [] and mysignal1.has_children == False:
        wincounter.winner.append(wincounter.index)
        print("SIGNALE1 WON")
        return "endofmachine", txt
    elif mysignal2.current_items == [] and mysignal1.has_children == True:
        return "endofmachine", txt
    elif mysignal1.current_items == [] or mysignal2.current_items == []:
        if mysignal1.current_items == []:
            wincounter.winner.append(wincounter.index)
            print("SIGNALE1 WON")
            return "endofmachine", txt
        if mysignal2.current_items == []:
            print("SIGNALE1 LOST")
            return "endofmachine", txt
        print("WTTFF WHAT NOW, used exit() in statemachine/wind_condition2")
        exit()
    elif mysignal1.current_items > mysignal2.current_items:
        return "endofmachine", txt
    else:
        wincounter.winner.append(wincounter.index)
        print("SIGNALE1 WON")
        return "endofmachine", txt


def win_condition1(txt: list, mysignal1: MySignal, mysignale2: MySignal, wincounter: WinCounter):
    winner = ""
    if not mysignal1.has_children:
        print("mysignal1outofitems")
        winner += "signal1"
    if not mysignale2.has_children:
        print("mysignals2outofitems")
        winner += "signal2"
    if winner == "signal1":
        wincounter.winner.append(wincounter.index)
        print("SIGNALE1 WON")
        return "endofmachine", txt
    if winner == "signal2":
        print("SIGNALE2 WON")
        return "endofmachine", txt
    else:
        if mysignal1.current_index < mysignale2.current_index:
            wincounter.winner.append(wincounter.index)
            print("SIGNALE1 WONabovenowinner")
            return "endofmachine", txt
        else:
            print("SIGNALE2 WON(abovenowinner)")
            return "endofmachine", txt


def remove_item(txt: list, mysignal1: MySignal, mysignals2: MySignal, wincounter: WinCounter):
    mysignal1.remove_child()
    mysignal1.refresh()
    mysignals2.remove_child()
    mysignals2.refresh()
    newState = "compare_signal"
    print("removing SIGNAL")
    return newState, txt


def endofmachine(txt, mysignal1: MySignal, mysignal2: MySignal, wincounter: WinCounter):
    wincounter.index += 1
    separator = txt.index("")
    for i in range(separator + 1):
        txt.pop(0)
