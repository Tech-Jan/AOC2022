class Printer:
    def __init__(self, prints: list, pos: tuple = (), fov: int = 0):
        self.pos = pos
        self.fov_range = fov
        self.prints = prints
        self.x_min = 0
        self.x_max = len(self.prints[0])
        self.y_min = 0
        self.y_max = len(self.prints)
        self.fov = {"x_min": self.x_min,
                    "x_max": self.x_max,
                    "y_min": self.y_min,
                    "y_max": self.y_max}

    def checks(self):
        x_min = self.pos[0] - self.fov_range*2-2
        x_max = self.pos[0] + self.fov_range*2-1

        delta_xmin = 0

        delta_xmax = 0

        y_min = self.pos[1] - self.fov_range
        y_max = self.pos[1] + self.fov_range+1
        delta_ymin = 0
        delta_ymax = 0

        if x_min <= 0:
            self.fov["x_min"] = 0
            delta_xmin = abs(x_min)
        else:
            self.fov["x_min"] = x_min

        if x_max >= self.x_max:
            self.fov["x_max"] = self.x_max
            self.fov["x_min"] = self.fov["x_min"] - abs(self.x_max - x_max)
        else:
            self.fov["x_max"] = x_max + delta_xmin

        if y_min <= 0:
            self.fov["y_min"] = 0
            delta_ymin = abs(y_min)
        else:
            self.fov["y_min"] = y_min

        if y_max >= self.y_max:
            self.fov["y_max"] = self.y_max
            self.fov["y_min"] = self.fov["y_min"] - abs(self.y_max - y_max)
        else:
            self.fov["y_max"] = y_max + delta_ymin

    def print_cut(self):
        pass

    def printer2(self):
        prints_str = self.turn_to_string(self.prints)
        if self.pos != () and (self.fov_range!=0 and self.fov_range*2<self.x_max) :
            self.prints = self.checks()

        for line in prints_str[self.fov["y_min"]:self.fov["y_max"]]:
            print(line[self.fov["x_min"]:self.fov["x_max"]])

        print( "O                                                     O")



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
