def main(x):
    A = x & 0b111111111
    B = (x >> 9) & 0b1111111
    C = (x >> 16) & 0b1111111111111
    D = (x >> 29) & 0b1
    E = (x >> 30) & 0b11
    result = 0
    result |= D
    result |= B << 24
    result |= A << 15
    result |= C << 2
    result |= E << 0
    return result

print(hex(main(0x0c73e236)))
print(hex(main(0xd996d8ff)))
