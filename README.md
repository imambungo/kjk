M Imam Pratama  
09021281722063  
IF Reg A 17  

## Tugas 1 Keamanan Jaringan Komputer

### a. Cryptography Hash Functions Assignment

Kalkulasikan atau implementasikan cryptography hashes.

1. Tuliskan & jalankan sebuah program untuk mengkalkulasi hash dengan input
'hello', dengan python seperti diberikan pada contoh: **SHA-224**, **SHA-384**,
**SHA3-224**, **SHA3-384**.  
**note**: gunakan library python, *hashlib*.

    Tulis [programnya](a_1.py):

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
    imampt@galatulis:~/Tugas1KJK$ python3 a_1.py
    SHA-224:  b'ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193'
    SHA-384:  b'59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f'
    SHA3-224:  b'b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81'
    SHA3-384:  b'720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887'
    ```
    
2. Generate-lah mennggunakan `openssl` sebuah file berisikan string, text,
kemudian gunakan opsi dari **aes-128-cbc**, **aes-192-cbc**, **aes-256-cbc**.  
**note**: lakukan seperti yang ada pada contoh menggunakan `openssl`.

    buat [file](text-original.txt) berisi string "hello":

    ```console
    imampt@galatulis:~/Tugas1KJK$ echo 'hello' > text-original.txt
    ```

    command-command untuk membuat enkripsi dengan ketiga opsi di atas:

    ```
    openssl enc -aes-128-cbc -in text-original.txt -out text-encoded-aes128cbc.txt
    openssl enc -aes-192-cbc -in text-original.txt -out text-encoded-aes192cbc.txt
    openssl enc -aes-256-cbc -in text-original.txt -out text-encoded-aes256cbc.txt
    ```

    Gunakan password "halo"

    ```console
    imampt@galatulis:~/Tugas1KJK$ openssl enc -aes-128-cbc -in text-original.txt -out text-encoded-aes128cbc.txt
    enter aes-128-cbc encryption password:
    Verifying - enter aes-128-cbc encryption password:
    *** WARNING : deprecated key derivation used.
    Using -iter or -pbkdf2 would be better.
    ```

### b. Brute-force attack

1. Gunakan serangan **brute-force** menggunakan `bruteforce-salted-openssl` terhadap
file enkripsi yang sudah dilakukan dengan openssl **aes-256-cbc** dan jelaskan
prinsip konsep dari serangan brute-force pada studi kasus tersebut.

    Berikut serangan brute-force menggunakan [list password](list-key-punya-kita.txt)
    terhadap [file tersebut](text-encoded-aes256cbc.txt):
    
    ```console
    imampt@galatulis:~/Tugas1KJK$ bruteforce-salted-openssl -f list-key-punya-kita.txt -d sha256 text-encoded-aes256cbc.txt
    Warning: using dictionary mode, ignoring options -b, -e, -l, -m and -s.
    
    Tried passwords: 2106
    Tried passwords per second: inf
    Last tried password: halo
    
    Password candidate: halo
    ```
    
    Tanpa file list password:

    ```console
    imampt@galatulis:~/Tugas1KJK$ bruteforce-salted-openssl -d sha256 text-encoded-aes256cbc.txt
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

    Kedua cara di atas sama-sama merupakan serangan brute-force, bedanya yang
    pertama lebih terfokus dan cepat karena hanya mencoba mencocokkan dengan
    list password yang sudah terbukti sering dipakai orang. Kelemahannya adalah
    cara ini tidak tidak ampuh untuk mendekripsi password yang kompleks.

    Dengan cara kedua, passwordnya pasti didapat, tapi butuh waktu yang lama
    karena mencoba semua kemungkinan.
