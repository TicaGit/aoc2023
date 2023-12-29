from src.utils import read_input


class Solution:
    def __init__(self):
        pass

    def solve(self, lines: list[str]):
        lines = [line.strip() for line in lines]
        self.lines = lines
        height = len(lines)
        width = len(lines[0])
        self.carac_coords = [
            (x, y) for x in range(width) for y in range(height) if not (lines[y][x] == "." or lines[y][x].isdigit())
        ]
        sum = 0
        id = 0
        self.num_part_coords = []
        for j, line in enumerate(lines):
            i = 0
            while i < len(line):
                carac = line[i]
                if not carac.isdigit():
                    i += 1
                    continue

                # digit
                start = i
                next = line[i + 1]
                number = carac
                while next.isdigit():
                    i += 1
                    number += next
                    if i >= len(line) - 1:
                        break
                    next = line[i + 1]
                end = i
                is_part = self.is_num_part(start, end, j)
                if is_part:
                    id += 1
                    sum += int(number)
                    for k in range(start, end + 1):
                        self.num_part_coords.append({"coord": (k, j), "id": id, "number": number})
                i += 1
        print(sum)
        pass

    def solve2(self, lines: list[str]):
        height = len(self.lines)
        width = len(self.lines[0])
        self.star_coords = [(x, y) for x in range(width) for y in range(height) if self.lines[y][x] == "*"]

        sum = 0
        for x, y in self.star_coords:
            ctr = 0
            parts = []
            num = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i + x < 0 or i + x >= width or j + y < 0 or j + y >= height:
                        continue
                    if (i + x, j + y) in [part["coord"] for part in self.num_part_coords if part["id"] not in parts]:
                        ctr += 1
                        parts.append(
                            [part["id"] for part in self.num_part_coords if part["coord"] == (i + x, j + y)][0]
                        )
                        num.append(
                            [part["number"] for part in self.num_part_coords if part["coord"] == (i + x, j + y)][0]
                        )
            if ctr == 2:
                ratio = int(num[0]) * int(num[1])
                sum += ratio
        print(sum)
        pass

    def is_num_part(
        self,
        start,
        end,
        line_num,
    ):
        for j in [-1, 0, 1]:
            if j + line_num < 0 or j + line_num > len(self.lines):
                continue
            for i in range(-1, end - start + 1 + 1):
                if i + start < 0 or i + start > len(self.lines[0]):
                    continue
                if (start + i, line_num + j) in self.carac_coords:
                    return True
        return False


if __name__ == "__main__":
    input = read_input("data/03dec.txt")
    sol = Solution()
    sol.solve(input)  # 530495
    sol.solve2(input)  # 54699
    pass
