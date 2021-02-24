def single_byte_xor(inp, key):
    enc = bytes.fromhex(inp)
    ans = ''
    for i in enc:
        ans += chr(i^key)
    return ans

fname = open('4.txt')

def cf(inp):
    freq = ['z', 'q', 'x', 'j', 'k', 'v', 'b', 'p', 'y', 'g', 'f', 'w', 'm',
            'u', 'c', 'l', 'd', 'r', 'h', 's', 'n', 'i', 'o', 'a', 't', 'e']
    
    low = inp.lower()
    sum = 0
    for x in low:
        if x in freq:
            sum += freq.index(x)
    return sum

for line in fname.readlines():
    for i in range(0xff):
        tmp1 = single_byte_xor(line,i)
        tmp2 = cf(tmp1)
        if tmp2 > 400: # Chosen heuristically
            print(tmp1) # Now that the party is jumping
