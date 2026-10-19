def interval_merge(list):
    if len(list) == 0:
        return []
    # после сортировки по началу следующий интервал либо продолжает текущий, либо начинается новый
    list.sort(key = lambda x:x[0])
    min_tek = min(list[0])
    max_tek = max(list[0])
    res = []
    list.remove(list[0])
    while len(list) > 0:
        if max_tek < max(list[0]) and min(list[0]) <= max_tek:
            max_tek = max(list[0])
        elif min(list[0]) > max_tek:
            res.append((min_tek, max_tek))
            min_tek = min(list[0])
            max_tek = max(list[0])
        list.remove(list[0])
    res.append((min_tek,max_tek))
    return res
print(interval_merge([(1, 4), (3, 8), (10, 12), (11, 15)]))
print(interval_merge([(1, 10), (2, 3), (4, 5)]))
print(interval_merge([(1, 4), (4, 6)]))
print(interval_merge([]))
