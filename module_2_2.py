first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
# не знаю, почему в задании указано избеготь вложенных операторов? По-моему,
# вполне удобно получилось. Но если это неправильно, то можно вместо оператора or
# использовать здесь несколько операторов elif для тех же условий
    print(2)
else:
    print(0)
