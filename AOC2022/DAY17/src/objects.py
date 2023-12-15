import numpy as np


class filereader():
    def __init__(self):
        self.input = self.read_input()

    def read_input(self):
        with open("../input/input", "r") as f:
            data = f.read()
            data_int = []
            for sign in data:
                if sign == "<":
                    data_int.append(-1)
                elif sign == ">":
                    data_int.append(1)
                else:
                    print("error parsing data")
                    exit()
            return data_int


class stones():
    def __init__(self):
        self.stone0 = np.array([1, 1, 1, 1])
        self.stone1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
        self.stone2 = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
        self.stone3 = np.array([[1], [1], [1], [1]])
        self.stone4 = np.array([[1, 1], [1, 1]])
        self.objects = [self.stone0, self.stone1, self.stone2, self.stone3, self.stone4]
        self.current_object = self.stone0
        self.current_pos = [0, 0]


class map():
    def __init__(self):
        self.landscape = np.array(np.ones(7))

    def add_object(self, ston: stones):
        if len(ston.current_object.shape) == 1:
            self.landscape = np.vstack([np.zeros((4, 7)), self.landscape])
            for i in range(len(ston.current_object)):
                if ston.current_object[i] == 1:
                    self.landscape[0, 2 + i] += ston.current_object[i]

        if len(ston.current_object.shape) == 2:
            self.landscape = np.vstack([np.zeros((3, 7)), self.landscape])
            height = ston.current_object.shape[1]
            if height == 1:
                height = 4

            self.landscape = np.vstack(
                [np.zeros((height, 7)), self.landscape])
            for i in range(len(ston.current_object)):
                for j in range(len(ston.current_object[i])):
                    if ston.current_object[i][j] == 1:
                        self.landscape[0 + i, 2 + j] += ston.current_object[i][j]
        ston.current_pos = [0, 2]

    def move(self, ston: stones, move: list):
        test_landscape = self.landscape.copy()

        try:
            if len(ston.current_object.shape) == 1:
                self.move1d(ston, move)

            if len(ston.current_object.shape) == 2:
                self.move2d(ston, move)

        except:
            #print("crahsleftorright")
            self.landscape = test_landscape
            return True

        if 2 in self.landscape:
            #rollback
            self.landscape = test_landscape
            if move == [1, 0]:
                #fell down. it stops moving
                return False
            else:
                #it just bumped against corner while moving left or right. needs to fall down to stop
                return True

        ston.current_pos[0] += move[0]
        ston.current_pos[1] += move[1]
        if ston.current_pos[1] < 0:
            ston.current_pos[1] = 0
        return True

    def move1d(self, ston: stones, move: list):

        for i in range(len(ston.current_object)):
            if ston.current_pos[1] + 0 + move[1] < 0:
                #stop it from escaping to the left
                break
            if ston.current_object[i] == 1:
                self.landscape[ston.current_pos[0], ston.current_pos[1] + i] -= ston.current_object[i]
                self.landscape[ston.current_pos[0] + move[0], ston.current_pos[1] + i + move[1]] += ston.current_object[
                    i]

    def move2d(self, ston: stones, move: list):
        for i in range(len(ston.current_object)):
            if ston.current_pos[1] + 0 + move[1] < 0:
                # stop it from escaping to the left
                break
            for j in range(len(ston.current_object[i])):
                if ston.current_object[i][j] == 1:
                    self.landscape[ston.current_pos[0] + i, ston.current_pos[1] + j] -= ston.current_object[i][j]
                    self.landscape[ston.current_pos[0] + i + move[0], ston.current_pos[1] + j + move[1]] += \
                        ston.current_object[i][j]
