import random

print(15*'=', "Game Tebak Angka", 15*'=')
teks_except = "Tolong Masukkan Angka!"

while True:

    # Game Mode
    print("""Mode Game:
    1. Easy (1 - 20)
    2. Medium (1 - 50)
    3. Hard (1 - 100)""")
    print(48*'-')

    # Input user pada Game Mode
    try:
        gm = int(input("Silahkan Pilih Mode Game: "))

        # Generate angka random berdasarkan game mode
        if gm == 1:
            sn = random.randint(1, 20)
            teks = "Easy"
            teks1 = "Range: 1 - 20"
        elif gm == 2:
            sn = random.randint(1, 50)
            teks = "Medium"
            teks1 = "Range: 1 - 50"
        elif gm == 3:
            sn = random.randint(1, 100)
            teks = "Hard"
            teks1 = "Range: 1 - 100"
        else:
            print("Harap Masukkan Angka yang Sesuai!\n")
            continue

    except ValueError:
        print(teks_except,"\n")
        continue

    print(f"Anda Memilih Mode Game {teks}\n{teks1}")
    print(48*'-')

    # Input kesempatan
    while True:
        try:
            count = int(input("Masukkan Jumlah Kesempatan (Min: 1; Max: 10): "))

            if count > 10 and count < 1:
                print("Harap Masukkan Angka di antara 1 - 10")
                print(48*'-')
                continue
            else:
                print(f"Anda Memilih {count} Kesempatan")
                print(48*'-')
                break

        except ValueError:
            print(teks_except)
            continue

    # Main loop
    full = 0
    is_right = False

    while count > 0 and not is_right:
        try:
            check = int(input("Coba Tebak: "))
        except ValueError:
            print(teks_except)
            continue

        full += 1

        if check < sn:
            print("Terlalu kecil! Coba lagi.")
        elif check > sn:
            print("Terlalu besar! Coba lagi.")
        else:
            print('-'*42)
            print("Selamat, Anda Benar")
            print(f"Anda Menebak Angka {sn} dalam {full} Percobaan")
            print(48*'-')
            is_right = True
            break

        count -= 1
        print(f"Sisa Percobaan Anda adalah {count}")

    if not is_right:
        print(f"Anda Gagal Menebaknya, Angka yang Benar adalah {sn}.")
        print(48*'-')

    # Tanya main lagi
    play = input("Apakah anda ingin bermain lagi? (y/n): ").lower()
    if play != 'y':
        print("Terima Kasih Telah Bermain!")
        break
    
