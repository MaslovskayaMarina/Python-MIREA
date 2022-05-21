def main(x):
    A = x & 0b111111
    B = (x >> 6) & 0b1111111111111111
    C = (x >> 22) & 0b111111
    D = (x >> 28) & 0b111
    E = (x >> 31) & 0b1
    result = 0
    result |= A << 26
    result |= E << 25
    result |= B << 9
    result |= D << 6
    result |= C << 0
    return result

print(hex(main(0x5f5c6e7a)))
print(hex(main(0x6a85235b)))
