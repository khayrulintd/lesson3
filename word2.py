# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???

word2 = 'Архангельск'
a_tuple = ('А','а')
word2_list = list('Архангельск')
i = 0
counted_a = 0
for i in range(len(word2_list)):
    if word2_list[i] in a_tuple:
        counted_a = counted_a + 1
        i = i + 1

print(counted_a)
