a = input()
b = int(a,16)
for i in range(1,16):
    r = b*i
    result = '{0:x}*{1:x}={2:x}'.format(b, i, r)
    print(result.upper())