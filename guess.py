nilai = 80
tebak = int(input("Tebak angka dari 1 sampai 100 : "))

while (nilai != tebak):
    if tebak < nilai:
        print('TEBAKAN KAMU TERLALU RENDAH, AYO TEBAK LAGI.')
        tebak = int(input("Tebak angka dari 1 sampai 100 : "))
    if tebak > nilai:
        print('TEBAKAN KAMU TERLALU TINGGI, AYO TEBAK LAGI.')
        tebak = int(input("Tebak angka dari 1 sampai 100 : "))

print("KAMU BERHASIL MENEBAK ANGKANYA.")