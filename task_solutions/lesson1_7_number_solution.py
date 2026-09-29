a = float(input("Enter the first number: ")) #тут на вход мы принимает значение 3-х переменных, тк неизвестно, какого типа переменных введет пользователь(float или int), мы используем float
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
summ = a + b + c #суммируем значение всех переменных в одну
print(f"The summ of these three numbers equals {summ}") #выводим результат с помощью print и f-строки
