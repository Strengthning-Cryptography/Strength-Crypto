from client import *
from crypt0graphy import *

crypto.pubrsakey = './RSAkey/server/public'
crypto.prirsakey = './RSAkey/client/private'

s = connect()

data, rk = DHc(s.recv(1024))
s.sendall(data)
print("Shared Key :", U.long_to_bytes(rk))

key = SHA256.new(U.long_to_bytes(rk))
aes = AES.new(key.digest(), AES.MODE_EAX)

while True:
    data = input("Message to server : ").encode()
    aes = AES.new(key.digest(), AES.MODE_EAX)
    s.sendall(aes.nonce+aes.encrypt(data))

    if data.strip() == b'Exit': break

    edata = s.recv(1024)
    nonce, edata = edata[:16], edata[16:]
    aes = AES.new(key.digest(), AES.MODE_EAX, nonce=nonce)
    data = aes.decrypt(edata).decode()

    if data.strip() == "Exit":
        break

    print("Response from server :", data.strip())
