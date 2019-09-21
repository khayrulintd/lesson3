# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ],
  [  # это – 3 класс
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Петя'},
  ],
  [  # это – 4 класс
    {'first_name': 'Таня'},
    {'first_name': 'Катя'},
    {'first_name': 'Катя'},
    {'first_name': 'Катя'},
  ]

]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
#k = 0
#for k in range (len(school_students)):
i = 0
j = 0
k = 0
repeat = 0
result_dict = {}


for k in range(len(school_students)):
  #print(school_students[k])
  for i in range(len(school_students[k])):  
    for j in range(len(school_students[k])):
      if school_students[k][i] == school_students[k][j]:
        repeat+= 1
  
    result_dict[school_students[k][i]['first_name']] = repeat
    repeat = 0
    i = 0
    j = 0 

  max_repeat = max(result_dict, key=result_dict.get)
  print(f'Самое частое имя в классе {k+1}: {max_repeat}')
  result_dict = {}
  k=k+1





