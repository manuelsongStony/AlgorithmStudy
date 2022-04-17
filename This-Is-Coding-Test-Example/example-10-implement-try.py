import copy

[0, 1, 0]
[1, 0, 0]
[1, 0, 0]

[(0, 0), (0, 0), (0, 0), (0, 0)]
[(0, 0), (0, 0), (0, 0), (0, 0)]
[(0, 0), (0, 0), (0, 0), (0, 0)]
[(0, 0), (0, 0), (0, 0), (0, 0)]

key2 = \
    [[(0, 0), (0, 1), (0, 2), (0, 3)],
     [(1, 0), (1, 1), (1, 2), (1, 3)],
     [(2, 0), (2, 1), (2, 2), (2, 3)],
     [(3, 0), (3, 1), (3, 2), (3, 3)]]

[(3, 0), (2, 0), (1, 0), (0, 0)]
[(3, 1), (2, 1), (1, 1), (0, 1)]
[(3, 2), (2, 2), (1, 2), (0, 2)]
[(3, 3), (2, 3), (1, 3), (0, 3)]

key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

key1 = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

lock1 = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

key2 = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

lock2 = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


def turn_ninty(array):
    # temp=[[0 for _ in range(len(array))] for _ in range(len(array))]
    # temp1=[[0]*4]*4
    n = len(array)
    temp2 = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp2[j][n - 1 - i] = array[i][j]

    return temp2


def enlarge_lock(key, lock):
    extra = len(key) - 1

    new_lock = [[0] * (extra * 2 + len(lock)) for _ in range(extra * 2 + len(lock))]

    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i + extra][j + extra] = lock[i][j]

    return new_lock

def check_valid(array,key):
    extra=len(key) - 1
    for row in range(len(array)-(2*extra)):
        for col in range(len(array)-(2*extra)):
            if array[row+extra][col+extra]==1:
                continue
            else:
                return False
    return True

def check(key, lock):
    e_lock=enlarge_lock(key, lock)

    n = len(e_lock)-len(key)+1

    for i in range(4):
        key=turn_ninty(key)
        for i in range(n):
            for j in range(n):
                temp=copy.deepcopy(e_lock)
                for row in range(len(key)):
                    for col in range(len(key)):
                        temp[i+row][j+col]+=key[row][col]

                """for k in temp:
                    print(k)
                print()"""
                if check_valid(temp,key):
                    return True

    return False

print(check(key, lock))
"""
for i in enlarge_lock(key, lock):
    print(i)
"""

