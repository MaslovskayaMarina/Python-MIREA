def cat(s):
    s = list(filter(None, s))
    s[0] = s[0][s[0].index('.') + 2:] + ' ' + s[0][:s[0].index(' ')]
    temp = s[1][8] + s[1][9] + '/' + s[1][3]
    s[1] = temp + s[1][4] + '/' + s[1][0] + s[1][1]
    s[2] = s[2][:s[2].index('[')] + '@' + s[2][s[2].index(']') + 1:]
    if s[3] == 'Выполнено':
        s[3] = 'Да'
    else:
        s[3] = 'Нет'
    s.pop(4)
    return s


def main(s):
    for i in range(len(s)):
        s[i] = cat(s[i])
    s.reverse()
    for x in s:
        if s.count(x) > 1:
            s.remove(x)
    s.reverse()
    s2 = [[row[i] for row in s] for i in range(len(s[0]))]
    return s2

print(main([['Всеволод Л. Сасберг', '15/08/2002', 'vsevolod66[at]mail.ru', 'Выполнено', 'Выполнено'],
            ['Данила Л. Кисонян', '09/01/2004', 'kisonan94[at]rambler.ru', 'Выполнено', 'Выполнено'],
            ['Владимир Т. Сичберг', '15/05/2002', 'vladimir79[at]mail.ru', 'Выполнено', 'Выполнено'],
            ['Владимир Т. Сичберг', '15/05/2002', 'vladimir79[at]mail.ru', 'Выполнено', 'Выполнено'],
            ['Владимир Т. Сичберг', '15/05/2002', 'vladimir79[at]mail.ru', 'Выполнено', 'Выполнено']]))
