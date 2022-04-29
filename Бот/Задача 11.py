import struct


def D(x, i):
    return {
        "D1": struct.unpack("> f", x[i: i+4])[0],
        "D2": struct.unpack("> B", x[i+4: i+5])[0],
        "D3": struct.unpack('>H', x[i+5: i+7])[0],
        "D4": struct.unpack("> h", x[i+7: i+9])[0],
    }


def C(x, i):
    size = struct.unpack("> I", x[i: i+4])[0]
    address = struct.unpack("> I", x[i+4: i+8])[0]
    c1 = struct.unpack("> "+"h"*size, x[address: address+2*size])
    return {
        'C1': [D(x, addressD(x, address+j*2) ) for j in range (0, size)],
        'C2': struct.unpack("> B", x[i+8: i+9])[0],
        'C3': struct.unpack("> b", x[i+9: i+10])[0],
        'C4': E(x, addressE(x, i+10)),
        'C5': F(x, addressE(x, i+14)),
        'C6': struct.unpack('>Q', x[i+18: i+26])[0],
        'C7': struct.unpack('>I', x[i+26: i+30])[0]
    }


def addressE(x, i):
    return struct.unpack("> I", x[i:i+4])[0]


def addressD(x, i):
    return struct.unpack("> H", x[i:i+2])[0]


def B(x, i):
    return {
        "B1": struct.unpack("> I", x[i: i+4])[0],
        "B2": struct.unpack("> d", x[i+4: i+12])[0],
    }


def addressC(x, i):
    return struct.unpack("> H", x[i:i+2])[0]


def A(x, i):
    return {
        'A1': B(x, i),
        'A2': struct.unpack('>4s', x[i+12: i+16])[0].decode('ascii'),
        'A3': struct.unpack("> f", x[i+16: i+20])[0],
        'A4': struct.unpack('>I', x[i+20: i+24])[0],
        'A5': C(x, addressC(x, i+24)),
    }


def S_u16Add_u32Ar_i16(x, i):
    size = struct.unpack("> H", x[i: i+2])[0]
    address = struct.unpack("> I", x[i+2: i+6])[0]
    a = struct.unpack("> "+"h"*size, x[address:address+2*size])
    return list(a)


def E(x, i):
    return {
        'E1': struct.unpack("> h", x[i: i+2])[0],
        'E2': S_u16Add_u32Ar_i16(x, i+2),
        'E3': struct.unpack("> B", x[i+8: i+9])[0],
        'E4': struct.unpack("> h", x[i+9: i+11])[0],
        'E5': struct.unpack("> q", x[i+11: i+19])[0],
        'E6': struct.unpack("> d", x[i+19: i+27])[0],
        'E7': list(struct.unpack('> 8b', x[i+27: i+35]))
    }


def F(x, i):
    return {
        'F1': struct.unpack('>Q', x[i: i+8])[0],
        'F2': struct.unpack('>I', x[i+8: i+12])[0],
        'F3': struct.unpack("> B", x[i+12: i+13])[0],
        'F4': S_u32Add_u16Ar_float(x, i+13)
    }


def S_u32Add_u16Ar_float(x, i):
    size = struct.unpack("> L", x[i: i+4])[0]
    address = struct.unpack("> H", x[i+4: i+6])[0]
    a = struct.unpack("> "+"f"*size, x[address: address+4*size])
    return list(a)


def main(x):
    return A(x, 4)


print(main(b'\xa0VATZ\x1c\x03\x9c?\xaa\xa1tG\x81\xdb\x00epek\xbe\xeatQ_\xe6Y5\x00z>\x15'
 b"OMPx\xd0#\x9c\xbd\x8c\x8a\xe2+\xb20]\x81\x00\x1e\x00'\x1c\xb1\xaa\xa5"
 b'*\xda6\x97o\x9a\x00\x04\x00\x00\x004#{*\x8c\xa3r=(\x9d\x89\x92?\xd3Z\xc4\xe3'
 b'\t\xda\xe4\nA\x81\x17.\x94"a?DP\x1a?ev$\x7f}b\x174\xfe\xe7@\xd7\xfc^\x08I'
 b'\x00\x00\x00\x02\x00_\x00\x00\x00\x02\x00\x00\x000\x81S\x00\x00\x00<'
 b'\x00\x00\x00g\x98e\x98M\xe6\xccH\x91\xf5\xa4W\x01'))
