from functools import cache

from tqdm import tqdm

from src.utils import read_input


def cache_me(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res

    return wrapper


class Solution:
    def __init__(self):
        pass

    def solve(self, input: list[str]):
        sum = 0
        for spring in tqdm(input):
            # print(spring)
            spring, config = spring.strip().split(" ")
            config = tuple([int(x) for x in config.split(",")])
            # .??..??...?##. 1,1,3
            # spring, config = "???##.?#?????#????", (4, 1, 3)
            # spring, config = "?##.?#?????#????", (4, 1, 3)
            sol = compute_dispo(spring, config)
            sum += sol
            print(f"sol for {spring} and {config}:", sol)
        print(sum)

    def solve2(self, input: list[str]):
        sum = 0
        for spring in input:
            # print(spring)
            spring, config = spring.strip().split(" ")
            spring = "?".join([spring] * 5)
            config = ",".join([config] * 5)
            config = tuple([int(x) for x in config.split(",")])
            # .??..??...?##. 1,1,3
            # spring, config = "???##.?#?????#????", (4, 1, 3)
            # spring, config = "?##.?#?????#????", (4, 1, 3)
            sol = compute_dispo(spring, config)
            sum += sol
            # print(f"sol for {spring} and {config}:", sol)
        print(sum)


@cache_me
def compute_dispo(spring, config):
    # print(spring, config)

    if len(config) == 0:
        if "#" in spring:
            return 0
        else:
            return 1

    space = config[0]
    idx, forced = find_idx(spring, space)
    if idx == -1:
        return 0
    if forced:
        return compute_dispo(spring[(idx + space + 1) :], config[1:])

    return compute_dispo(spring[(idx + space + 1) :], config[1:]) + compute_dispo(spring[idx + 1 :], config)


def find_idx(spring, space) -> int:
    # remaining too short
    if len(spring) < space:
        return -1, False
    for i in range(len(spring)):
        # remaining too short
        if len(spring) - i < space:
            return -1, False
        if spring[i] != ".":
            if spring[i] == "#":
                forced = True
            else:
                forced = False
            works = True
            for j in range(space):
                if spring[i + j] == ".":
                    works = False
                    break
            # check carac after
            if i + space < len(spring) and spring[i + space] == "#":
                works = False
            if forced and not works:
                return -1, False
            if works:
                return i, forced
    return -1, False


if __name__ == "__main__":
    input = read_input("data/12dec.txt")
    sol = Solution()
    # sol.solve(input)  # 7670
    sol.solve2(input)  # 157383940585037
    sol.solve2(input)  # 157383940585037
    pass
