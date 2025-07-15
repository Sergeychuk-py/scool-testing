# Итерируем список
d = [4, 5, 7, 8, 9, 87]
it = iter(d)
print(next(it))
print(next(it))
print()


# Функция генератор

def get_list():
    for x in [1, 2, 3, 4, 5]:
        yield x


a = get_list()
print(next(a))
print(next(a))


def find_word(f, word):
    """"func - generator, looks for the word generator"""
    g_indx = 0  # проверяет смещение индекса в соответствии со строкой
    for line in f:  # читаем файл по строчно
        indx = 0
        while (indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1
        g_indx += len(line)


try:
    with open('lesson.txt', encoding="utf-8") as file:
        a = find_word(file, 'генератор')
        print(list(a))
except FileNotFoundError:
    print('File not find')
except:
    print('Mistake working')

def gena():
    for i in range(0, 4):
        yield i

a = gena()
print(next(a))
print(next(a))

for i in gena():
    print(i, end= ",")