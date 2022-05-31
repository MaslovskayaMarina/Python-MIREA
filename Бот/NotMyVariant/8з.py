def main(s):
    i = 0
    s = s.replace("\n", "")
    k = 0
    x = ""
    result = {}
    while i < len(s):
        key = ""
        if s[i] == '#':
            i += 1
            while s[i] == ' ':
                i += 1
            while s[i] != ' ' and s[i] != '=':
                x = x + s[i]
                i += 1
        if s[i] == ':':
            i += 1
            while s[i] == ' ':
                i += 1
            while s[i] != ';':
                key = key + s[i]
                i += 1
            result[key] = int(x)
            x = ""
        i += 1
    return result

print(main("((.do declare #-379 =: quarbi_915; .end, .do declare #9028=: xegeso_950;.end, ))"))
