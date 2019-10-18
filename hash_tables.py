import hash_functions
import time
import random
import argparse


class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        hash_slot = self.hash(key, self.N)

        for k, v in self.T[hash_slot]:
            if key == k:
                return v
        return None


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify hash parameters")
    parser.add_argument('N', type=str, help='number')
    parser.add_argument('hash_type', type=str, help='Specify hash ftn type')
    parser.add_argument('coll_strat', type=str, help='Specify collison strat')
    parser.add_argument('file', type=str, help='specify file name')
    parser.add_argument('keys', type=int, help='keys to add')
    args = parser.parse_args()

    N = int(args.N)
    hash_alg = args.hash_type
    collision_strategy = args.coll_strat
    data_file_name = args.file
    keys_to_add = args.keys

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_rolling)

    elif hash_alg == 'python':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_python)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_python)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)
