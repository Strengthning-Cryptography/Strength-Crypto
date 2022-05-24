from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import Crypto.Util.number as U
from sympy.ntheory import primitive_root
import random

pubrsakey = None
prirsakey = None

def signer(rsakey_loc): # or verifier
    with open(rsakey_loc, 'r') as rsakey_:
        rsakey = RSA.importKey(rsakey_.read())
    return PKCS1_v1_5.new(rsakey)

def sign(signer, data):
    return signer.sign(SHA256.new(data))

def sign_with_data(signer, data):
    return data+sign(signer, data)

def verify(verifier, signeddata):
    data, sign = signeddata[:-128], signeddata[-128:]
    return verifier.verify(SHA256.new(data), sign), data

def diffie_hellman_0():
    p = U.getPrime(52)
    g = primitive_root(p)
    a = random.randrange(2, p)
    return p, g, a

def diffie_hellman_1(p,g,n):
    m = pow(g,n,p)
    return m

def diffie_hellman_2(p,m,n):
    return pow(m,n,p)

