import reader


class decipher:
    def __init__(self, code, ):
        self.code = code[0]
        self.read_startpos = 0
        self.read_currpos = 0
        self.read_endpos = 0
        self.read = ""
        self.checkpos = 0
        self.passed_checks = 0
        self.passed_checks2 = 0
        self.passed_checks3 = 0
        self.digit = ""
        self.matches = []
        self.matches2 = []
        self.pairs = []
        self.part1sum = 0
        self.part2sum = 0
        self.enabler = True
        self.pairs2 = []

    def function(self):
        pass

    def get_curletter(self):
        letter = self.code[self.read_currpos]
        self.read_currpos += 1
        self.read += letter
        return letter

    def get_nextletter(self):
        nextletter = self.code[self.read_currpos]
        return nextletter

    def check_digit(self, letter: str):
        if letter.isdigit():
            return True

    def reader(self):
        letter = self.get_curletter()
        if self.check_digit(letter) and self.check_digit(self.get_nextletter()):

            while self.check_digit(self.get_nextletter()):
                letter = self.get_curletter()

        else:
            pass

    def check(self, curpo, read):
        checkpassed = False
        letter = read[curpo]
        if self.passed_checks == 0:
            if letter == "m":
                checkpassed = True
        if self.passed_checks == 1:
            if letter == "u":
                checkpassed = True
        if self.passed_checks == 2:
            if letter == "l":
                checkpassed = True
        if self.passed_checks == 3:
            if letter == "(":
                checkpassed = True
        if self.passed_checks == 4:
            number = int(self.read[4:])
            if number >= 0 and number <= 1000:
                checkpassed = True
        if self.passed_checks == 5:
            if letter == ",":
                checkpassed = True

        if self.passed_checks == 6:
            pos_komma = self.read.index(",") + 1
            test = self.read[pos_komma:]
            number = int(self.read[pos_komma:])
            if number >= 0 and number <= 1000:
                checkpassed = True

        if self.passed_checks == 7:
            if letter == ")":
                self.matches.append(self.read)
                if self.enabler:
                    self.matches2.append(self.read)
                checkpassed = False
                self.passed_checks = 0

        if checkpassed:
            self.passed_checks += 1

        return checkpassed

    def check2(self, curpo, read):
        checkpassed = False
        letter = read[curpo]
        if self.passed_checks2 == 0:
            if letter == "d":
                checkpassed = True
                self.passed_checks3 += 1

        if self.passed_checks2 == 1:
            if letter == "o":
                checkpassed = True
                self.passed_checks3 += 1
        if self.passed_checks2 == 2:
            if letter == "(":
                checkpassed = True
        if self.passed_checks2 == 3:
            if letter == ")":
                self.enabler = True

        if checkpassed:
            self.passed_checks2 += 1

        return checkpassed

    def check3(self, curpo, read):
        checkpassed = False
        letter = read[curpo]
        if self.passed_checks3 == 0:
            if letter == "d":
                checkpassed = True

        if self.passed_checks3 == 1:
            if letter == "o":
                checkpassed = True
        if self.passed_checks3 == 2:
            if letter == "n":
                checkpassed = True
                self.passed_checks2 = 0
        if self.passed_checks3 == 3:
            if letter == "'":
                checkpassed = True
        if self.passed_checks3 == 4:
            if letter == "t":
                checkpassed = True
        if self.passed_checks3 == 5:
            if letter == "(":
                checkpassed = True
        if self.passed_checks3 == 6:
            if letter == ")":
                self.enabler = False

        if checkpassed:
            self.passed_checks3 += 1

        return checkpassed

    def reset(self):
        self.cutter()
        self.read_currpos = 0
        self.read = ""
        self.passed_checks = 0
        self.passed_checks2 = 0
        self.passed_checks3 = 0

    def cutter(self):
        if self.read[-1] == "m":
            self.code = self.code[self.read_currpos - 1:]
        else:
            self.code = self.code[self.read_currpos:]

    def checker(self):
        if self.check(self.read_currpos - 1, self.read) == True:
            # print(self.read_currpos)
            pass
        elif self.check2(self.read_currpos - 1, self.read) == True:
            pass

        elif self.check3(self.read_currpos - 1, self.read) == True:
            pass

        else:
            # print(self.read)
            # print(self.code)
            self.reset()

    def checker_run(self):
        while self.code != "":
            self.reader()
            self.checker()

    def transformator(self):
        for item in self.matches:
            start = item.index("(") + 1
            end = item.index(")")
            vals = item[start:end].split(",")

            self.pairs.append([int(vals[0]), int(vals[1])])

        for item in self.matches2:
            start = item.index("(") + 1
            end = item.index(")")
            vals = item[start:end].split(",")

            self.pairs2.append([int(vals[0]), int(vals[1])])

    def calculator(self):
        for item in self.pairs:
            self.part1sum += item[0] * item[1]
        for item in self.pairs2:
            self.part2sum += item[0] * item[1]


def main():
    input = [reader.read_input(1)]
    decipher_instant = decipher(input)

    decipher_instant.checker_run()
    print(decipher_instant.matches)
    print(decipher_instant.matches2)
    decipher_instant.transformator()
    decipher_instant.calculator()

    # 31104909 to low
    181345830

    print(decipher_instant.pairs)
    print(decipher_instant.part1sum)
    print(decipher_instant.part2sum)


main()
