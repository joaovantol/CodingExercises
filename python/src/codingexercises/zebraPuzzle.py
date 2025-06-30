from itertools import permutations

class ZebraPuzzle:
    def __init__(self) -> None:
        self.solution: (None | dict[str, dict[str, int]]) = None

    def solve(self) -> bool:
        # Clue 1: There are five houses
        houses = [1, 2, 3, 4, 5]

        # a) Generate permutations for colors and check the only color clue
        for (red, green, ivory, yellow, blue) in permutations(houses):
            # Clue 6: green is immediately right of ivory (green = ivory + 1)
            if green != ivory + 1:
                continue

            # b) Generate permutations for nationalities and check their clues
            for (english, spaniard, ukrainian, norwegian, japanese) in permutations(houses):
                # Clue 2: English in red house
                if english != red:
                    continue
                # Clue 10: Norwegian in first house
                if norwegian != 1:
                    continue
                # Clue 15: Norwegian is a neighbor to the blue house
                if abs(norwegian - blue) != 1:
                    continue

                # c) Generate beverage permutations and check their clues
                for (coffee, tea, milk, orange_juice, water) in permutations(houses):
                    # Clue 4: Green houser drinks coffee
                    if coffee != green:
                        continue
                    # Clue 5: Ukrainian drinks tea
                    if ukrainian != tea:
                        continue
                    # Clue 9: Middle houser drinks milk
                    if milk != 3:
                        continue

                    # d) Generate activity permutations and check their clues
                    for (dancer, painter, reader, footballer, chess_player) in permutations(houses):
                        # Clue 8: Painter in yellow house
                        if painter != yellow:
                            continue
                        # Clue 13: Footballer drinks orange juice
                        if footballer != orange_juice:
                            continue
                        # Clue 14: japanese plays chess
                        if japanese != chess_player:
                            continue

                        # e) Generate pet permutations and check their clues
                        for (dog, snails, fox, horse, zebra) in permutations(houses):
                            # Clue 3: Spaniard owns dog
                            if spaniard != dog:
                                continue
                            # Clue 7: Dancer owns snails
                            if dancer != snails:
                                continue
                            # Clue 11: Reader next to fox owner
                            if abs(reader - fox) != 1:
                                continue
                            # Clue 12: Painter next to horse owner
                            if abs(painter - horse) != 1:
                                continue

                            # We found a solution that satisfies all constraints
                            self.solution = {
                                'colors': {
                                    'red': red,
                                    'green': green,
                                    'ivory': ivory,
                                    'yellow': yellow,
                                    'blue': blue
                                },
                                'nationalities': {
                                    'english': english,
                                    'spaniard': spaniard,
                                    'ukrainian': ukrainian,
                                    'norwegian': norwegian,
                                    'japanese': japanese
                                },
                                'drinks': {
                                    'coffee': coffee,
                                    'tea': tea,
                                    'milk': milk,
                                    'orange_juice': orange_juice,
                                    'water': water
                                },
                                'smokes': {
                                    'dancer': dancer,
                                    'painter': painter,
                                    'reader': reader,
                                    'footballer': footballer,
                                    'chess_player': chess_player
                                },
                                'pets': {
                                    'dog': dog,
                                    'snails': snails,
                                    'fox': fox,
                                    'horse': horse,
                                    'zebra': zebra
                                }
                            }

                            return True

        return False

    def drinksWater(self) -> (str | None):
        if not self.solution:
            return None

        water_house = self.solution['drinks']['water']
        for nationality, house in self.solution['nationalities'].items():
            if house == water_house:
                return nationality

        return None

    def ownsZebra(self) -> (str | None):
        if not self.solution:
            return None

        zebra_house = self.solution['pets']['zebra']
        for nationality, house in self.solution['nationalities'].items():
            if house == zebra_house:
                return nationality

        return None


# if __name__ == "__main__":
#     puzzle = ZebraPuzzle()
#     if puzzle.solve():
#         print("Solution found:")
#         print(f"The {puzzle.drinksWater()} drinks water.")
#         print(f"The {puzzle.ownsZebra()} owns the zebra.")

#         # Print full solution
#         print("\nFull solution:")
#         for category, items in puzzle.solution.items():
#             print(f"\n{category.capitalize()}:")
#             for item, house in items.items():
#                 print(f"  {item}: House {house}")
#     else:
#         print("No solution found.")
