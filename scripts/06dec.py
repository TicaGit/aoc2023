from tqdm import tqdm

from src.utils import read_input


class Solution:
    def __init__(self):
        pass

    def solve(self, input: list[str]):
        times = [int(dig) for dig in input[0].split(":")[1].strip().split(" ") if dig.isdigit()]
        dists = [int(dig) for dig in input[1].split(":")[1].strip().split(" ") if dig.isdigit()]
        tot = 1
        for time, dist in zip(times, dists):
            win = 0
            for mill_sec_pressed in tqdm(range(0, time + 1)):
                speed = mill_sec_pressed
                dist_made = (time - mill_sec_pressed) * speed
                if dist_made > dist:
                    win += 1
            tot *= win
        print(tot)

    def solve2(self, input: list[str]):
        times = [dig for dig in input[0].split(":")[1].strip().split(" ") if dig.isdigit()]
        dists = [dig for dig in input[1].split(":")[1].strip().split(" ") if dig.isdigit()]
        time = int("".join(times))
        dist = int("".join(dists))
        win = 0
        for mill_sec_pressed in tqdm(range(0, time + 1)):
            speed = mill_sec_pressed
            dist_made = (time - mill_sec_pressed) * speed
            if dist_made > dist:
                win += 1
        print(win)


if __name__ == "__main__":
    input = read_input("data/06dec.txt")
    sol = Solution()
    # sol.solve(input)  # 781200
    sol.solve2(input)  # 49240091
    pass
