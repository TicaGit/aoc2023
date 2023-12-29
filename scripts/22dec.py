from functools import cache
from pathlib import Path

import numpy as np
from tqdm import tqdm


def read_input(path: Path):
    with open(path, "r") as f:
        return f.readlines()


class Solution:
    def __init__(self):
        pass

    def solve(self, input: list[str]):
        self.bricks = {}
        for i, brick in enumerate(input):
            begining, end = brick.strip().split("~")
            bx, by, bz = [int(a) for a in begining.split(",")]
            ex, ey, ez = [int(a) for a in end.split(",")]
            coords = []
            for x in range(bx, ex + 1):
                for y in range(by, ey + 1):
                    for z in range(bz, ez + 1):
                        coords.append((x, y, z))
            self.bricks[i] = coords
        print(self.bricks)
        self.fall()
        print(self.bricks)
        pass

        self.can_remove = []
        for id, coords in self.bricks.items():
            all_id_on_top = self.which_is_on_top(id, self.bricks)
            if len(all_id_on_top) == 0:
                self.can_remove.append(id)
                continue

            all_suported = True
            for id_on_top in all_id_on_top:
                is_on_bottom = self.which_is_on_bottom(id_on_top, self.bricks)
                if len(is_on_bottom) <= 1:
                    all_suported = False
                    break
            if all_suported:
                self.can_remove.append(id)

        print(len(self.can_remove))

    def fall(self):
        sorted_keys = sorted(self.bricks, key=lambda x: min([coord[2] for coord in self.bricks[x]]))
        for brick_id in tqdm(sorted_keys):
            while self.can_go_one_down(brick_id, self.bricks):
                self.bricks[brick_id] = [(x, y, z - 1) for x, y, z in self.bricks[brick_id]]

    def can_go_one_down(self, brick_id, bricks):
        for coords in bricks[brick_id]:
            if coords[2] == 1:
                return False
            potential = (coords[0], coords[1], coords[2] - 1)
            for other_id, other_coords in bricks.items():
                if other_id == brick_id:
                    continue
                if potential in other_coords:
                    return False
        return True

    def which_is_on_top(self, brick_id, bricks):
        ids = []
        for coords in bricks[brick_id]:
            potential = (coords[0], coords[1], coords[2] + 1)
            for other_id, other_coords in bricks.items():
                if other_id == brick_id:
                    continue
                if potential in other_coords:
                    ids.append(other_id)
        return set(ids)

    def which_is_on_bottom(self, brick_id, bricks):
        ids = []
        for coords in bricks[brick_id]:
            potential = (coords[0], coords[1], coords[2] - 1)
            for other_id, other_coords in bricks.items():
                if other_id == brick_id:
                    continue
                if potential in other_coords:
                    ids.append(other_id)
        return set(ids)

    def solve2(self):
        sorted_keys = sorted(self.bricks, key=lambda x: min([coord[2] for coord in self.bricks[x]]))
        sum_ = 0
        for brick_id in sorted_keys:
            will_fall = []
            fallen = [brick_id]
            if brick_id in self.can_remove:
                continue
            will_fall.extend(list(self.which_is_on_top(brick_id, self.bricks)))
            while will_fall:
                brick_to_fall = will_fall.pop(0)
                bot_bricks = self.which_is_on_bottom(brick_to_fall, self.bricks)
                if bot_bricks.issubset(set(fallen)):
                    fallen.append(brick_to_fall)
                    will_fall.extend(
                        [x for x in self.which_is_on_top(brick_to_fall, self.bricks) if x not in will_fall]
                    )
            sum_ += len(fallen) - 1
        print(sum_)

    def solve2_fail(self, input: list[str]):
        which_could_fall = {idx: set() for idx in self.bricks}
        sorted_keys = sorted(self.bricks, key=lambda x: max([coord[2] for coord in self.bricks[x]]), reverse=True)
        sum_ = 0
        for brick_id in sorted_keys:
            which_could_fall[brick_id] = self.which_is_on_top(brick_id, self.bricks)

            for id_on_top in which_could_fall[brick_id]:
                res_set = set()
                is_on_bottom = self.which_is_on_bottom(id_on_top, self.bricks)
                for id_bot in is_on_bottom:
                    res_set = res_set & which_could_fall[id_bot]
                if id_on_top in res_set:
                    pass

                if len(is_on_bottom) <= 1:
                    num += 1
                    num += [id_on_top]

            [brick_id] = num
            sum_ += num

        print(sum_)


if __name__ == "__main__":
    input = read_input("data/22dec.txt")
    sol = Solution()
    sol.solve(input)  # 480
    sol.solve2()  # 157383940585037
    pass
