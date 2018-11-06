try:
    x = 10
    y = 0
    z = 40/0


except ArithmeticError:
    print("error",ZeroDivisionError)
else:
    print(z)

