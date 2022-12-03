# ADVENT OF CODE
# https://adventofcode.com
#
# Solution to Day 01 - Part 1 challenge
# https://adventofcode.com/2022/day/1

import os

if __name__ == '__main__':
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    current = 0
    highest = 0
    with open(os.path.join(__location__,'./input.txt')) as f:
        for line in f:
            if (line.strip()):
                current = current + int(line)
            else:
                if (current > highest):
                    highest = current
                current = 0

        print(highest)