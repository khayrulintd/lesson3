
# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???

word3 = 'Архангельск'
vowels_tuple = ('А','а','е')
word3_list = list('Архангельск')
i = 0
counted_vowels = 0
for i in range(len(word3_list)):
    if word3_list[i] in vowels_tuple:
        counted_vowels = counted_vowels + 1
        i = i + 1

print(counted_vowels)
