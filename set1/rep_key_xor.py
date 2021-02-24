def rep_key_xor(inp, key):
    ct1 = ''
    for i in range(len(inp)):
        tmp = ord(key[i%3])^ord(inp[i])
        ct1 += '{:02x}'.format(tmp)
    return ct1

pt1 = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
ky1 = "ICE"
print(rep_key_xor(pt1,ky1))