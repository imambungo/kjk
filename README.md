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
