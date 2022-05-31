import struct


def D(x, i):
    return {
        "D1": list(struct.unpack('> 4i', x[i: i+16])),
        "D2": S_u1Add_u32Ar_i16(x, i+16),
        "D3": struct.unpack('>I', x[i+24: i+28])[0]
    }


def C(x, i):
    return {
        'C1': struct.unpack("> b", x[i: i+1])[0],
        'C2': struct.unpack('>I', x[i+1: i+5])[0]
    }


def B(x, i):
    return {
        "B1": [C(x, addressC(x, i)),
               C(x, addressC(x, i+4)),
               C(x, addressC(x, i+8)),
               C(x, addressC(x, i+12)),
               C(x, addressC(x, i+16)),
               C(x, addressC(x, i+20))],
        "B2": struct.unpack("> i", x[i+24: i+28])[0],
        'B3': D(x, addressC(x, i+28)),
        'B4': struct.unpack("> f", x[i+32: i+36])[0],
        'B5': struct.unpack("> d", x[i+36: i+44])[0],
    }


def addressC(x, i):
    return struct.unpack("> I", x[i:i+4])[0]


def addressB(x, i):
    return struct.unpack("> H", x[i:i+2])[0]


def A(x, i):
    return {
        'A1': struct.unpack("> d", x[i: i+8])[0],
        'A2': struct.unpack('>Q', x[i+8: i+16])[0],
        'A3': struct.unpack("> h", x[i+16: i+18])[0],
        'A4': B(x, addressB(x, i+18)),
        'A5': list(struct.unpack('> 7h', x[i+20: i+34]))
    }


def S_u1Add_u32Ar_i16(x, i):
    size = struct.unpack("> I", x[i: i+4])[0]
    address = struct.unpack("> I", x[i+4: i+8])[0]
    a = struct.unpack("> "+"q"*size, x[address:address+8*size])
    return list(a)


def main(x):
    return A(x, 4)


print(main(b'ZOYj?\xdcms5h\xf4\x1cI%\x9e\x8c4\xc9\xbb\xf6\xdc\xfb\x00\x90\xb1F\xc81'
 b'\xcaS\xab\xc5\x81oe\xcb\xf0\x82\xb3\x8f\xa42\xb16;\x84\xe1\xed\x98V\xda\xc8'
 b'\x0c\x8deg\xb9[\x02\xees\xc2]T,\t\xfe\x8f\xecx8\x0fe[2\x183\xfb@\x17'
 b'\x9b3m\x83\xb2\x07\x0f\xd1\xa1\x90\xb8\xdd\xf93<\xcf\x90\n1\x9bj\xdb\x0cA'
 b'\xa3\xb1r\xba\xf5\xf3\xbdx\xcc\x01\xf8"\':\x11pU\xd3\x94@\xe0z\x8e\x83'
 b'\xad\x00\x06\x82\x00\x00\x00\x06\x00\x00\x00D\xfe\xb3Q)\x00\x00\x00&'
 b'\x00\x00\x00+\x00\x00\x000\x00\x00\x005\x00\x00\x00:\x00\x00\x00?\xed\x187h'
 b'\x00\x00\x00t=\xc23g\xbf\xe1\x10mQ\xa1g\xc4'))
