import my_module
v = int(input("Введіть значенння: "))
print("Сума цифр:", {my_module.sum_digits(v)})
print("Найбільша цифра:", {my_module.max_digit(v)})
print("Найменша цифра:", {my_module.min_digit(v)})