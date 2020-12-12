# python3

prime = 1000000007
multiplier = 1

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(s):
    global prime,multiplier
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans

def PreComputeHashes(T,P):
    global prime, multiplier
    P_len = len(P)
    T_len = len(T)
    H = [[None] for i in range(T_len - P_len + 1)]
    S = T[(T_len - P_len) : ]
    H[T_len - P_len] = PolyHash(S)
    y = 1
    for i in range(1,P_len):
        y = (y * multiplier) % prime
    for j in range(T_len - P_len - 1, -1, -1):
        H[j] = (multiplier * H[j+1] + ord(T[j]) - y * ord(T[j+P_len])) % prime

    return H


def RabinKarp(pattern, text):
    global prime, multiplier
    P_len = len(pattern)
    T_len = len(text)
    result = []
    pHash = PolyHash(pattern)
    H = PreComputeHashes(text, pattern)
    for i in range(T_len - P_len + 1):
        if pHash != H[i]:
            continue
        if text[i:(i + P_len)] == pattern:
            result.append(i)
    
    return result

if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

