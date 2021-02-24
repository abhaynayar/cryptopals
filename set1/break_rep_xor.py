import base64

f = open('6.txt')
lines = f.readlines()


def hamming(i1,i2):
    sum = 0
    for i in range(len(i1)):
        sum += abs(ord(i1[i]) - ord(i2[i]))
    return sum

h1 = 'this is a test'
h2 = 'wokka wokka!!!'
print(hamming(h1,h2))

for KEYSIZE in range(2, 40):
    continue