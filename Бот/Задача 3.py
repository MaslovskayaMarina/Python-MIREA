def main(b, m, z, a, p):
    res1 = 0
    for k in range(1, m + 1):
        for j in range(1, b + 1):
            res1 = res1 + k ** 4 - (k ** 2 + z ** 3 + 1) ** 5 - j
    res2 = 0
    for j in range(1, a + 1):
        res2 = res2 + 99 * (j ** 5) + (79 * p - j ** 3) ** 4 + p ** 3
    return (res1 - res2)

main(6, 8, -0.72, 2, 0.73)
main(3, 8, -0.07, 6, 0.87)
