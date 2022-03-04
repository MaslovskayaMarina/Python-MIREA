import math


def main(y):
    if y < 152:
        return 19 + 71 * (math.atan(57 * y + 1 + 14 * y ** 2)) ** 7
    if y >= 152 and y < 191:
        return 65 * y ** 5 + 20
    if y >= 191:
        return 21 * math.log(36 * y ** 3 + (y ** 2) / 92) ** 2
