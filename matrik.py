import numpy as np
ulang = True
while ulang:
    print()
    print(".::Operasi 2 Matriks::.")
    print("1. Penjumlahan 2 matriks")
    print("2. Pengurangan 2 matriks")
    print("3. Perkalian 2 matriks")
    print("4. Pembagian 2 matriks")
    pilihan = int(input("Pilih Operasi matrix yang Anda inginkan [1-4]:"))
    cek = True
    while cek:
        print()
        n_baris1 = int(input("Masukkan jumlah baris matriks 1 : "))
        n_kolom1 = int(input("Masukkan jumlah kolom matriks 1 : "))
        n_baris2 = int(input("Masukkan jumlah baris matriks 2 : "))
        n_kolom2 = int(input("Masukkan jumlah kolom matriks 2 : "))
        print("Masukkan nilai matrik 1 (dipisah dengan spasi):")
        inputmatrik1 = list(map(int, input().split()))
        matrix1 = np.array(inputmatrik1).reshape(n_baris1,n_kolom1)
        print("Masukkan nilai matrik 2 (dipisah dengan spasi):")
        inputmatrik2 = list(map(int, input().split()))
        matrix2 = np.array(inputmatrik2).reshape(n_baris2,n_kolom2)
        print()
        print("Matrik 1:")
        print(matrix1)
        print()
        print("Matrik 2:")
        print(matrix2)
        print()
        tanya = input("Apakah matriks Anda sudah benar? [y/n]")
        cek = False if tanya=="y" else True
    if pilihan == 1:
        if (n_baris1==n_baris2 and n_kolom1==n_kolom2):
            print("Hasil penjumlahan matriks 1 dengan matriks 2 adalah")
            print(matrix1+matrix2)
        else:
            print("!!!Ordo kedua matriks tidak sama!!!")
    elif pilihan == 2:
        if (n_baris1==n_baris2 and n_kolom1==n_kolom2):
            print("Hasil pengurangan matriks 1 dengan matriks 2 adalah")
            print(matrix1-matrix2)
        else:
            print("!!!Ordo kedua matriks tidak sama!!!")
    elif pilihan == 3:
        if n_kolom1==n_baris2:
            print("Hasil perkalian matriks 1 dengan matriks 2 adalah")
            print(np.dot(matrix1,matrix2))
        else:
            print("!!!Kolom matriks 1 tidak sama dengan baris matriks 2!!!")
    elif pilihan == 4:
        if (n_kolom1==n_baris2 and n_kolom2==n_baris2):
            det_matrix2 = np.linalg.det(matrix2)
            if det_matrix2!=0:
                print("Hasil pembagian matriks 1 dengan matriks 2 adalah")
                matrix2_inv = np.linalg.inv(matrix2)
                print(np.dot(matrix1, matrix2_inv))
            else:
                print("!!!Matriks 2 adalah matriks singular!!!")
        elif n_kolom1!=n_baris2:
            print("!!!Kolom matriks 1 tidak sama dengan baris matriks 2!!!")
        elif n_baris2!=n_kolom2:
            print("!!!Matriks 2 bukan matriks persegi!!!")
    else:
        print("Pilihan tidak tersedia")
    ulangi = input("Apakah Anda ingin melanjutkan? [y/n]")
    ulang = False if ulangi=="n" else True