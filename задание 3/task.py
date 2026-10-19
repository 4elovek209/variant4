def remove_dublicate(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res

print(remove_dublicate([3, 1, 3, 2, 1, 5, 2]))
print(remove_dublicate(["мама", "папа", "мама", "дом", "папа"]))
