import sys


def parse_line(line):
    parts = line.split()
    count_range = [int(x) for x in parts[0].split("-")]
    letter = parts[1][0]
    password = parts[2]

    return (count_range[0], count_range[1], letter, password)


def letter_count(s, l):
    return len([x for x in list(s) if x == l])


def valid(entry):
    count = letter_count(entry[3], entry[2])
    return entry[0] <= count <= entry[1]


def valid2(entry):
    try:
        return (entry[3][entry[0] - 1] == entry[2]) ^ (entry[3][entry[1] - 1] == entry[2])
    except IndexError:
        return False


entries = [parse_line(line) for line in sys.stdin.readlines()]
print(len([e for e in entries if valid(e)]))
print(len([e for e in entries if valid2(e)]))
