var_int = 10
var_float = 8.4
var_str = "No"
var_big = var_int*3.5
var_float-=1 #var_float=var_float-1
var_str = var_str*2 + "Yes"*3

print(f"var_big = {var_big}")
print(f"var_int = {var_int}")
print(f"var_str = {var_str}")
print(f"var_float = {var_float}")
print(f"Number 4: {var_int/var_float}, {var_big/var_float}")