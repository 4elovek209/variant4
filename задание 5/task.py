import numpy as np

def line_regression(x, y):
    if len(x) != len(y) or len(x) == 0:
        print("Списки x и y должны быть одной длины и не пустые")
        return None
    same = 1
    for value in x:
        if value != x[0]:
            same = 0
            break
    if same == 1:
        print("Все x одинаковые, коэффициент a не считается")
        return None
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    top = 0
    bottom = 0
    for i in range(n):
        top += (x[i] - mean_x) * (y[i] - mean_y)
        bottom += (x[i] - mean_x) ** 2
    a = top / bottom
    b = mean_y - a * mean_x
    return a, b

def line_regression_np(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    if np.all(x == x[0]):
        print("Все x одинаковые, коэффициент a не считается")
        return None
    a, b = np.polyfit(x, y, 1)
    return a, b

def predict(a, b, x):
    return a * x + b

x = [1, 2, 3, 4]
y = [3, 5, 7, 9]
hand = line_regression(x, y)
auto = line_regression_np(x, y)
print("Своя формула:", hand)
print("Numpy:", auto)
print("Предсказание при x = 5:", predict(hand[0], hand[1], 5))
print(line_regression([2, 2, 2], [1, 2, 3]))
