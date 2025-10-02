N, C, K = int(input()),int(input()),int(input())
page = K//(N*C)+1
K1 = K - (page-1)*N*C
column = K1//N+1
line = K1 - N*(column-1)
print(f"страница {page} столбец {column} строка {line}")