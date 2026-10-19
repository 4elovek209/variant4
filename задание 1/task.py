def tr_pascala(n):
    row:list[int]
    row = [1]
    if n == 0:
        return row
    else:
        while n != 0:
            row.append(1)
            row_new = []
            for i in range(len(row)):
                if i == 0 or i == len(row)-1:
                    row_new.append(1)
                else:
                    row_new.append(row[i-1] + row[i])
            
            row = row_new
            n -= 1
    return(row_new)

def triangle(n):
    rows = []
    for k in range(n):
        rows.append(tr_pascala(k))
    return rows

for row in triangle(4):
    print(*row)
print("Строка номер 3:", tr_pascala(3))
