
# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???

sentence2 = 'Мы приехали в гости'
sentence2_list = sentence2.split()
for i in range(len(sentence2_list)):
    print(list(sentence2_list[i][0]))
