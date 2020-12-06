import sys


def make_map(lines):
    return [[x == "#" for x in line.strip()] for line in lines]


def tree(m, x, y):
    return m[y][x]


lines = sys.stdin.readlines()
map = make_map(lines)
width = len(map[0])

trees = 0
try:
    x = 0
    y = 0
    while True:
        if tree(map, x % width, y):
            trees += 1
        x += 3
        y += 1
except IndexError:
    pass

print(trees)
