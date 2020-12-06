import sys


def partition(lines):
    chunk = []
    out = []
    for line in lines:
        if line == "":
            out.append(" ".join(chunk))
            chunk = []
        else:
            chunk.append(line)

    return out


def passport(rec):
    parts = [x.split(":") for x in rec.split(" ")]

    out = {}
    for p in parts:
        out[p[0]] = p[1]
    return out


def valid(p):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(r in p for r in required)


def data_valid(p):
    try:
        return valid(p) and byr_valid(p["byr"]) and iyr_valid(p["iyr"]) and eyr_valid(p["eyr"]) and hgt_valid(p["hgt"]) and hcl_valid(p["hcl"]) and ecl_valid(p["ecl"]) and pid_valid(p["pid"])
    except:
        print(p)
        raise


def byr_valid(byr):
    val = int(byr)
    return 1920 <= val <= 2002


def iyr_valid(iyr):
    val = int(iyr)
    return 2010 <= val <= 2020


def eyr_valid(eyr):
    val = int(eyr)
    return 2020 <= val <= 2030


def hgt_valid(hgt):
    if hgt[-2:] == "cm":
        val = int(hgt[:-2])
        return 150 <= val <= 193
    elif hgt[-2:] == "in":
        val = int(hgt[:-2])
        return 59 <= val <= 76
    else:
        return False


def hcl_valid(hcl):
    return len(hcl) == 7 and hcl[0] == "#" and all(x in "0123456789abcdef" for x in hcl[1:])


def ecl_valid(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_valid(pid):
    return len(pid) == 9 and all(x in "0123456789" for x in pid)


recs = partition([x.strip() for x in sys.stdin.readlines()])
passports = [passport(rec) for rec in recs]
print(len([p for p in passports if valid(p)]))
print(len([p for p in passports if data_valid(p)]))

