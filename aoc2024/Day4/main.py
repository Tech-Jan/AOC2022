from itertools import count
from operator import index

import reader


class puzzle:
    def __init__(self, rooster: list):
        self.rooster: list[list[str]] = rooster
        self.rooster_width: int = len(self.rooster[0])
        self.rooster_heigth: int = len(self.rooster)
        self.vertical: list[str] = self.turn_to_string(self.transform_vertical())
        self.diagonal_tl_br: list[str] = self.turn_to_string(self.transform_diagonal_tl_br())
        self.diagonal_bl_tr: list[str] = self.turn_to_string(self.transform_diagonal_bl_tr())
        self.horizontal: list[str] = self.turn_to_string(self.rooster)
        self.keyword_tl_br=[]
        self.keyword_bl_tr=[]
        self.keyword_bl_tr_quader=[]
        self.keyword_tl_br_quader=[]

    def func(self):
        pass

    def turn_to_string(self, table):
        table_str = []
        stroutput = ""
        for line in table:
            for letter in line:
                stroutput += letter
            table_str.append(stroutput)
            stroutput = ""
        return table_str

    def printer(self, prints):
        prints_str = self.turn_to_string(prints)
        for line in prints_str:
            print(line)

    def transform_vertical(self):
        vertical = [[] for x in range(len(self.rooster))]
        for column in self.rooster:
            for row in range(len(column)):
                vertical[row].append(column[row])

        return vertical

    def count(self, table: list[str]):
        keyword = "XMAS"
        total_count = 0
        for line in table:
            founds = line.count(keyword)
            total_count += founds
        return total_count

    def reverser(self, table: list[str]):
        table_reversed: list[str] = []
        for line in table:
            table_reversed.append(list(reversed(line)))
        table_reversed_str = self.turn_to_string(table_reversed)
        return table_reversed_str

    def counter_part1(self):
        horizontal = self.count(self.horizontal)
        horizontal_r = self.count(self.reverser(self.horizontal))
        verticals = self.count(self.vertical)
        verticals_r = self.count(self.reverser(self.vertical))
        diagonals_tl_br = self.count(self.diagonal_tl_br)
        diagonals_tl_br_r = self.count(self.reverser(self.diagonal_tl_br))
        diagonals_bl_tr = self.count(self.diagonal_bl_tr)
        diagonals_bl_tr_r = self.count(self.reverser(self.diagonal_bl_tr))
        total = (horizontal + horizontal_r + verticals + verticals_r +
                 diagonals_tl_br + diagonals_tl_br_r + diagonals_bl_tr + diagonals_bl_tr_r)
        print(f"total={total}, "
              f"h {horizontal}, "
              f"h_r {horizontal_r}, "
              f"v {verticals}, "
              f"v_r {verticals_r}, "
              f" d_tlbr {diagonals_tl_br},"
              f" d_tlbr_r {diagonals_tl_br_r}, "
              f"d_bltr {diagonals_bl_tr}, "
              f"d_bltr_r {diagonals_bl_tr_r}")
        return total

    def transform_diagonal_tl_br(self):
        diagonal = [[] for x in range(self.rooster_heigth + self.rooster_width)]
        for column_count in range(self.rooster_heigth + 1):
            for i in range(column_count):
                x = i
                y = column_count - i - 1
                c = column_count - 1
                diagonal[column_count - 1].append(self.rooster[y][x])
        for row_count in range(self.rooster_width):
            for column_count in range(row_count):
                x = self.rooster_width - row_count + column_count
                y = self.rooster_heigth - column_count - 1
                c = self.rooster_heigth + self.rooster_width - row_count - 1
                diagonal[self.rooster_heigth + self.rooster_width - row_count - 1].append(self.rooster[y][x])

        return diagonal

    def transform_diagonal_bl_tr(self):
        diagonal = [[] for x in range(self.rooster_heigth + self.rooster_width)]

        for column_count in range(self.rooster_heigth, -1, -1):
            for i in range(self.rooster_heigth - column_count):
                x = i
                y = column_count + i
                diagonal[self.rooster_heigth - column_count - 1].append(self.rooster[y][x])
        for row_count in range(self.rooster_width - 1, 0, -1):
            for column_count in range(self.rooster_width - row_count):
                x = row_count + column_count
                y = column_count
                diagonal[self.rooster_heigth + row_count - 1].append(self.rooster[y][x])

        return diagonal

    def get_x_line(self, line, keyword):
        x_coord = []
        pos = 0
        while True:
            x = line.find(keyword, pos)
            if x != -1:
                x_coord.append(x+1)
            pos += x+len(keyword)
            if x == -1:
                return x_coord

    def klappauf_x(self,x_list:list,y:int,coords):

        for x in x_list:
            coords.append([x,y])
        return coords

    def x_max_search(self):
        keywords = ["MAS","SAM"]
        pos_tl_br = []
        pos_bl_tr = []
        for y, value in enumerate(self.diagonal_tl_br):
            for keyword in keywords:
                x_list=list(self.get_x_line(value,keyword))
                pos_tl_br=self.klappauf_x(x_list,y,pos_tl_br)
            #print(f"x={x},y={y}")
            #print(pos)
        for y, value in enumerate(self.diagonal_bl_tr):
            for keyword in keywords:
                x_list=list(self.get_x_line(value,keyword))
                pos_bl_tr=self.klappauf_x(x_list,y,pos_bl_tr)
        print("pos_tl_br  ", pos_tl_br)
        print("pos_bl_tr  ",pos_bl_tr)

        self.keyword_tl_br=pos_tl_br
        self.keyword_bl_tr=pos_bl_tr

    def counter_part2(self):
        counts=0
        new=[]
        for xy1 in self.keyword_tl_br_quader:
            for xy2 in self.keyword_bl_tr_quader:
                if xy1==xy2:
                    counts+=1
                    new.append(xy1)

        fuck=[]
        for y in range(10):
            kk=""
            for x in range(10):
                if [x,y] in new:
                    kk+="A"
                else:
                    kk+="."
            fuck.append(kk)
        self.printer(fuck)

        print(f"part2 {counts}")

    def coordinate_transfomer_tl_br(self, old_coordinates):
        new_coordinates=[]
        for old_coordinate in old_coordinates:
            x_old=old_coordinate[0]
            y_old=old_coordinate[1]
            if y_old<self.rooster_heigth:
                y_new=y_old-x_old
                x_new=x_old
                new_coordinates.append([x_new, y_new])
                #new_coordinates.append([x_new,y_new,x_old,y_old])
            else:
                y_new=self.rooster_heigth-1-x_old
                x_new=y_old-self.rooster_heigth +1+x_old
                new_coordinates.append([x_new, y_new])
                #new_coordinates.append(["BIG",x_new,y_new,x_old,y_old])
        print(new_coordinates)
        self.keyword_tl_br_quader=new_coordinates

    def coordinate_transfomer_bl_tr(self, old_coordinates):
        new_coordinates = []
        for old_coordinate in old_coordinates:
            x_old = old_coordinate[0]
            y_old = old_coordinate[1]
            if y_old < self.rooster_heigth:
                y_new = self.rooster_heigth-1 - y_old + x_old
                x_new = x_old
                #new_coordinates.append([x_new, y_new, x_old, y_old])
                new_coordinates.append([x_new, y_new])
            else:
                y_new = x_old
                x_new =   y_old - self.rooster_heigth + 1 + x_old

                #new_coordinates.append(["BIG", x_new, y_new, x_old, y_old])
                new_coordinates.append([x_new, y_new])
        print(new_coordinates)
        self.keyword_bl_tr_quader=new_coordinates

def main():
    input = reader.read_input(2)
    puzzle_1 = puzzle(input)
    # puzzle_1.printer(puzzle_1.rooster)
    # puzzle_1.printer(puzzle_1.vertical)
    # puzzle_1.printer(puzzle_1.diagonal_tl_br)
    puzzle_1.printer(puzzle_1.diagonal_bl_tr)
    puzzle_1.x_max_search()
    puzzle_1.coordinate_transfomer_tl_br(puzzle_1.keyword_tl_br)
    puzzle_1.coordinate_transfomer_bl_tr(puzzle_1.keyword_bl_tr)
    puzzle_1.counter_part1()
    puzzle_1.counter_part2()
    print("end")

    #test
    roos=[]
    for y in range(10):
        xrow=[]
        for x in range(10):
           xrow.append([x,y])
        roos.append(xrow)

    print(roos)

    print(roos[5][3])

    #489 to low
    #595 to low
    #1908??

if __name__ == "__main__":
    main()
