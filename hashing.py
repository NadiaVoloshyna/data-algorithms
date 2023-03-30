def hash_string1(str):
    hv = 0
    for ch in str:
        hv <<= 7
        hv += ord(ch)
    return hv

def hash_string2(str):
    hv = 0
    for ch in str:
        hv <<= 7
        hv += ord(ch)
    return bin(hv)

# modular hashing disregards most of the original value to keep hash values in a range
def hash_string3(str, M):
    hv = 0
    for ch in str:
        hv <<= 7
        hv += ord(ch)
    hv = bin(hv % M)
    return hv

items = ['abc', 'def', 'xyz', 'ugb', 'ord']
for item in items:
    print(item, "{}".format(hash_string1(item)), "{}".format(hash_string2(item)), "{}".format(hash_string3(item, 64)))

