M Imam Pratama  
09021281722063  
IF Reg A 17  

## Tugas 1

### a. Cryptography Hash Functions Assignment

Kalkulasikan atau implementasikan cryptography hashes.

1. Tuliskan & jalankan sebuah program untuk mengkalkulasi hash dengan input
'hello', dengan python seperti diberikan pada contoh: **SHA-224**, **SHA-384**,
**SHA3-224**, **SHA3-384**.  
**note**: gunakan library python, *hashlib*.

    ```python
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

    ```
    
    output:
    
    ```console
    imampt@galatulis:~/Documents/Kuliah/KJK/tugas1$ python3 a_1.py                                                         
    SHA-224:  b'ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193'
    SHA-384:  b'59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f'
    SHA3-224:  b'b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81'
    SHA3-384:  b'720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887'
    ```
    
2. Generate-lah mennggunakan `openssl` sebuah file berisikan string, text,
kemudian gunakan opsi dari **aes-128-cbc**, **aes-192-cbc**, **aes-256-cbc**.  
**note**: lakukan seperti yang ada pada contoh menggunakan `openssl`.

### b. Brute-force attack

1. Gunakan serangan **brute-force** menggunakan `brute-salted-openssl` terhadap
file enkripsi yang sudah dilakukan dengan openssl **aes-256-cbc** dan jelaskan
prinsip konsep dari serangan brute-force pada studi kasus tersebut.

Berikut serangan brute-force yang dilakukan:

```console
imampt@galatulis:~/Documents/Kuliah/KJK/tugas1$ bruteforce-salted-openssl -f list-key-punya-kita.txt -d sha256 text-encoded-aes256cbc.txt
Warning: using dictionary mode, ignoring options -b, -e, -l, -m and -s.

Tried passwords: 2106
Tried passwords per second: inf
Last tried password: halo

Password candidate: halo
```

Tanpa file list password:

```console
imampt@galatulis:~/Documents/Kuliah/KJK/tugas1$ bruteforce-salted-openssl -d sha256 text-encoded-aes256cbc.txt
Tried / Total passwords: 1598403 / 2,21919e+14
Tried passwords per second: 799201,500000
Last tried password: 5gnh
Total space searched: 0,000001%
ETA: Sel 18 Jul 2028 06:33:24  WIB

Password candidate: 5gnh
Tried / Total passwords: 10631686 / 2,21919e+14
Tried passwords per second: 885973,833333
Last tried password: halo
Total space searched: 0,000005%
ETA: Rab 08 Sep 2027 12:12:23  WIB

Password candidate: halo
Tried / Total passwords: 11375146 / 2,21919e+14
Tried passwords per second: 875011,230769
Last tried password: kiB6
Total space searched: 0,000005%
ETA: Kam 14 Okt 2027 07:54:58  WIB

Password candidate: kiB6
^C
```
