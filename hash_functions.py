import sys


def h_ascii(key, N):
    """ASCII value sum for characters in key"""
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_rolling(key, N):
    '''polynomial rolling hash algorith,'''
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N 


if __name__ == '__main__':
    
    for l in open(sys.argv[1]):
        if sys.argv[2] == 'ascii':
            print(h_ascii_sum(l, 1000))
        elif sys.argv[2] == 'rolling':
            print(h_polynomial_rolling(l, 1000))
        elif sys.argv[2] == 'python':
            print(h_python(l, 1000))