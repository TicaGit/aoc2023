from src.utils import read_input


class Solution:
    def __init__(self):
        pass

    def solve(self, input=list[str]):
        sequ = input[0].strip()

        nodes = self.get_nodes(input[2:])

        current_node = "AAA"
        count = 0
        ptr = 0
        while current_node != "ZZZ":
            count += 1

            next_instr = sequ[ptr]
            ptr += 1
            if ptr >= len(sequ):
                ptr = 0
            if next_instr == "R":
                current_node = nodes[current_node][1]
            else:
                current_node = nodes[current_node][0]
        print(count)
        pass

    def solve2(self, input=list[str]):
        sequ = input[0].strip()

        nodes = self.get_nodes(input[2:])

            current_nodes = self.find_initial(nodes)

        pass

    def get_nodes(self, input):
        nodes = {}
        for line in input:
            node, instr = line.strip().split("=")
            node = node.strip()
            left, right = instr.strip().split(",")
            left = left.strip("(")
            right = right.strip(")").strip()
            nodes[node] = (left, right)
        return nodes

    def find_initial(self, nodes):
        initials = []
        for key in nodes.keys():
            if key[2] == "A":
                initials.append(key)
        return initials


if __name__ == "__main__":
    input = read_input("data/08dec.txt")
    sol = Solution()
    # sol.solve(input)  # 16271
    sol.solve2(input)  # 54699
    pass
