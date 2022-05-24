import crypto
from crypto import *

class DS_Verification_Error(Exception):
    pass

def DHs1():
    p,g,a = diffie_hellman_0()
    DHs1.p, DHs1.a = p, a
    x = diffie_hellman_1(p,g,a)
    data = str((p,g,x)).encode()
    signer_ = signer(crypto.prirsakey)
    return sign_with_data(signer_, data)

def DHc(sdata):
    verifier = signer(crypto.pubrsakey)
    ver, data = verify(verifier, sdata)
    if not ver: raise DS_Verification_Error
    p,g,x = eval(data.decode())
    
    b = random.randrange(2,p)
    rk = diffie_hellman_2(p,x,b)
    y = diffie_hellman_1(p,g,b)
    data = str(y).encode()
    signer_ = signer(crypto.prirsakey)
    return sign_with_data(signer_, data), rk

def DHs2(cdata):
    verifier = signer(crypto.pubrsakey)
    ver, data = verify(verifier, cdata)
    if not ver: raise DS_Verification_Error

    y = int(data.decode())
    rk = diffie_hellman_2(DHs1.p,y,DHs1.a)
    return rk
