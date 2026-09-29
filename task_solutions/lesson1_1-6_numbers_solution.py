var_int = 10 #создание переменных с заданным значением
var_float = 8.4
var_str = "No"

var_big = var_int*3.5 #первые действия
var_float-=1 #var_float=var_float-1 одно и то же, что var_float-=1, просто укороченный вид
var_str = var_str*2 + "Yes"*3

print(f"var_big = {var_big}") #вывод. f перед кавычками называется f-строкой, упрощает запись и дает возможность вписать переменную в строку
print(f"var_int = {var_int}")
print(f"var_str = {var_str}")
print(f"var_float = {var_float}")
print(f"Number 4: {var_int/var_float}, {var_big/var_float}")
