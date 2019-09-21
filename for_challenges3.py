# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???

i = 0
for i in range(len(names)):    
  if is_male[names[i]] == True:
    print(names[i], 'мужской')
    i+= i 
  else:
    print(names[i], 'женский')
    i+= i
