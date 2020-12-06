import sys


def make_map(lines):
    return [[x == "#" for x in line.strip()] for line in lines]


def tree(m, x, y):
    return m[y][x]


def count_slope(slope_x, slope_y, map):
    width = len(map[0])
    trees = 0
    try:
        x = 0
        y = 0
        while True:
            if tree(map, x % width, y):
                trees += 1
            x += slope_x
            y += slope_y
    except IndexError:
        pass

    return trees


lines = sys.stdin.readlines()
map = make_map(lines)

print(count_slope(3, 1, map))

total = 1
for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    total *= count_slope(x, y, map)
print(total)
