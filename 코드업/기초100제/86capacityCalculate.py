# 8 bit(비트)           = 1byte(바이트)  // 8bit=1Byte
# 1024 Byte(210 byte) = 1KB(킬로 바이트) // 1024bit=1KB
# 1024 KB(2^10 KB)      = 1MB(메가 바이트)
# 1024 MB(2^10 MB)=2^33 bit    = 1GB(기가 바이트)
# 1024 GB(2^10 GB)      = 1TB(테라 바이트)

w , h, c = input().split()
w = int(w)
h = int(h)
c = int(c)

trans = 2**23

result = (w*h*c)/trans
print(result)
if int((result*100)%10)==0:
    print(round(result,2),'MB')
else:
    print(round(result,2),'MB')

