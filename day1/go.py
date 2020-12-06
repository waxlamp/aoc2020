import itertools
import sys

nums = [int(x) for x in sys.stdin.readlines()]
for (a, b) in itertools.product(nums, nums):
    if a + b == 2020:
        print a * b
        break
