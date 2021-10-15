# print("Hi Python")
# #Study coment
# print("My Python is Bad, yet!")
# words = ['мадам', 'топот', 'test', 'madam', 'word']
# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# palindromes = []

# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
# print(palindromes)

# palindrom = [i for i in words if i== i[::-1]]
# print(palindrom)

# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# palindromes = []
# for i in my_str:
#     str_r = i.replace(' ', '').lower()
#     if str_r == str_r[::-1]:
#         palindromes.append(i)
# s2 = '!!!'.join(palindromes)
# print(s2)

#
# for i in range(1, 10):
#     for s in range(1, 10):
#         print(f'{i} * {s} = {i * s}\t', end=' ')
#     print('')
# words = ['мадам', 'топот', 'test', 'madam', 'word',1, 25, 15 , 25 ]
# s2 = []
# for word in words.split():
#     try:
#         s2.append(word)
#     except: ValueError
#     pass
# print(s2)

s = 72
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

