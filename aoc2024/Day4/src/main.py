from aoc2024.Day4.src import za
from aoc2024.Day4.src import reader

# case1=real case2=test
case = 1


class Puzzle:
    def __init__(self, rooster: list):
        self.rooster: list[list[str]] = rooster
        self.rooster_width: int = len(self.rooster[0])
        self.rooster_height: int = len(self.rooster)
        self.vertical: list[str] = self.turn_to_string(self.transform_vertical())
        self.vertical_r = self.reverser(self.vertical)
        self.diagonal_tl_br: list[str] = self.turn_to_string(self.transform_diagonal_tl_br())
        self.diagonal_tl_br_r = self.reverser(self.diagonal_tl_br)
        self.diagonal_bl_tr: list[str] = self.turn_to_string(self.transform_diagonal_bl_tr())
        self.diagonal_bl_tr_r = self.reverser(self.diagonal_bl_tr)
        self.horizontal: list[str] = self.turn_to_string(self.rooster)
        self.horizontal_r = self.reverser(self.horizontal)
        self.directions_dict = {"vertical": self.vertical,
                                "vertical_r": self.vertical_r,
                                "horizontal": self.horizontal,
                                "horizontal_r": self.horizontal_r,
                                "diagonal_tl_br": self.diagonal_tl_br,
                                "diagonal_tl_br_r": self.diagonal_tl_br_r,
                                "diagonal_bl_tr": self.diagonal_bl_tr,
                                "diagonal_bl_tr_r": self.diagonal_bl_tr_r}
        self.keyword_tl_br = self.x_max_search(self.diagonal_tl_br)
        self.keyword_bl_tr = self.x_max_search(self.diagonal_bl_tr)
        self.keyword_bl_tr_quader = self.coordinate_transfomer_bl_tr(self.keyword_bl_tr)
        self.keyword_tl_br_quader = self.coordinate_transformer_tl_br(self.keyword_tl_br)
        self.keyword_dict = {"keyword_tl_br": self.keyword_tl_br,
                             "keyword_bl_tr": self.keyword_bl_tr,
                             "self.keyword_bl_tr_quader": self.keyword_bl_tr_quader,
                             "self.keyword_tl_br_quader": self.keyword_tl_br_quader}
        self.res_part2 = self.counter_part2_do()

    def func(self):
        pass

    @staticmethod
    def turn_to_string(table):
        table_str = []
        str_output = ""
        for line in table:
            for letter in line:
                str_output += letter
            table_str.append(str_output)
            str_output = ""
        return table_str

    def printer(self, prints):
        prints_str = self.turn_to_string(prints)
        for line in prints_str:
            print(line)

    def transform_vertical(self):
        vertical = [[] for _x in range(len(self.rooster))]
        for column in self.rooster:
            for row in range(len(column)):
                vertical[row].append(column[row])

        return vertical

    @staticmethod
    def count(table: list[str]):
        keyword = "XMAS"
        total_count = 0
        for line in table:
            founds = line.count(keyword)
            total_count += founds
        return total_count

    def reverser(self, table: list[str]):
        table_reversed: list[list[str]] = []
        for line in table:
            table_reversed.append(list(reversed(line)))
        table_reversed_str = self.turn_to_string(table_reversed)
        return table_reversed_str

    def get_count(self, mylist: list) -> int:
        return self.count(mylist)

    def counter_part1(self):
        total_str = ""
        total_count = 0
        for key, value in self.directions_dict.items():
            counting = self.count(value)
            total_str += f"{key}: {counting}, "
            total_count += counting
        total_str = f"total: {total_count}, " + total_str
        print(total_str)
        return total_count

    def transform_diagonal_tl_br(self):
        diagonal = [[] for _x in range(self.rooster_height + self.rooster_width)]
        for column_count in range(self.rooster_height + 1):
            for i in range(column_count):
                x = i
                y = column_count - i - 1
                _c = column_count - 1
                diagonal[column_count - 1].append(self.rooster[y][x])
        for row_count in range(self.rooster_width):
            for column_count in range(row_count):
                x = self.rooster_width - row_count + column_count
                y = self.rooster_height - column_count - 1
                _c = self.rooster_height + self.rooster_width - row_count - 1
                diagonal[self.rooster_height + self.rooster_width - row_count - 1].append(self.rooster[y][x])
        return diagonal

    def transform_diagonal_bl_tr(self):
        diagonal = [[] for _x in range(self.rooster_height + self.rooster_width)]
        for column_count in range(self.rooster_height, -1, -1):
            for i in range(self.rooster_height - column_count):
                x = i
                y = column_count + i
                diagonal[self.rooster_height - column_count - 1].append(self.rooster[y][x])
        for row_count in range(self.rooster_width - 1, 0, -1):
            for column_count in range(self.rooster_width - row_count):
                x = row_count + column_count
                y = column_count
                diagonal[self.rooster_height + row_count - 1].append(self.rooster[y][x])
        return diagonal

    @staticmethod
    def get_x_line( line, keyword):
        x_coord = []
        pos = 0
        while True:
            x = line.find(keyword, pos)
            if x != -1:
                x_coord.append(x + 1)
            pos = x + 1
            if x == -1:
                return x_coord

    @staticmethod
    def klappauf_x( x_list: list, y: int, coords):
        for x in x_list:
            coords.append([x, y])

    def x_max_search(self, mydiagonal: list):
        keywords = ["MAS", "SAM"]
        mydiagonal_hits = []
        for y, value in enumerate(mydiagonal):
            for keyword in keywords:
                x_list = list(self.get_x_line(value, keyword))
                self.klappauf_x(x_list, y, mydiagonal_hits)
        return mydiagonal_hits

    def show_hits(self, hits):
        fuck = []
        for y in range(self.rooster_height):
            kk = ""
            for x in range(self.rooster_width):
                if (x, y) in hits:
                    kk += "A"
                else:
                    kk += "."
            fuck.append(kk)
        self.printer(fuck)

    def counter_part2_do(self):
        counts = 0
        new = []
        new_list = []
        for xy1 in self.keyword_tl_br_quader:
            for xy2 in self.keyword_bl_tr_quader:
                if xy1 == xy2:
                    counts += 1
                    new.append(tuple(xy1))
                    new_list.append(xy1)
        return new

    def counter_part2(self):
        self.show_hits(self.res_part2)
        # print(self.res_part2)
        res2 = za.main(case)
        added = []
        kuku = 0
        for item in self.res_part2:
            for item2 in res2:
                if item == item2:
                    added.append(item)
                    kuku += 1
        lala = list(set(res2) - set(self.res_part2))
        print("similarities  ", kuku, added)
        print("nosimilar", lala)
        print(f"part2 {len(self.res_part2)}")

    def coordinate_transformer_tl_br(self, old_coordinates):
        new_coordinates = []
        for old_coordinate in old_coordinates:
            x_old = old_coordinate[0]
            y_old = old_coordinate[1]
            if y_old < self.rooster_height:
                y_new = y_old - x_old
                x_new = x_old
                new_coordinates.append([x_new, y_new])
                # new_coordinates.append([x_new,y_new,x_old,y_old])
            else:
                y_new = self.rooster_height - 1 - x_old
                x_new = y_old - self.rooster_height + 1 + x_old
                new_coordinates.append([x_new, y_new])
                # new_coordinates.append(["BIG",x_new,y_new,x_old,y_old])
        # print(new_coordinates)
        return new_coordinates

    def coordinate_transfomer_bl_tr(self, old_coordinates):
        new_coordinates = []
        for old_coordinate in old_coordinates:
            x_old = old_coordinate[0]
            y_old = old_coordinate[1]
            if y_old < self.rooster_height:
                y_new = self.rooster_height - 1 - y_old + x_old
                x_new = x_old
                # new_coordinates.append([x_new, y_new, x_old, y_old])
                new_coordinates.append([x_new, y_new])
            else:
                y_new = x_old
                x_new = y_old - self.rooster_height + 1 + x_old
                # new_coordinates.append(["BIG", x_new, y_new, x_old, y_old])
                new_coordinates.append([x_new, y_new])
        # print(new_coordinates)
        return new_coordinates


def main():
    inputs = reader.read_input(case)
    puzzle_1 = Puzzle(inputs)
    # puzzle_1.printer(puzzle_1.rooster)
    # puzzle_1.printer(puzzle_1.vertical)
    # puzzle_1.printer(puzzle_1.diagonal_tl_br)
    # puzzle_1.printer(puzzle_1.diagonal_bl_tr)
    puzzle_1.counter_part1()
    puzzle_1.counter_part2()
    print("end")


if __name__ == "__main__":
    main()
