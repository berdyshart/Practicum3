a_sec = int(input())
a_hours = a_sec//3600
a_mins = a_sec//60 - a_hours*60
a_secfinal = a_sec - a_mins*60 - a_hours*3600
print(f"{a_hours} часов {a_mins} минут {a_secfinal} секунд")