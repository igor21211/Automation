names = ['Mark', 'Ryan', 'Kieran', 'John', 'David', 'Paul']
name1 = []
s = 'even', 7, 'even', 2, 'even', 55, 'even', 6, 'even', 10, 'odd', 3, 'even'
t = 'even', 7, 'even', 2, 'even', 55, 'even', 6, 'even', 9, 'odd', 3, 'even'
c = 'even', 7, 'odd', 2, 'even', 55


def user_names(names):
    return [i for i in names if 4 == len(i)]


def odd_ball(arr):
    return arr.index('odd') in arr


print(odd_ball(['even', 7, 'even', 2, 'even', 55, 'even', 6, 'even', 10, 'odd', 3, 'even']))
print(odd_ball(['even', 7, 'even', 2, 'even', 55, 'even', 6, 'even', 9, 'odd', 3, 'even']))
print(odd_ball(['even', 7, 'odd', 2, 'even', 55]))


def find_sum(n):
    s = [i for i in range(n+1) if i % 3 == 0 or i % 5 == 0]
    return sum(s)


def find_sum1(n):
    s = 0
    for i in range(n+1):
        if i % 3 ==0 or i % 5 ==0:
            s += i
    return s
s = 'madam'


def palindrom(s):
    return s in s[::-1]

print(palindrom(s))