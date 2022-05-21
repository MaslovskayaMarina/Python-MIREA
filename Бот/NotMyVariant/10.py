def cat(s):
    s = list(filter(None, s))
    if s[1] == 'нет':
        s.append('N')
    else:
        s.append('Y')
    s[1] = s[0][:s[0].index('[')] + '@'
    s[1] = s[1] + s[0][s[0].index(']') + 1:s[0].index(';')]
    s[0] = s[0][s[0].index(';') + 1:]
    s[0] = s[0][6:] + '.' + s[0][3:5] + '.' + s[0][0:2]
    return s


def main(s):
    for i in range(len(s)):
        s[i] = cat(s[i])
    s.reverse()
    for x in s:
        if s.count(x) > 1:
            s.remove(x)
    s.reverse()
    return s

print(main([['salegan82[at]yandex.ru;03.08.2002', 'нет'],
            ['komanz97[at]mail.ru;22.05.2003', 'да'],
            ['nizecman83[at]gmail.com;13.04.2004', 'нет'],
            ['nizecman83[at]gmail.com;13.04.2004', 'нет'],
            ['nizecman83[at]gmail.com;13.04.2004', 'нет'],
            ['vafev77[at]gmail.com;22.02.2000', 'нет']]))
