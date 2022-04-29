import struct


def A(x, i):
    size = struct.unpack('> H', x[i+3: i+5])[0]
    add = struct.unpack('> H', x[i+5: i+7])[0]
    a3 = ''
    for j in range(0, size):
        a3 += struct.unpack('> '+'c'*size, x[add: add+size])[j].decode('ascii')
    return {
        'A1': struct.unpack('> b', x[i: i+1])[0],
        'A2': struct.unpack('> H', x[i+1: i+3])[0],
        'A3': a3,
        'A4': B(x, address16(x, i+7)),
        'A5': [C(x, i+9), C(x, i+23)],
        'A6': list(struct.unpack('> 3q', x[i+37: i+61])),
        'A7': struct.unpack('> b', x[i+61: i+62])[0]
    }


def B(x, i):
    return {
        'B1': struct.unpack('> d', x[i: i+8])[0],
        'B2': struct.unpack('> b', x[i+8: i+9])[0],
        'B3': struct.unpack('> Q', x[i+9: i+17])[0],
        'B4': struct.unpack('> B', x[i+17: i+18])[0]
    }


def address16(x, i):
    return struct.unpack('> H', x[i: i+2])[0]


def C(x, i):
    return {
        'C1': D(x, address16(x, i)),
        'C2': struct.unpack('> q', x[i+2: i+10])[0],
        'C3': u16u16u32(x, i+10)
    }


def D(x, i):
    return {
        'D1': struct.unpack('> f', x[i: i+4])[0],
        'D2': struct.unpack('> f', x[i+4: i+8])[0],
    }


def u16u16u32(x, i):
    size = struct.unpack('> H', x[i: i+2])[0]
    add = struct.unpack('> H', x[i+2: i+4])[0]
    a = struct.unpack('> '+'I'*size, x[add: add+4*size])
    return list(a)


def main(x):
    return A(x, 3)



print(main(b'ZTR\xf0\xf3c\x00\x02\x00A\x00C\x00U\xb8WE\x91\xbf\xa2\xb1\xf2\x00\x06\x00]\x00u \xf88@\x98 \xd3\x8d\x00\x04\x00}Uz\x1c\xae\xb4\x15\xfaw$\xe2\xf7\x04\xc9xB1\x9e\xbb\xccTk\x901\x1dVjj?\xce\x07j\xf3\xb4=\xc8\xa6o_\x11\x8c\x83o\x16\xc5I\xbff\x9d\xdc>\xa5\xb1\xb6\xa6x\xefw\x0c\xc8\x82Pb>\xfc\xbdj\xe0\xb9>I\xb7\xcd\xbf\r\xa1\x14M?-"\x8d\xbe\xd1\xfe\xb3\x82\x9a\xbe\n\xa1\xde\x8d\xaa\xc6\x93m\xd1\xf1x\x19\xa2'))
