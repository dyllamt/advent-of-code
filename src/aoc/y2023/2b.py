from toolz import functoolz  # type: ignore

from aoc.y2023.utils import input


day = 2


def parse_cubes(text):
    nummber, color = text.strip().split(" ")
    return color.strip(), int(nummber.strip())


def parse_round(text):
    round = {}
    for cubes in text.split(","):
        color, number = parse_cubes(cubes)
        round[color] = number
    return round


def parse_game(text):
    game, rounds = text.split(":")
    game = int(game[5:])
    rounds = [parse_round(i) for i in rounds.strip().split(";")]
    return game, rounds


def minimum_cubes(game):
    _, rounds = game
    cubes = {}
    for round in rounds:
        for cube, number in round.items():
            if cubes.get(cube, 0) < number:
                cubes[cube] = number
    return cubes


def power(game):
    p = 1
    for _, number in game.items():
        p *= number
    return p


def main():
    return functoolz.pipe(
        input(day),
        lambda x: x.text,
        lambda x: x.split("\n"),
        lambda x: x[:-1],
        lambda x: map(parse_game, x),
        lambda x: map(minimum_cubes, x),
        lambda x: map(power, x),
        sum,
    )


result = main()
print(result)
