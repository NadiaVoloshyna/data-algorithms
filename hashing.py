def convert_string(str, M):
    l = []
    exp = len(str) - 1
    for el in str:
        l.append(ord(el)*128**exp)
        exp = exp - 1
    print(l)
    num = sum(l) % M
    print(num)

convert_string('abcd', 97)

def hash(string, M):
    hash = 0
    a = 127 # base: prime
    for c in string:
        hash = ( hash * a + ord( c ) ) % M
    return hash

items = ['foo', 'bar', 'BCA', 'CAB', 'ad', 'ga', 'abcdefghijklmno']
for item in items:
    print("{}: {}".format(item, hash(item, 97))) # table size: prime

# output
foo: 84
bar: 44
BCA: 74
CAB: 42
ad: 3
ga: 83
abcdefghijklmno: 79