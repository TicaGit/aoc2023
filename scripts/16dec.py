from functools import cache
from pathlib import Path

import numpy as np
from tqdm import tqdm


def read_input(path: Path):
    with open(path, "r") as f:
        return f.readlines()


class Beam:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.pos = (x, y)
        self.posdir = (x, y, dx, dy)
        self.pos_inverse = (y, x)

    def __repr__(self):
        return f"Beam({self.x}, {self.y}, {self.dx}, {self.dy})"

    def is_in_map(self, map):
        return self.x >= 0 and self.x < len(map[0]) and self.y >= 0 and self.y < len(map)


class Solution:
    def __init__(self):
        pass

    def solve(self, input: list[str]):
        self.map = np.array([list(x.strip()) for x in input])
        # print(self.map)
        energized = set()
        beams = [Beam(0, 0, 1, 0)]

        ctr = 0
        prev = 0

        while True:
            energized.update([beam.posdir for beam in beams if beam.is_in_map(self.map)])
            new_beams = []
            for beam in beams:
                beams_out = self.step(beam)

                if beams_out is not None:
                    for bo in beams_out:
                        if bo.posdir not in energized:
                            new_beams.append(bo)
            beams = new_beams
            # print(beams)

            if len(beams) == 0:
                break
            if len(energized) == prev:
                ctr += 1
                if ctr == 100:
                    break
            else:
                ctr = 0
            prev = len(energized)

        print(len(energized))

    def solve2(self, input: list[str]):
        self.map = np.array([list(x.strip()) for x in input])
        self.map = tuple(tuple(x) for x in self.map)
        # print(self.map)
        starting_beams = [Beam(0, y, 1, 0) for y in range(len(self.map))]
        starting_beams.extend([Beam(len(self.map[0]) - 1, y, 1, 0) for y in range(len(self.map))])
        starting_beams.extend([Beam(x, 0, 1, 0) for x in range(1, len(self.map[0]) - 1)])
        starting_beams.extend([Beam(x, len(self.map) - 1, 1, 0) for x in range(1, len(self.map[0]) - 1)])
        # starting_beams = [Beam(0, 0, 1, 0)]

        best_energy = 0
        for beams in tqdm(starting_beams):
            beams = [beams]
            energized = set()

            ctr = 0
            prev = 0

            while True:
                energized.update([beam.posdir for beam in beams if beam.is_in_map(self.map)])
                new_beams = []
                for beam in beams:
                    beams_out = step(beam.x, beam.y, beam.dx, beam.dy, map_=self.map)
                    if beams_out is not None:
                        for bo in beams_out:
                            if bo.posdir not in energized:
                                new_beams.append(bo)
                beams = new_beams
                # print(beams)

                if len(beams) == 0:
                    break
                if len(energized) == prev:
                    ctr += 1
                    if ctr == 100:
                        break
                else:
                    ctr = 0
                prev = len(energized)

            real_energy = set([(ene[0], ene[1]) for ene in energized])
            if len(real_energy) > best_energy:
                best_energy = len(real_energy)
                print("best", best_energy)

        print(f"final: {best_energy}")


@cache
def step(x, y, dx, dy, map_):
    H = len(map_)
    W = len(map_[0])

    # limit map
    if x < 0 or x >= W or y < 0 or y >= H:
        return None
    # print(self.map[beam.pos_inverse])
    # straight
    if map_[y][x] == ".":
        return [Beam(x + dx, y + dy, dx, dy)]

    if map_[y][x] == "/":
        return [Beam(x - dy, y - dx, -dy, -dx)]

    if map_[y][x] == "\\":
        return [Beam(x + dy, y + dx, dy, dx)]

    if map_[y][x] == "|":
        if dx == 0:
            # straight
            return [Beam(x + dx, y + dy, dx, dy)]
        else:
            return [Beam(x, y + 1, 0, 1), Beam(x, y - 1, 0, -1)]
    if map_[y][x] == "-":
        if dy == 0:
            # straight
            return [Beam(x + dx, y + dy, dx, dy)]
        else:
            return [Beam(x + 1, y, 1, 0), Beam(x - 1, y, -1, 0)]


if __name__ == "__main__":
    input = read_input("data/16dec.txt")
    sol = Solution()
    # sol.solve(input)  # 6883
    sol.solve2(input)  # 157383940585037
    pass
