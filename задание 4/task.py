def chess_knight_moves(row,column):
    res = []
    all_rows = [x for x in range(1,9)]
    all_column = [x for x in range(1,9)]
    if row-2 in all_rows:
        if column-1 in all_column:
            res.append([row-2,column-1])
        if column+1 in all_column:
            res.append([row-2,column+1])
    if column-2 in all_column and row-1 in all_rows:
        res.append([row-1,column-2])
    if column+2 in all_column and row-1 in all_rows:
        res.append([row-1,column+2])
    if column-2 in all_column and row+1 in all_rows:
        res.append([row+1,column-2])
    if column+2 in all_column and row+1 in all_rows:
        res.append([row+1,column+2])
    if row+2 in all_rows:
        if column-1 in all_column:
            res.append([row+2,column-1])
        if column+1 in all_column:
            res.append([row+2,column+1])
    return sorted(res)
def can_move(list1,list2):
    row, column = list1 
    move_list = chess_knight_moves(row,column)
    if list2 in move_list:
        return 1 
    else: return 0
print(chess_knight_moves(4,4))
print(chess_knight_moves(1,1))
print(can_move([8,8],[6,7]))
print(can_move([8,8],[6,6]))
