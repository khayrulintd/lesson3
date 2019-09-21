
# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???

sentence3 = 'Мы приехали в гости'
sentence3_list = sentence3.split()
sum = 0
i = 0
for i in range(len(sentence3_list)):
    sum = sum + (len(sentence3_list[i]))

print(sum/len(sentence3_list))

        
            
