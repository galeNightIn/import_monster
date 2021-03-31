def str_hash(s):
    p = 2**64 + 1
    a = 3533
    a_pow = [1] * (len(s) + 1)
    h = [0] * (len(s) + 1)
    for i in range(len(s)):
        h[i + 1] = (h[i] + (ord(s[i])) * a_pow[i]) % p
        a_pow[i + 1] = (a_pow[i] * a) % p
    return h[1:]


with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    s = fin.readline().rstrip('\n')
    str_set = set()
    for i in range(len(s)):
        for el in str_hash(s[i:]):
            str_set.add(el)
    fout.write(str(len(str_set)) + '\n')
