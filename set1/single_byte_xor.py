ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# Sol: Cooking MC's like a pound of bacon

def single_byte_xor(inp, key):
    enc = bytes.fromhex(inp)
    ans = ''
    for i in enc:
        ans += chr(i^key)
    return ans

for i in range(0xff):
    print(single_byte_xor(ct,i))