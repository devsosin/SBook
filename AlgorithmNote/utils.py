# Python 회전함수 리스트(튜플)
def rotate(key):
    return list(zip(*key[::-1]))

# Python 회전 (직접 구현) 리스트(리스트)
def rot90(square):
    len_row = len(square)
    len_col = len(square[0])
    temp = [[0 for _j in range(len_row)] for _i in range(len_col)]
    
    for i, row in enumerate(square):
        for j, value in enumerate(row):
            
            temp[j][len_row-i-1] = value
    return temp
