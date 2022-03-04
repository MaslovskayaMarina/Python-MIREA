import math


def main(n):
    if n == 0:
        return -0.25
    if n >= 1:
        return main(n - 1) - 42 - (math.cos(main(n - 1)) ** 3) / 13

print(main(5))
print(main(4))
