from src.utils import read_input


class Solution:
    def __init__(self):
        pass

    def solve(self, input: list[str]):
        seeds = input[0]
        current = seeds.split(":")[1].split(" ")
        current = [int(num) for num in current if num.isdigit()]

        maping = {"dest": [], "source": [], "range": []}
        for i in range(2, len(input)):
            next = input[i]
            if next[0].isalpha():
                # title
                continue
            if next == "\n":
                current = self.map_to_next(maping=maping, current=current)
                maping = {"dest": [], "source": [], "range": []}
                continue

            dest, source, range_ = next.strip("\n").split(" ")
            maping["dest"].append(int(dest))
            maping["source"].append(int(source))
            maping["range"].append(int(range_))

        current = self.map_to_next(maping=maping, current=current)
        print(min(current))

    def solve2(self, input: list[str]):
        seeds = input[0]
        current_ranges = self.get_seeds(seeds)

        maping = {"dest_start": [], "dest_stop": [], "source_start": [], "source_stop": []}
        for i in range(2, len(input)):
            next = input[i]
            if next[0].isalpha():
                # title
                continue
            if next == "\n":
                current_ranges = self.map_to_next_ranges(maping=maping, current_ranges=current_ranges)
                maping = {"dest_start": [], "dest_stop": [], "source_start": [], "source_stop": []}
                continue

            dest, source, range_ = next.strip("\n").split(" ")
            maping["dest_start"].append(int(dest))
            maping["dest_stop"].append(int(dest) + int(range_))
            maping["source_start"].append(int(source))
            maping["source_stop"].append(int(source) + int(range_))

        current_ranges = self.map_to_next_ranges(maping=maping, current_ranges=current_ranges)
        print(min(current_ranges, key=lambda x: x[0])[0])
        pass

    def map_to_next_ranges(self, maping: dict, current_ranges: list[int]):
        remaining_ranges = current_ranges
        new_ranges = []
        while len(remaining_ranges) > 0:
            range_ = remaining_ranges.pop(0)
            mapped = False
            for dest_start, dest_stop, source_start, source_stop in zip(
                maping["dest_start"], maping["dest_stop"], maping["source_start"], maping["source_stop"]
            ):
                # a) whole range is include in the source range, or perfect match
                if range_[0] >= source_start and range_[1] <= source_stop:
                    exceed_before = range_[0] - source_start
                    exceed_after = source_stop - range_[1]
                    new_ranges.append((dest_start + exceed_before, dest_stop - exceed_after))
                    mapped = True
                    break
                # d) current start is outside of the source range, but the stop is inside
                if range_[0] < source_start and range_[1] > source_start and range_[1] <= source_stop:
                    exceed = source_stop - range_[1]
                    remaining_ranges.append((range_[0], source_start))
                    new_ranges.append((dest_start, dest_stop - exceed))
                    mapped = True
                    break
                # c) current start is inside of the source range, but the stop is outside
                if range_[0] >= source_start and range_[0] < source_stop and range_[1] > source_stop:
                    exceed = range_[0] - source_start
                    remaining_ranges.append((source_stop, range_[1]))
                    new_ranges.append((dest_start + exceed, dest_stop))
                    mapped = True
                    break
                # b) whole source is included in the range
                if range_[0] < source_start and range_[1] > source_stop:
                    remaining_ranges.append((range_[0], source_start))
                    remaining_ranges.append((source_stop, range_[1]))
                    new_ranges.append((dest_start, dest_stop))
                    mapped = True
                    break
            # range is not mapped
            if not mapped:
                new_ranges.append(range_)
        return new_ranges

    def get_seeds(self, seeds):
        current = seeds.split(":")[1].strip().split(" ")
        current = [int(num) for num in current if num.isdigit()]
        ranges = []
        for i in range(len(current)):
            if i % 2 == 0:
                ranges.append((current[i], current[i] + current[i + 1]))  # stop is exclusive
        return ranges

    def map_to_next(self, maping: dict, current: list[int]):
        new_item = []
        for item in current:
            match = False
            for dest, source, range_ in zip(maping["dest"], maping["source"], maping["range"]):
                if item >= source and item < source + range_:
                    shift = item - source
                    new_item.append(dest + shift)
                    match = True
                    break
            # no matching range
            if not match:
                new_item.append(item)

        return new_item


if __name__ == "__main__":
    input = read_input("data/05dec.txt")
    sol = Solution()
    # sol.solve(input)  # 17803
    sol.solve2(input)  # 2008785
    pass
