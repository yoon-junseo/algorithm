import hashlib

s = input()

s = s.encode()
hashObject = hashlib.sha256()
hashObject.update(s)
hexDigit = hashObject.hexdigest()
print(hexDigit)

# result = hashlib.sha256(s).hexdigest() 6,7,8 줄 대체
