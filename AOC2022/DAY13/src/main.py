from filereader import readfile
from my_signal import MySignal, WinCounter
from itertools import zip_longest

isfound=False
# ToDO use from itertools import zip_longest and def compare(l, r) -> bool:
#  or make TuDo from statemachine


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
    input_file = "../input/input"
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

    tests_singal = MySignal()
    tests_singal.signal = [[], [[], 4, [[0, 4, 9, 6, 6], 4, [], 5], [[2, 7], [10, 2], [0, 6, 0, 2]],
                                [5, [2, 10, 10, 7], 8, 1, [1, 2, 4, 9]]], [[7, 6, 1], 6, [[], 0]], [10, 3, [4, []]],
                           [[[5], 2, 10], 10, [[9], [1]], [7, 2, [6, 6, 10, 5, 8], [6, 0, 3, 4, 10], 9],
                            [1, [9, 0], [7, 2, 10, 8, 9], 10]]]

    mysingal3 = MySignal()
    mysingal4 = MySignal()
    input = readfile(input_file)
    winnalist = []
    winnaindex = 0
    while len(input) > 0:
        winnaindex +=1
        mysingal3 = MySignal()
        mysingal4 = MySignal()
        mysingal3.signal = ast.literal_eval(input[0])
        mysingal3.refresh()
        mysingal3.current_item_expander()
        input.pop(0)
        mysingal4.signal = ast.literal_eval(input[0])
        mysingal4.refresh()
        mysingal4.current_item_expander()
        input.pop(0)
        separator = input.index("")
        isfound = False
        for i in range(separator + 1):
            input.pop(0)
        while mysingal3.signal != [] and mysingal4.signal != [] and isfound == False:
            print(mysingal3.signal)
            print(mysingal4.signal)
            mysingal3.refresh()
            mysingal3.current_item_expander()
            mysingal3.get_item_expended()
            mysingal4.refresh()
            mysingal4.current_item_expander()
            mysingal4.get_item_expended()
            ll = mysingal3.current_item_expand
            rr = mysingal4.current_item_expand
            print(ll,rr)
            if isinstance(ll, int) and isinstance(rr, int):
                if ll > rr:
                    isfound = True
                if ll < rr:
                    isfound = True
                    winnalist.append(winnaindex)
                if ll==rr:
                    mysingal3.current_items_expanded_remove()
                    mysingal4.current_items_expanded_remove()


            else:
                rrnone = False
                llnone = False
                if isinstance(rr, int):
                    rr = [rr]
                    rrnone=True
                if isinstance(ll, int):
                    ll = [ll]
                    llnone=True
                comparer=(zip_longest(ll,rr,fillvalue=None))
                i=0
                for item in comparer:
                    print(item)
                    if item[0] == None:
                        isfound = True
                        winnalist.append(winnaindex)
                        break
                    if item[1] == None:
                        isfound = True
                        winnalist.append(winnaindex)
                        break
                    if item[0]>item[1]:
                        isfound = True
                        break
                    if item[0] < item[1]:
                        isfound = True
                        winnalist.append(winnaindex)
                        break
                if llnone==True:
                    isfound = True
                    winnalist.append(winnaindex)

                if rrnone==True:
                    isfound = True

                if isfound==False:
                    mysingal3.current_items_expanded_remove()
                    mysingal4.current_items_expanded_remove()






    print(set(winnalist))
    print(sum(set(winnalist)))
    # testii=MySignal()
    # testii.signal=[[9, [[6, 3, 9], 5], 6], [9, 8, [2], []], [7, 7, [3, [], [4, 5, 2], [5], 6], 1, [[0, 0, 0, 0], 1, [0], [0, 2, 0, 9], [5, 3]]], [6, 4, [], [], 7], [[], 5]]
    # testii.current_item_expander()
    # testii.get_item_expended()
    # print(testii.current_item_expand)
    # testii.current_items_expanded_remove()
    # testii.refresh()
    # testii.current_item_expander()
    # testii.get_item_expended()
    #
    # print(testii.current_item_expand)




if __name__ == "__main__":
    main()
