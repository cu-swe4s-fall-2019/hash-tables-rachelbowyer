import sys
import argparse


def h_ascii(key, N):
    """ASCII value sum for characters in key"""
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N


def h_rolling(key, N, p=53,  m=2**64):
    """polynomial rolling hash algorithm"""
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N


def h_python(key, N):
    """python default has function"""
    return hash(key) % N


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify hash ftn type")
    parser.add_argument('file', type=str, help='specify input .txt file')
    parser.add_argument('hash_type', type=str, help='Specify hash ftn type')
    args = parser.parse_args()

    for l in open(args.file):
        if args.hash_type == 'ascii':
            print(h_ascii(l, 1000))
        elif args.hash_type == 'rolling':
            print(h_rolling(l, 1000))
        elif args.hash_type == 'python':
            print(h_python(l, 1000))
        else:
            raise ValueError
