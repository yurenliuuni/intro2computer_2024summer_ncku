
#get the user input
ui_U = input("Enter matrix U: ")
ui_V = input("Enter matrix V: ")

U_rows=ui_U.split("|")
V_rows=ui_V.split("|")

#initiate the matrix U with dictionary
U = {}
for i in range(len(U_rows)):
    entries = U_rows[i].split(",")
    U[i] = [] #initiate the first row list
    for j in entries:
        U[i].append(int(j))
V = {}
for i in range(len(V_rows)):
    entries = V_rows[i].split(",")
    V[i] = [] #initiate the first row list
    for j in entries:
        V[i].append(int(j))

#matrix multiplication
def multiplication(U,V):
    M={}
    for row in range(len(U)):
        M[row] = []
        for col in range(len(V)):
            entry_sum =0
            for i in range(len(U[0])): # Should iterate over columns of U or rows of V
                entry_sum += U[row][i] * V[i][col]
            M[row].append(entry_sum)
    return M

print("M = U x V")
M = multiplication(U,V)
for key in M:
    print(M[key])


# def parse_input(input_string):
#     """將字串格式的矩陣輸入轉化為二維列表"""
#     return [list(map(int, row.split(','))) for row in input_string.split('|')]

# def matrix_multiply(U, V):
#     """計算兩個矩陣的乘積"""
#     size = len(U)
#     result = [[0] * size for _ in range(size)]
#     for i in range(size):
#         for j in range(size):
#             result[i][j] = sum(U[i][k] * V[k][j] for k in range(size))
#     return result

# def main():
#     # 獲取用戶輸入
#     U_input = input("Enter matrix U: ")
#     V_input = input("Enter matrix V: ")
    
#     # 解析矩陣
#     U = parse_input(U_input)
#     V = parse_input(V_input)
    
#     # 計算乘積
#     M = matrix_multiply(U, V)
    
#     # 以字典形式輸出結果
#     result_dict = {i: M[i] for i in range(len(M))}
#     for key, value in result_dict.items():
#         print(f"Row {key}: {value}")

# main()

        

