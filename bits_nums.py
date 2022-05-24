from qiskit_ import *

def bis(counts, len=None):
    if type(counts) is not dict:
        counts = counts.get_counts()
    results = [(j,i) for i,j in counts.items()]
    results.sort(reverse=True, key=lambda x:x[0])
    binary_string = ''.join(map(str, [i[1] for i in results]))
    return binary_string[:len]

def num(counts, bits=None):
    return int(bis(counts, bits), 2)
