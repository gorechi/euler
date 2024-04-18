""" Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. 
Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000. """


def find_dividers (number):
    dividers = []
    for i in range(1, number):
        if number % i == 0:
            dividers.append(i)
    return dividers

def find_friend(number):
    candidate = sum(find_dividers(number))
    if sum(find_dividers(candidate)) == number and candidate != number:
        print(number, candidate)
        return True
    return False

friends = []
for i in range (1, 10000):
    if find_friend(i):
        friends.append(i)

print(friends)
print('Сумма все дружественных чисел: ', sum(friends))
    