"""
Написать программу, которая:
- Создаёт список из 6 строк (*строки определяются в коде, на ваш вкус*).
- Подсчитывает количество строк, содержащих букву `в`.
- Использует циклы для подсчета.
"""

spisok = ["биба","боба","вова","вилка","лавка","пуп"] #сам список

spisok_count = 0 #начало подсчета
for i in spisok: #использование из списка
    if "в" in i: #если есть буква в
        spisok_count += 1 #работа подсчета
print(spisok_count) #вывод
