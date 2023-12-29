from src.utils import read_input


class Solution:
    def __init__(self):
        pass

    def solve(self, cards: list[str]):
        tot = 0
        for card in cards:
            winning, ours = card.split(":")[1].split("|")
            winning = set([int(num) for num in winning.split() if num.isdigit()])
            ours = set([int(num) for num in ours.split() if num.isdigit()])
            same = winning.intersection(ours)
            if same:
                tot += pow(2, len(same) - 1)
        print(tot)

    def solve2(self, cards: list[str]):
        number_of_cards = {i: 1 for i in range(1, len(cards) + 1)}
        for i, card in enumerate(cards):
            current_card_number = i + 1
            winning, ours = card.split(":")[1].split("|")
            winning = set([int(num) for num in winning.split() if num.isdigit()])
            ours = set([int(num) for num in ours.split() if num.isdigit()])
            same = winning.intersection(ours)
            num_matches = len(same)
            for card_number in range(current_card_number + 1, current_card_number + num_matches + 1):
                number_of_cards[card_number] += number_of_cards[current_card_number]
        tot = sum(number_of_cards.values())
        print(tot)


if __name__ == "__main__":
    input = read_input("data/04dec.txt")
    sol = Solution()
    # sol.solve(input)  # 17803
    sol.solve2(input)  # 54699
    pass
