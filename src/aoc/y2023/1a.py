from toolz import functoolz  # type: ignore

from aoc.y2023.utils import input


day = 1


def main():
    return functoolz.pipe(
        input(day),
        lambda x: x.text,
        lambda x: x.split(),
        lambda x: [[s for s in i if s.isdigit()] for i in x],
        lambda x: [i[0] + i[-1] for i in x],
        lambda x: [int(i) for i in x],
        sum,
    )


result = main()
print(result)
