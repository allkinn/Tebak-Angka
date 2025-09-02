# Game Tebak Angka

Game sederhana berbasis console dengan Python.  
Player harus menebak angka rahasia yang digenerate secara random sesuai mode permainan.  

---

## Fitur
- 3 Mode Game:
  - **Easy** → angka 1 - 20
  - **Medium** → angka 1 - 50
  - **Hard** → angka 1 - 100
- Player bisa menentukan jumlah kesempatan (1 - 10).
- Validasi input → program tidak akan error walaupun player salah input.
- Feedback interaktif (angka terlalu besar/kecil).
- Bisa dimainkan berulang kali tanpa restart program.

---

## Cara Menjalankan
1. Pastikan Python sudah terinstall di perangkatmu.
   ```
   python --version
2. clone repository atau download file .py
   ```
   git clone https://github.com/username/repo-tebak-angka.git
3. Jalankan program
   ```
   python tebak_angka.py

---

## Cara Bermain
1. Pilih mode permainan (Easy/Medium/Hard).
2. Tentukan jumlah kesempatan (1 - 10).
3. Masukkan angka tebakanmu.
   - Jika terlalu kecil → akan muncul pesan "Terlalu kecil".
   - Jika terlalu besar → akan muncul pesan "Terlalu besar".
   - Jika benar → kamu menang!
4. Jika kesempatan habis, angka rahasia akan ditampilkan.
5. Pilih apakah ingin bermain lagi atau keluar dari game.

---

Contoh output:
=============== Game Tebak Angka ===============
Mode Game:
    1. Easy (1 - 20)
    2. Medium (1 - 50)
    3. Hard (1 - 100)
------------------------------------------------
Silahkan Pilih Mode Game: 1
Anda Memilih Mode Game Easy
Range: 1 - 20
------------------------------------------------
Masukkan Jumlah Kesempatan (Min: 1; Max: 10): 5
Anda Memilih 5 Kesempatan
------------------------------------------------
Coba Tebak: 10
Terlalu kecil! Coba lagi.
Sisa Percobaan Anda adalah 4
Coba Tebak: 15
Selamat, Anda Benar!
Anda Menebak Angka 15 dalam 2 Percobaan
------------------------------------------------
Apakah anda ingin bermain lagi? (y/n): n
Sampai Jumpa Lagi

---

## Teknologi
   Python (standar library random).

---

## Kontributor
   - allkinn
   - GPT

---

