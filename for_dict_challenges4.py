# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for k in range(len(school)):
  print(k)
  print(school[k]['students'])

  for i in range(len(school[k]['students'])):
    print(school.get("class"))
    print(school[k]['students'])
    #if is_male[school[k]['students'] == True:
      #print(school[k]['students'][i], 'мужской')
      #print(1)
      #i+= i 
    #else:
      #print(school[k]['students'][i], 'женский')
      #print(2)
      #i+= i




'''
i = 0
for i in range(len(names)):    
  if is_male[names[i]] == True:
    print(names[i], 'мужской')
    i+= i 
  else:
    print(names[i], 'женский')
    i+= i
'''