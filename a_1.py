#!/usr/bin/env python3

# M Imam Pratama
# 09021281722063

import hashlib, binascii

text = "hello"
data = text.encode('utf8')

sha224hash = hashlib.sha224(data).digest()
sha384hash = hashlib.sha384(data).digest()
sha3_224hash = hashlib.sha3_224(data).digest()
sha3_384hash = hashlib.sha3_384(data).digest()

print("SHA-224: ", binascii.hexlify(sha224hash))
print("SHA-384: ", binascii.hexlify(sha384hash))
print("SHA3-224: ", binascii.hexlify(sha3_224hash))
print("SHA3-384: ", binascii.hexlify(sha3_384hash))
