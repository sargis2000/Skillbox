print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

try:
    x_diff = x1 - x2
    y_diff = y1 - y2
    k = y_diff / x_diff
    b = y2 - k * x2
except ZeroDivisionError:
    print("x1 cant be equal to x2")
else:
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)
