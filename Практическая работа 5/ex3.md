Использование модуля coverage

1)Получите статистику по покрытию операторов:
coverage run -m pytest ex3.py
coverage report -m ex3.py

2)Получите статистику по покрытию ветвей:
coverage run --branch -m pytest ex3.py
coverage report -m ex3.py

3)Постарайтесь изменить код исходной программы так, чтобы затруднить получение 100% покрытия - 
*Удалить в ex3.py строку assert incr(10) == 10*

4)Реализуйте вывод статистики о покрытии в HTML-представлении:
coverage html ex3.py
