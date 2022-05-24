import argparse
parser = argparse.ArgumentParser()
backend = parser.add_mutually_exclusive_group()
backend.add_argument("-1", dest='b1', action='store_true', help='Use qmachine1')
backend.add_argument("-2", dest='b2', action='store_true', help='Use qmachine2')
parser.add_argument("-g", dest='gui', action='store_true', help='For GUI')
parser.add_argument("-s", dest='show', action='store_true', help='Show Qcircuit')
parser.add_argument("-p", dest='plot', action='store_true', help='Plot Qcir result')

args = parser.parse_args()


print("I> Loading Modules ...")

import sys
import random
import signal

from quantum import *
from crypt0graphy import *
from server import *

print("I> All Modules Loaded")


### loading IBM Q account

if args.b1 or args.b2:
    print("I> Loading IBM Q account ...")
    qiskit_.qaccount = IBMQ.load_account()
    qiskit_.qbackend1 = qiskit_.qaccount.get_backend('ibmq_bogota')
    qiskit_.qbackend2 = qiskit_.qaccount.get_backend('ibmq_belem')
    print("I> IBM Q account loaded")


### quantum code

qcir = get_qcir()
if args.show:
    show(qcir)                  # matplotlib window

if args.b1:
    r = output(qcir, 1)
elif args.b2:
    r = output(qcir, 2)
else:
    r = output(qcir)

if args.plot:
    plot(r)                     # matplotlib window

if args.show or args.plot:
    #def exception(*a): raise Exception
    #signal.signal(signal.SIGALRM, exception)
    #signal.alarm(2)
    try: plt.show()
    except: print("I> Matplotlib Windows shown")
    else: print("I> Matplotlib windows shown")

print("I> Quantum Code done")


### seeding randomess

seed = U.long_to_bytes(num(r))
random.seed(seed)

print("Seed :", seed)
print("I> Seeding randomess done")


### server-client

print("I> Waiting for client to connect ...")

c = client()

print("I> Connected to client")


### sharing pure random key for AES

print("I> Sharing pure randomness ...")

crypto.pubrsakey = './RSAkey/client/public'
crypto.prirsakey = './RSAkey/server/private'

c.sendall(DHs1())
rk = DHs2(c.recv(1024))

print("Shared Key :", U.long_to_bytes(rk))
print("I> Shared by diffie-hellman")

key = SHA256.new(U.long_to_bytes(rk))


#### GUI

if args.gui:
    import server_gui
    server_gui.main()
    s.close()
    c.close()
    plt.close()
    sys.exit()


#### CLI

while True:
    edata = c.recv(1024)
    nonce, edata = edata[:16], edata[16:]
    aes = AES.new(key.digest(), AES.MODE_EAX, nonce=nonce)
    data = aes.decrypt(edata).decode()

    if data.strip() == "Exit":
        break
    
    print("Data from client   :", data.strip())
    data = input("Response to client : ").encode()
    aes = AES.new(key.digest(), AES.MODE_EAX)
    c.sendall(aes.nonce+aes.encrypt(data))

    if data.strip() == b'Exit': break


s.close()
c.close()
plt.close()

print("I> Socket closed")
print("I> Quiting...")
