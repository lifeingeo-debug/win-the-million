print("столица-германи?")
a =['A. Берлин', 'B. Вена', 'C. Брюссель', 'D. Лиссабон'] 
right_answer = 'A'
for i in range (len(a)):
    print(a[i])
answer = input("Ваш ответ?: ")
if answer == right_answer:
    print("Правильный ответ!")
else:
    print("Неправильный ответ!")

