from toolz import functoolz  # type: ignore

from aoc.y2023.utils import input


day = 2


real_bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_cubes(text):
    nummber, color = text.strip().split(" ")
    return color.strip(), int(nummber.strip())


def parse_round(text):
    round = {}
    for cubes in text.split(","):
        color, number = parse_cubes(cubes)
        round[color] = number
    return round


def is_valid_round(round):
    for i, j in round.items():
        if real_bag[i] < j:
            return False
    return True


def parse_game(text):
    game, rounds = text.split(":")
    game = int(game[5:])
    rounds = [parse_round(i) for i in rounds.strip().split(";")]
    return game, rounds


def is_valid_game(game):
    _, rounds = game
    for i in rounds:
        if not is_valid_round(i):
            return False
    return True


def main():
    return functoolz.pipe(
        input(day),
        lambda x: x.text,
        lambda x: x.split("\n"),
        lambda x: x[:-1],
        lambda x: map(parse_game, x),
        lambda x: filter(is_valid_game, x),
        lambda x: map(lambda y: y[0], x),
        sum,
    )


result = main()
print(result)
