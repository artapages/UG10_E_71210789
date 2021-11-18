#judul
print("===== Kalkulator Akar dan Pangkat =====")

#soal
print("Pilihan menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")

#mengambil input
pilihan = int(input("Masukkan menu yang anda pilih : "))

#mengambil output
if pilihan == 1:
    proses = int(input("Masukkan bilangan yang ingin di pangkatkan : "))
    penyelesaian = (proses ** 2)
    print("Hasil dari pemangkatan bilangan", proses, "dengan 2 (Kuadrat) adalah", penyelesaian)
elif pilihan == 2:
    proses = int(input("Masukkan bilangan yang ingin di pangkatkan : "))
    penyelesaian = (proses ** 3)
    print("Hasil dari pemangkatan bilangan", proses, "dengan 3 (Kubik) adalah", penyelesaian)
elif pilihan == 3: 
    proses = int(input("Masukkan bilangan yang ingin di akarkan : "))
    penyelesaian = float(proses ** (1/2))
    print("Hasil akar kuadrat dari bilangan", proses, "adalah", penyelesaian)
else:
    print("Pilihan menu yang dimasukkan tidak sesuai!")