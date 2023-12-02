colors = ["red", "green", "blue"]
max_colors = {"red": 12, "green": 13, "blue": 14}


class Solution:
    def __init__(self):
        pass

    def read_input(self, path="data/02dec.txt"):
        with open(path, "r") as f:
            self.input = f.readlines()
            self.input = [l.strip("\n\r") for l in self.input]

    def solve(self):
        sum = 0
        for line in self.input:
            # line = "Game 100: 5 red, 9 green, 2 blue; 9 blue, 6 green, 1 red; 8 blue, 7 green, 3 red"
            # line = "Game 93: 3 blue; 8 blue; 3 blue, 2 red; 2 red, 1 green"
            # line = "Game 68: 7 red, 1 blue, 12 green; 17 red, 1 green; 10 red, 8 green; 16 red, 5 green, 2 blue; 4 red, 1 blue, 8 green; 8 green, 7 red, 2 blue"
            game = self.parse_input(line)
            invalid = False
            for draw in game["draws"]:
                for color in colors:
                    if draw[color] > max_colors[color]:
                        invalid = True
                        break
                if invalid:
                    break
            if not invalid:
                sum += game["game_num"]
        print(sum)

    def solve2(self):
        sum = 0
        for line in self.input:
            # line = "Game 100: 5 red, 9 green, 2 blue; 9 blue, 6 green, 1 red; 8 blue, 7 green, 3 red"
            # line = "Game 93: 3 blue; 8 blue; 3 blue, 2 red; 2 red, 1 green"
            # line = "Game 68: 7 red, 1 blue, 12 green; 17 red, 1 green; 10 red, 8 green; 16 red, 5 green, 2 blue; 4 red, 1 blue, 8 green; 8 green, 7 red, 2 blue"
            game = self.parse_input(line)
            smalest_game = {"red": 0, "green": 0, "blue": 0}
            for draw in game["draws"]:
                for color in colors:
                    if draw[color] > smalest_game[color]:
                        smalest_game[color] = draw[color]
            pow = smalest_game["red"] * smalest_game["green"] * smalest_game["blue"]
            sum += pow
        print(sum)

    def parse_input(self, line: str):
        game_num = int(line.split(":")[0][5:])
        draws = line.split(":")[1].split(";")
        resp = {"game_num": game_num, "draws": []}
        for draw in draws:
            draw = draw.replace(",", "")
            draw_list = draw.split()
            draw_dict = {"red": 0, "green": 0, "blue": 0}
            for color in colors:
                if color in draw_list:
                    idx = draw_list.index(color)
                    draw_dict[color] = int(draw_list[idx - 1])
            resp["draws"].append(draw_dict)

        return resp


if __name__ == "__main__":
    sol = Solution()
    sol.read_input()
    # sol.solve()  # 2593
    sol.solve2()  # 54699
    pass
