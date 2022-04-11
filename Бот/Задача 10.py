def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def todo(s):
    s = list(filter(None, s))
    for i in range(len(s)):
        if '@' in s[i]:
            s.append(s[i][:s[i].index('@')])
            s[i] = toFixed(round(float(s[i][s[i].index(':') + 1:]), 2), 2)
        elif '.' in s[i] and '@' not in s[i]:
            s[i] = s[i][0] + '.' + s[i][s[i].index(' '):]
        elif '/' in s[i]:
            s[i] = s[i].replace('/', '.')
            a = s[i][s[i].index('.') + 1:][s[i].index('.') + 1:]
            b = '.' + s[i][s[i].index('.') + 1:][:s[i].index('.') + 1]
            c = s[i][:s[i].index('.')]
            s[i] = c + b + a
    s.reverse()
    for x in s:
        if s.count(x) > 1:
            s.remove(x)
    s.reverse()
    return s


def main(s):
    for i in range(len(s)):
        s[i] = todo(s[i])
    s = list(filter(None, s))
    s.sort()
    s.reverse()
    for x in s:
        if s.count(x) > 1:
            s.remove(x)
    s.reverse()
    s2 = [[row[i] for row in s] for i in range(len(s[0]))]
    return s2

