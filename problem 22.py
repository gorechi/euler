"""
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. 
Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в 
отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. 
Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
"""

def alphabet_sum(name):
    name = name.lower()
    sum = 0
    for letter in name:
        sum += ord(letter) - ord('a') + 1
    return sum

with open('names.txt') as names:
    lines = []
    for i in names:
        lines.append(i)
names = lines[0][1:-1].split('","')
names.sort()
total = 0
for index, name in enumerate(names):
    total += alphabet_sum(name) * (index + 1)
print(total)