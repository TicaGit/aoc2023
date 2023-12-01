hash = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


class Solution:
    def __init__(self):
        pass

    def read_input(self, path="data/01dec.txt"):
        with open(path, "r") as f:
            self.input = f.readlines()
            self.input = [l.strip("\n\r") for l in self.input]

    def solve(self):
        self.output = 0
        for line in self.input:
            digits = [int(d) for d in line if d.isdigit()]
            combined_digits = digits[0] * 10 + digits[-1]
            self.output += combined_digits
        print(self.output)

    def solve2(self):
        self.output = 0
        for line in self.input:
            line = self.parse_line(line)
            digits = [int(d) for d in line if d.isdigit()]
            combined_digits = digits[0] * 10 + digits[-1]
            self.output += combined_digits
        print(self.output)

    def parse_line(self, line):
        new_line = ""
        for carac in line:
            new_line = new_line + carac
            for dig_letter, dig in hash.items():
                if dig_letter in new_line:
                    new_line = new_line.replace(dig_letter[:-1], str(dig))  # ugly: keep last letter
        return new_line


if __name__ == "__main__":
    sol = Solution()
    sol.read_input()
    # sol.solve()  # 54940
    sol.solve2()  # 54208
    pass
