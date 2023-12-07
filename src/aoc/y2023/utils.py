import os.path

import requests  # type: ignore


YEAR = 2023


here = os.path.abspath(__file__)
session_file = os.path.abspath(
    os.path.join(here, "../../../../session-cookie.txt")
)
with open(session_file) as fh:
    cookie = fh.read()


def input(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    return requests.get(url, cookies={"session": cookie})
