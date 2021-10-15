# print(5 + 10)
# print(5 - 2)
# print(5 * 5)
# print(10 / 2)
# print(40 % 6)
# print(5 ** 4)
# print(10 // 5)
# name = 'Igor'
# age = 30
# salary = 3500
# # print('My name is {0}, I am {1}, and i want have salary {2}'.format(name,age,salary))
# # print('My name is {x}, I am {y}, and i want have salary {w}'.format(x=name,y=age,w=salary))
# # print(f'My name is {name}, I am {age} , and i want have salary {salary}')
# # print('453+234={}'.format(453+234))
# # print(f'453+234={453+234}')
# price = int(input('Сколько зарплаты хочешь?'))
#
# if salary>price:
#     print(f'Нет, это мало, я щас зарабатываю {salary}, а вы мне предлагаете на {salary-price} меньше')
# elif salary == price:
#     print('Накиньте немног')
# else:
#     print(f'Я согласен, это больше на {price-salary} чем моя нынешняя зарплата')
#
#
# time = int(input('Которий час?'))
#
# if not time:
#     print('True')
# else:
#     print('False')

#
# i = 1900
#
# while i<=1991:
#      print(i)
#      i+=1

# i = (1 , 2, 3)
# print(i[0]* 2,i[1]*2,i[2]*2)
# i = (1 , 2, 3)
# print(i[0]*2,i[1]*2,i[2]*2)
# print(f'{i[0]*2 + i[1]*2  + i[2]*2}')
# s = input('What is your name?')
# v = input('How old are you?')
# print('.')
# print('..')
# print('....')
# print(f'Welcome {s} in {v} age you can all')
# print(f'Good luck {s}')

# for x in "Hello World":
#     if x ==' ':
#      print(x, end='')
# i = 'Helloworld'
# if ' ' in i:
#     i = i.upper()
# else:
#     i = i.lower()
#
# print(i)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [2, 1, 5, 8, 23, 12, 54, 98, 3, 6, 7, 1]
q = []
for c in b:
    for s in a:
        if c == s:
            q.append(c)

print(q)