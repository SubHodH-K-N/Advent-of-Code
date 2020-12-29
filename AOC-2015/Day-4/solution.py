import hashlib

secret = "yzbqklnj"
i = 1
while True:
    s = secret + str(i)
    result = hashlib.md5(s.encode()).hexdigest()
    if result[:6] == '000000':
        print(i, " ", result)
        break
    else:
        i += 1
