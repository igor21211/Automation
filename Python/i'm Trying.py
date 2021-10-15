import random
# import re
# s = random.randint(0,10)
# user = 0
# count = 0
#
# while True:
#     user = int(input('Я загадал число угадай его: '))
#     count += 1
#     if user == s:
#         print(f'Поздравляю ты угадал число с {count} попытки')
#         break
#     elif user > s:
#         print('Мое число меньше')
#     else:
#         print('Мое число больше')

# jaiko = []
#
# for jai in range(1, 11):
#     jaiko.append(jai **2)
# print(jaiko)
# print(sum(jaiko))
# print(min(jaiko))
# print(max(jaiko))
# products =  {'name': 'Sony', 'Price': 500, 'date_of_birth': 15}
# print(products.items())
# print(products.keys())
# print(products.values())
# products.update({'Name': 'LG'})
# products.update({'price': 340})
# print(products)
# def table_mnog(x):
#     for x in range(1, 10):
#         for y in range(1, 10):
#             print(f'{x} * {y} = {x * y}\t', end=' ')
#         print('')
#
#
# def hello(s):
#     if ' '  in s:
#         return s.upper()
#     else:
#         return s.lower()
#
#
# def get_sum(x , y):
#     print(x + y)
#
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [2, 1, 5, 8, 23, 12, 54, 98, 3, 6, 7, 1]
# q = []
# for c in b:
#     for s in a:
#         if c == s:
#             q.append(c)
# # print(q)
#
#
#
#
# def register_dict(s):
#     list_d = list(s.items())
#     list_d.sort(key=lambda i: i[1])
#     list_d = dict(list_d)
#     print(list_d)
#
#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# c = {2: 10, 4: 5, 3: 7, 3: 9, 1: 0}
# e = {1: 4, 3: 6, 3: 8, 2: 6, 4: 0}


def what_number():
    s = random.randint(0, 10)
    user = 0
    count = 0
    while True:
        user = int(input('Я загадал число угадай его: '))
        count += 1
        if user == s:
            print(f'Поздравляю ты угадал число с {count} попытки')
            break
        elif user > s:
            print('Мое число меньше')
        else:
             print('Мое число больше')
    user_info()


def user_info():
    user_info1 = str(input('Do you want more? Y/N'))
    if 'N' in user_info1:
        print('Thanks for game')
    else:
        what_number()

what_number()