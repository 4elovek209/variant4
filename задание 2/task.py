def sum_proizv(n):
    sc = 0
    pr_c = 1
    if n == 0:
        return [0,0]
    else:
        while n != 0:
            digit = n % 10
            sc += digit
            if digit != 0:
                pr_c *= digit
            n = n // 10
        return [sc,pr_c]
def osob_svo(a,b):
    result = []
    if a < 0 or b < 0:
        print("Отрицательные числа недопустимы")
        return result
    for i in range(a,b+1):
        sp = sum_proizv(i)
        summary = sp[0]
        product = sp[1]
        if summary == product:
            result.append(i)
    return result
a,b = [int(x) for x in input("Введите два числа через пробел ").split()]
#a,b = 1, 150
answer = osob_svo(a,b)
print(*answer)
print(f"Количество найденых чисел:{len(answer)}")
print(osob_svo(-1, 10))
