from json.scanner import NUMBER_RE

from tools import reader
from tools.printer import Printer
import time


class Hard_disk:
    def __init__(self, input):
        self.code_raw = input
        self.signal = []
        self.signal2 = []
        # self.turn_to_signal()
        self.turn_to_signal2()
        # self.compress()
        self.current_place = 0

    def turn_to_signal2(self):
        switch = 1
        counter = 0
        next_line = ""
        for number in self.code_raw:
            if switch == 1:
                next_line = int(number), counter
                self.signal2.append(next_line)
                counter += 1
            else:
                if int(number) != 0:
                    next_line = int(number), "."
                    self.signal2.append(next_line)
            switch *= -1

    def turn_to_signal(self):
        switch = 1
        counter = 0

        for number in self.code_raw:
            if switch == 1:
                for i in range(int(number)):
                    self.signal.append(counter)
                counter += 1
            else:
                if int(number) != 0:
                    for i in range(int(number)):
                        self.signal.append(".")
            switch *= -1

    def freespace_find(self):
        freespace = self.signal.index('.')
        return freespace

    def compress(self):
        lengt = len(self.signal)
        freespace_location = self.freespace_find()
        for place, data in enumerate(reversed(self.signal)):

            if freespace_location < lengt - place - 2:
                freespace_location = self.freespace_find()
                if data != '.':
                    self.signal[freespace_location] = data
                    self.signal[-place - 1] = "."

            # print(self.signal)

    def find_space2(self, space):
        for place, [freespace, item] in enumerate(self.signal2):
            if freespace >= space and item == '.':
                return place,freespace-space

        return -1,-1

    def compress2(self):
        ##
        #todo correct this problem ist er macht immermehr sachen hinzufügen und so inside self.signal2
        for place, [space, data] in enumerate(reversed(self.signal2)):
            if data!='.':
                freespace,space_left = self.find_space2(space)
                if freespace !=-1:
                    self.signal2[freespace]=(space,data)
                    self.signal2[-place-1]=(space_left,'.')
                    if space_left>0:
                        self.signal2.insert(freespace+1,(space_left,'.'))

            print(place, space, data, freespace)


    def counter(self):
        entire = 0
        for i, data in enumerate(self.signal):
            if data != '.':
                entire += i * data
        print(entire)


def main():
    my_harddisk = Hard_disk(reader.read_input(2)[0])
    # print(my_harddisk.signal)
    # my_harddisk.compress()
    # print(my_harddisk.signal)
    print(my_harddisk.signal2)
    my_harddisk.compress2()
    print(my_harddisk.signal2)

if __name__ == "__main__":
    main()
