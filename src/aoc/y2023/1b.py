import re

from toolz import functoolz  # type: ignore

from aoc.y2023.utils import input


day = 1


number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def substitute_strings(text):
    pattern = '(?=' + '|'.join(number_words.keys()) + ')'

    offset = 0

    for match in re.finditer(pattern, text):
        word_start = match.start() + offset
        for number_word, digit in number_words.items():
            if text[word_start:].startswith(number_word):
                text = text[:word_start] + digit + text[word_start:]
                offset += 1
                break  # Break after the first matching word is processed

    return text


def main():
    return functoolz.pipe(
        input(day),
        lambda x: x.text,
        lambda x: x.split(),
        lambda x: [substitute_strings(i) for i in x],
        lambda x: [[s for s in i if s.isdigit()] for i in x],
        lambda x: [i[0] + i[-1] for i in x],
        lambda x: [int(i) for i in x],
        sum,
    )


import pprint  # noqa
result = main()
pprint.pprint(result)
