import hashlib

# SHA-1

data = 'test'.encode()
hashObject = hashlib.sha1()  # 해시 함수
hashObject.update(data)  # byte로 변환
hexDig = hashObject.hexdigest()  # 16진수로 추출
print(hexDig)

# SHA-256
data2 = 'test'.encode()
hashObject2 = hashlib.sha256()
hashObject2.update(data)
hexDig2 = hashObject2.hexdigest()
print(hexDig2)
