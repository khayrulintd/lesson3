# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
  {'first_name': 'Петя'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

i = 0
j = 0
repeat = 0
result_dict = {}

for i in range(len(students)):
  for j in range(len(students)):
    if students[i] == students[j]:
      repeat+= 1
  
  result_dict[students[i]['first_name']] = repeat
  print(repeat)
  repeat = 0 

max_repeat = max(result_dict, key=result_dict.get)

print(f'Самое частое имя среди учеников: {max_repeat}')
