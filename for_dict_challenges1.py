# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

i = 0
j = 0
repeat = 0
result_dict = {}
for i in range(len(students)):
  for j in range(len(students)):
    if students[i] == students[j]:
      repeat += 1
  
  result_dict[students[i]['first_name']] = repeat
  repeat = 0 

for key in result_dict:
  print(key, result_dict[key])
 
