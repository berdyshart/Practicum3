raw = input('Enter number:')
if all([True if i in "1234567890" else False for i in raw] ):
    num = int(raw)
    print(num)
