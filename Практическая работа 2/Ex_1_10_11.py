#Практическая работа 2. Вариант 3: задачи 1, 10, 11
# Задача 1

def ex1():
    # Преобразовать элементы списка s из строковой в числовую форму
    s = ['1', '-1', '2', '-2', '0']
    for i in range(len(s)): s[i] = int(s[i])
    print(s)
    # Подсчитать количество различных элементов в последовательности s
    s = ['true', 'false', '123', '000', '999']
    print(len(set(s)))
    # Обратить последовательность s без использования функций
    s = [9, 8, 7, 6, 5, 4, 3, 23, 1, 0]
    s.reverse()
    print(s)
    # Выдать список индексов, на которых найден элемент x в последовательности s
    s = ['x', 'y', 'x', 'z', 'kx']
    print([i for i in range(len(s)) if s[i] == 'x'])
    # Сложить элементы списка s с четными индексами 
    s = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]      
    print(sum([int(s[i]) for i in range(len(s)) if i % 2 != 1]))
    # Найти строку максимальной длины в списке строк s
    s = ['true', 'false', '123', '000', '999']
    result = max(s, key=len)
    print(result)



# Задача 2

def ex10():
    bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10', 'ПитонН4 н11', 'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']
    group = 'f';
    isgroup = False
    j = 0
    for i in range(len(bad_subj)):
        for j in range (len(bad_subj[i])): # Проверка на группу
            if bad_subj[i][j].isdigit() == True: 
                if group != 'f': isgroup = True
                break
            if bad_subj[i][j] == 'N' or bad_subj[i][j] == 'n' or bad_subj[i][j] == 'Н' or bad_subj[i][j] == 'н':
                if j == 5:
                    if bad_subj[i][0] == "P" or bad_subj[i][0] == "p" or bad_subj[i][0] == "П" or bad_subj[i][0] == "п":
                        continue
                group = 'ИНБО'
            if bad_subj[i][j] == 'V' or bad_subj[i][j] == 'v' or bad_subj[i][j] == 'В' or bad_subj[i][j] == 'в':
                group = 'ИВБО'
            if bad_subj[i][j] == 'K' or bad_subj[i][j] == 'k' or bad_subj[i][j] == 'К' or bad_subj[i][j] == 'к':
                group = 'ИКБО'
            if bad_subj[i][j] == 'N' and bad_subj[i][j] == "n" and bad_subj[i][j] == "Н" and bad_subj[i][j] == "н":
                group = 'ИНБО'
        if isgroup:
            print(group, end = "") # Вывод наименования группы на экран
        group = 'f'
        if j + 1 != len(bad_subj[i]) and isgroup: # Обнаружение номера группы
            while bad_subj[i][j].isdigit() == False and j + 1 != len(bad_subj[i]):
                j += 1
            if bad_subj[i][j].isdigit() == True:
                print('-',bad_subj[i][j], end = "")
                j += 1
            if bad_subj[i][j].isdigit() == True:
                print(bad_subj[i][j], end = "")
                j += 1
            print('-19', end = "") 
        elif isgroup and j+ 1== len(bad_subj[i]) and bad_subj[i][j].isdigit():
            print('-',bad_subj[i][j], '-19', end = "")
        if isgroup: # Обнаружение варианта выполненного задания
            if j+1 >= len(bad_subj[i]):
                print(' Без варианта')
            elif j + 1 != len(bad_subj[i]):
                while bad_subj[i][j].isdigit() == False and j + 1 != len(bad_subj[i]):
                    j += 1
                if bad_subj[i][j].isdigit() == False and bad_subj[i][j+1].isdigit() == False:
                    print(' Без варианта', end = "")
                elif bad_subj[i][j].isdigit() == True:
                    print(' Вариант:',bad_subj[i][j], end = "")
                    j += 1
                if j != len(bad_subj[i]):
                    if bad_subj[i][j].isdigit() == True:
                        print(bad_subj[i][j], end = "")
                print('') 
            elif isgroup and j== len(bad_subj[i]) and bad_subj[i][j].isdigit():
                print(' Вариант:',bad_subj[i][j], '')
        isgroup = False


# Задача 3

def ex11():
    from itertools import groupby # Для удобства вывода

    def rle_encode(info): # Вспомогательная функция для вывода результата на экран
        return [(k, len(list(g))) for k, g in groupby(info)]

    def pr_preobr(str): #Прямое преобразование
        str += '|' # Добавляем разделитель, чтобы отслеживать перестановки
        # Создание "таблицы", которая содержит всё перестановки
        # Используем срезы :, чтобы помещать каждый символ в нужную ячейку
        permutations = [str[index:] + str[:index] for index, _ in enumerate(str)]
        # _ - это пропуск передачи значения. в данном случае счётчик будет начинать с 0
        permutations.sort() # Сортировка по алфавиту
        new_str = [y[-1] for y in permutations] # Прохождение по последнему столбцу "таблицы"
        new_str = ''.join(new_str) # Запись последней буквы каждого столбца в новую строку
        return new_str # Возврат результата
 
    def obr_preobr(str): #Обратное преобразование
        table = list('')
        # Создание списка, который содержит в себе прямое преобразование в качестве "столбца" для таблицы
        for i in range (len(str)):
            table.append(str[i])
        for i in range(len(str) - 1): # Пока "столбец" не пройден до конца выполняется цикл
            table.sort() # Текущий "столбец" сортируем по алфавиту
            table = [str[i] + table[i] for i in range(len(str))] # Добавляем идентичный входному "столбцу" "столбец"
        return table[[x[-1] for x in table].index('|')] # Вернем ту строку, в исходной которой в конце стоял разделитель
 
    st_r = 'CCCCATTTATTATCC' # Входная строка
    print('Строка:', st_r)
    result1 = pr_preobr(st_r)
    for_2 = result1
    result1 = result1.replace('|', '') # Возвращение копии строки, в которой все вхождения подстроки # заменяются новой подстрокой (пустой)
    print('Результат прямого преобразования', result1)
    result2 = obr_preobr(for_2)
    print('Результат обратного преобразования', result2.replace('|', '')) # Возвращение копии строки, в которой все вхождения подстроки # заменяются новой подстрокой (пустой) 
    print('Обычное RLE-сжатие', rle_encode(st_r))
    print('RLE сжатие с пользованием преобразования Барроуза-Уилера', rle_encode(result1))

ex1()
ex10()
ex11()
