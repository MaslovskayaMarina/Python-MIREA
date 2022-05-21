import struct


def addressB(x, start):
    return struct.unpack("< H", x[start:start+2])[0]


def uint32uint32uint32(x, start):
    size = struct.unpack("< I", x[start: start + 4])[0]
    add = struct.unpack("< I", x[start + 4: start + 8])[0]
    a = struct.unpack("< " + "I" * size, x[add: add + 4 * size])
    return list(a)


def addressC(x, i):
    return struct.unpack("< I", x[i:i+4])[0]


def A(x, start):
    return {
        'A1': B(x, addressB(x, start)),
        'A2': struct.unpack("< d", x[start + 2:start + 10])[0],
        'A3': uint32uint32uint32(x, start + 10),
        'A4': struct.unpack("< h", x[start + 18:start + 20])[0],
        'A5': G(x, start + 20),
        'A6': struct.unpack("< b", x[start + 35:start + 36])[0],
    }


def B(x, start):
    size = struct.unpack("< H", x[start: start+2])[0]
    address = struct.unpack("< H", x[start+2: start+4])[0]
    return {
        'B1': [C(x, addressC(x, address+j*4)) for j in range(0, size)],
        'B2': struct.unpack("< b", x[start + 4:start + 5])[0],
        'B3': struct.unpack("< B", x[start + 5:start + 6])[0],
        'B4': D(x, addressB(x, start + 6)),
        'B5': F(x, start + 8),
        'B6': struct.unpack("< b", x[start + 24:start + 25])[0],
    }


def C(x, start):
    return {
        'C1': struct.unpack("< b", x[start:start + 1])[0],
        'C2': struct.unpack("< b", x[start + 1:start + 2])[0],
    }


def D(x, start):
    return {
        'D1': struct.unpack("< b", x[start:start + 1])[0],
        'D2': struct.unpack("< I", x[start + 1:start + 5])[0],
        'D3': struct.unpack("< q", x[start + 5:start + 13])[0],
        'D4': struct.unpack("< h", x[start + 13:start + 15])[0],
        'D5': E(x, start + 15),
        'D6': struct.unpack("< d", x[start + 42:start + 50])[0],
        'D7': struct.unpack("< I", x[start + 50:start + 54])[0],
    }


def E(x, start):
    return {
        'E1': struct.unpack("< B", x[start:start + 1])[0],
        'E2': uint16uint32uint16(x, start + 1),
        'E3': struct.unpack("< b", x[start + 7:start + 8])[0],
        'E4': struct.unpack("< b", x[start + 8:start + 9])[0],
        'E5': struct.unpack("< h", x[start + 9:start + 11])[0],
        'E6': uint16uint16uint8(x, start + 11),
        'E7': struct.unpack("< f", x[start + 15:start + 19])[0],
        'E8': struct.unpack("< Q", x[start + 19:start + 27])[0],
    }


def F(x, start):
    return {
        'F1': struct.unpack("< d", x[start:start + 8])[0],
        'F2': struct.unpack("< h", x[start + 8:start + 10])[0],
        'F3': struct.unpack("< i", x[start + 10:start + 14])[0],
        'F4': struct.unpack("< h", x[start + 14:start + 16])[0],
    }


def G(x, start):
    return {
        'G1': uint32uint16uint16(x, start),
        'G2': struct.unpack("< h", x[start + 6:start + 8])[0],
        'G3': struct.unpack("< i", x[start + 8:start + 12])[0],
        'G4': struct.unpack("< b", x[start + 12:start + 13])[0],
        'G5': struct.unpack("< h", x[start + 13:start + 15])[0],
    }


def uint16uint32uint16(x, start):
    size = struct.unpack("< H", x[start: start + 2])[0]
    add = struct.unpack("< I", x[start + 2: start + 6])[0]
    a = struct.unpack("< " + "h" * size, x[add: add + 2 * size])
    return list(a)


def uint16uint16uint8(x, start):
    size = struct.unpack("< H", x[start: start + 2])[0]
    add = struct.unpack("< H", x[start + 2: start + 4])[0]
    a = struct.unpack("< " + "B" * size, x[add: add + 1 * size])
    return list(a)


def uint32uint16uint16(x, start):
    size = struct.unpack("< I", x[start: start + 4])[0]
    add = struct.unpack("< H", x[start + 4: start + 6])[0]
    a = struct.unpack("< " + "H" * size, x[add: add + 2 * size])
    return list(a)


def main(x):
    return A(x, 4)


print(main(b'\xcfLUU\x80\x00\xae\x7f\x80\x80\xac\xe0\xe8?\x02\x00\x00\x00\x99\x00'
 b"\x00\x00.k\x02\x00\x00\x00\xa1\x00N\xe99\xe9E\xa4\x15'\xefO\x18\x8e\x08z"
 b'\x1d\xdc(\x00\x00\x00*\x00\x00\x00,\x00\x00\x00\x8a\xb2\x92g\xb5%'
 b'\x0f"\xdc\xda\xb94\xa6p\xd3\xae\xd9\x9d\xba\x9b\xc9\xf8\xcf\xf7^\xa8\xd588-'
 b'M\xf7\x06\x00:\x00\x00\x00\xdeo\xc8V\x04\x00F\x00\xe4\x9f\xa7>\xc0\xf4g\x02'
 b'\xe5\xc1\xe8\x14\x8a\x1a\x1e\xc1z\x8e\xe6?\xbb8\xc3\xd4\x03\x00.\x00:RJ\x00'
 b'B\x02\x00~\x8dv\xe7?\x8f\xb9\xe5\xd6#=\xb5\xac/\xcec\x10D\x92g\xd5\x88YEHs'))
