from dataclass import Storage, MovePlan
from Crane import Crane
import pprint
import time
import os

storage = Storage("/home/jew/PycharmProjects/day5 OOP/extendedcrates")
storage.storeheight = 45
storage.floorlevel = 1
move_list = MovePlan("/home/jew/PycharmProjects/day5 OOP/day5moves")
crane9000 = Crane(storage, "9000")
pp = pprint.PrettyPrinter(width=250)

pp.pprint(storage.shelf)

# this turns the list into a random lsit where the moves fit the storage width
mylist = move_list.datamovelistcreator(storage)
# print(mylist)


for move in mylist:
    amount = int(move[0])
    fromwhere = int(move[1]) - 1
    towhere = int(move[2]) - 1
    crane9000.movebox(amount, fromwhere, towhere)
    pp.pprint(storage.shelf)
    print("!###############################################################################################!")
    pp.pprint(len(storage.shelf))
    time.sleep(0.08)
    os.system('clear')

storage2 = Storage("/home/jew/PycharmProjects/day5 OOP/day5crates")
# need +- 50 to pull of the AOC day5 quest
storage2.storeheight = 50
crane9001 = Crane(storage2, "9001")
move_list2 = MovePlan("/home/jew/PycharmProjects/day5 OOP/day5moves")
move_list23 = move_list.datamovelistcreator(storage2)

for move in move_list2.movelist:
    # for move in move_list23:
    amount = int(move[0])
    fromwhere = int(move[1]) - 1
    towhere = int(move[2]) - 1
    crane9001.movebox(amount, fromwhere, towhere)
    pp.pprint(storage2.shelf)
    print("!##############################################!")
    time.sleep(0.08)
    os.system('clear')

pp.pprint(storage2.shelf)
# print(crane9001.move_box)
