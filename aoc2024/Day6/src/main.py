from tools import reader
from tools.printer import Printer
import time


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.maze_orig=maze.copy()
        self.lenx_maze = len(maze[0])
        self.leny_maze = len(maze)
        self.watcher_pos = self.find_watcher()
        self.watcher_dir = (0 - 1j)
        self.stones_pos = self.find_stones(self.maze)
        self.move_possible = True
        self.extra_stone_possible = True
        self.extra_stone = (0 + 0j)
        self.move_counts = 0
        self.stone_counts = 0

    def maze_reset(self):
        self.maze=self.maze_orig.copy()
        self.watcher_dir=(0 - 1j)
        self.watcher_pos =self.find_watcher()
        self.move_possible=True
        self.move_counts=0

    def turn_r(self):
        self.watcher_dir = self.watcher_dir * (1j)

    def turn_l(self):
        self.watcher_dir = self.watcher_dir * (1j) ** 3

    def move(self):
        self.move_mark()
        self.move_check()
        # Printer(self.maze, self.get_xy(self.watcher_pos), 5).printer2()
        # time.sleep(0.5)

    def move_check(self):
        next_pos = self.watcher_dir + self.watcher_pos

        if next_pos in self.stones_pos:
            self.turn_r()
        else:
            self.watcher_pos = next_pos

    def get_xy(self, coords: complex):
        y = int(coords.imag)
        x = int(coords.real)
        return x, y

    def count_X(self):
        count = 0
        for line in self.maze:
            for letter in line:
                if letter == "X":
                    count += 1
        print(count)

    def move_mark(self):
        x, y = self.get_xy(self.watcher_pos)
        if x >= 0 and x <= len(self.maze[0]) and y >= 0 and y <= len(self.maze) - 1:
            self.maze[y] = self.maze[y][:x] + 'X' + self.maze[y][x + 1:]
            self.move_counts += 1
            #print(self.move_counts)
            if self.move_counts > 10000:
                self.stone_counts += 1
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                self.move_possible = False

        else:
            self.move_possible = False

    def find_stones(self,maze):
        stones = []
        for y, line in enumerate(maze):
            for x, letter in enumerate(line):
                if letter in ['#', 'O']:
                    stones.append(complex(x, y))
        return stones

    def find_watcher(self):
        for y, line in enumerate(self.maze):
            for x, letter in enumerate(line):
                if letter == '^':
                    return (complex(x, y))

    def put_stone(self):
        x_stone, y_stone = self.get_xy(self.extra_stone)
        self.maze = self.maze_orig.copy()
        self.maze[y_stone] = self.maze[y_stone][:x_stone] + 'O' + self.maze[y_stone][x_stone + 1:]


    def move_stone(self):
        x_stone, y_stone = self.get_xy(self.extra_stone)
        if x_stone >= 0 and x_stone < self.lenx_maze - 1:
            self.extra_stone += (1 + 0j)
            self.put_stone()
            self.stones_pos= self.find_stones(self.maze)
        elif y_stone >= 0 and y_stone < self.lenx_maze - 1:
            self.extra_stone = complex(0 + (y_stone + 1) * 1j)
            self.put_stone()
            self.stones_pos= self.find_stones(self.maze)
        else:
            self.extra_stone_possible = False


def main():
    clyde = reader.read_input(1)
    Printer(clyde, (9, 7), 5).printer2()
    my_maze = Maze(clyde)
    Printer(my_maze.maze, (9, 7), 5).printer2()
    print("posstart", my_maze.watcher_pos)

    while my_maze.move_possible:
        my_maze.move()
    my_maze.count_X()
    print(my_maze.move_counts)
    my_maze.put_stone()
    Printer(my_maze.maze, (9, 7), 5).printer2()
    my_maze.move_stone()
    while my_maze.extra_stone_possible:
        while my_maze.move_possible:
            my_maze.move()
        # time.sleep(0.1)
        my_maze.move_stone()
        my_maze.maze_reset()

        #Printer(my_maze.maze).printer2()
        print(my_maze.extra_stone)
    print(my_maze.stone_counts)
    # 5106 to high


if __name__ == "__main__":
    main()
