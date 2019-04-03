import matplotlib.pyplot as plt
import numpy as np
#Tugas Praktikum Konsep Teknologi
#author: Anastasyarez

#fungsi input nilai
def inputnilai():
    lagi = "y"

    while (lagi=="y"):
        print("ISI DATA NILAI")

        nis = input("NIS: ")
        nama = input("NAMA: ")
        test1 = float(input("TEST 1: "))
        test2 = float(input("TEST 2: "))
        test3 = float(input("TEST 3: "))

        rerata = (test1+test2+test3)/3

        f = open("nilai.txt", "a")
        f.write(nis + " " + nama + " " + str(test1) + " " + str(test2) + " " + str(test3) + " " + str(rerata)+" \n")

        lagi = input("Mau mengisi kembali? (y/t): ")
    print("--------------------------")
    print("Terima kasih sudah mengisi! \n")

def lihat():
    f = open("nilai.txt", "r")
    text = f.read()

    print("--------------------------")
    print("Rekap Data:\nNIM     NAMA    TEST 1 TEST 2 TEST 3 RATA-RATA")
    print(text)

    list_nilai = text.split()
    # print(list_nilai)

    n = 6
    final = [list_nilai[i * n:(i + 1) * n] for i in range((len(list_nilai) + n - 1) // n)]
    # print(final)

    test1 = []
    test2 = []
    test3 = []
    # rerata = []
    nama = []
    rata = 0
    maks1 = 0
    maks2 = 0
    maks3 = 0
    for baris in range(0, len(final)):
        for kolom in range(5, 6):
            # rerata.append(float(final[baris][kolom]))
            if (float(final[baris][kolom]) > float(rata)):
                rata = float(final[baris][kolom])
                ratamin = rata
            if (float(final[baris][kolom]) < float(ratamin)):
                ratamin = float(final[baris][kolom])

    for baris in range(0, len(final)):
        for kolom in range(2, 3):
            test1.append(float(final[baris][kolom]))
            if (float(final[baris][kolom]) > float(maks1)):
                maks1 = float(final[baris][kolom])
                min1 = maks1
            if (float(final[baris][kolom]) < float(min1)):
                min1 = float(final[baris][kolom])

    for baris in range(0, len(final)):
        for kolom in range(3, 4):
            test2.append(float(final[baris][kolom]))
            if (float(final[baris][kolom]) > float(maks2)):
                maks2 = float(final[baris][kolom])
                min2 = maks2
            if (float(final[baris][kolom]) < float(min2)):
                min2 = float(final[baris][kolom])

    for baris in range(0, len(final)):
        for kolom in range(4, 5):
            test3.append(float(final[baris][kolom]))
            if (float(final[baris][kolom]) > float(maks3)):
                maks3 = float(final[baris][kolom])
                min3 = maks3
            if (float(final[baris][kolom]) < float(min3)):
                min3 = float(final[baris][kolom])

    for baris in range(0, len(final)):
        for kolom in range(1, 2):
            nama.append(final[baris][kolom])

    print("Rata-rata nilai terbesar adalah: " + str(rata));
    print("Rata-rata nilai terkecil adalah: " + str(ratamin));
    print("Nilai TEST 1 terbesar adalah: " + str(maks1))
    print("Nilai TEST 1 terkecil adalah: " + str(min1))
    print("Nilai TEST 2 terbesar adalah: " + str(maks2))
    print("Nilai TEST 2 terkecil adalah: " + str(min2))
    print("Nilai TEST 3 terbesar adalah: " + str(maks3))
    print("Nilai TEST 3 terkecil adalah: " + str(min3) + "\n")

    graf = input("Mau melihat grafiknya? (y/t): ")
    if graf == 'y':
        ax=plt.subplot()
        index = np.arange(len(nama))
        r1 = ax.bar(index-0.2, test1, color="black", width=0.2)
        r2 = ax.bar(nama, test2, color="pink", width=0.2)
        r3 = ax.bar(index+0.2, test3, color="r", width=0.2)
        # ax.bar(index+0.4, rerata, color="y", width=0.2)
        ax.legend((r1, r2, r3),("TEST 1", "TEST 2", "TEST 3"), loc="upper right")
        plt.ylim(0,150)
        plt.xlabel('Nama')
        plt.ylabel('Nilai')
        plt.title('Grafik Nilai')
        # plt.legend()
        plt.show()

    x = input("Silakan input apa saja untuk kembali ke menu...")
    print("----------------------------------------------------------")
    print("Terima kasih telah menggunakan layanan input nilai~\n")

pilih = 0
while (pilih != 3):
    try:
        print("====PROGRAM MENGINPUT NILAI====")
        print("1. Input Nilai\n2. Lihat Statistik \n3. Selesai")
        pilih = int(input("Pilih Menu: "))

        if pilih == 1:
            inputnilai()
        elif pilih == 2:
            lihat()
        elif pilih == 3:
            print("Sampai jumpa lagi!")

    except ValueError:
        print("\nInput dengan benar!\n")