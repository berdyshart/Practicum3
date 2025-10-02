N = int(input())
min_total = N*2
n_hours = min_total//60
n_mins = int(min_total-n_hours*60)
print(n_hours, n_mins)