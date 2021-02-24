def fixed_xor(inp, xor):
    res = int(inp, 16) ^ int (xor,16)
    return '{:x}'.format(res)

i1 = '1c0111001f010100061a024b53535009181c'
i2 = '686974207468652062756c6c277320657965'

print(fixed_xor(i1,i2))