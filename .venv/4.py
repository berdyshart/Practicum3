X, Y, N = map(int, input().split())
Y_total = X*100 + Y
M = Y_total*N
print(f"{M//100} руб. {M%100} коп.")