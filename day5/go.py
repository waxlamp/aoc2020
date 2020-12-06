import sys


def convert(line):
    row = line[0:7]
    col = line[7:10]

    row_b = "".join(['1' if x == 'B' else '0' for x in row])
    col_b = "".join(['1' if x == 'R' else '0' for x in col])

    row_d = int(row_b, 2)
    col_d = int(col_b, 2)

    id = row_d * 8 + col_d

    return id


def find_id(ids):
    i = 0
    while True:
        if i not in ids and (i - 1) in ids and (i + 1) in ids:
            return i
        i += 1


lines = sys.stdin.readlines()
ids = [convert(x) for x in lines]
print(max(ids))
print(find_id(ids))
