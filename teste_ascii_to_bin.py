import binascii

a = raw_input("palavra para codificar")

b = int(binascii.hexlify(a), 16)

c = binascii.unhexlify('%x' % b)

print bin(b)

print c
