#mengambil input
nama1, nama2, nama3 = list(input("Masukkan daftar siswa : ").split(", "))
a = nama1.title()
r = nama2.title()
t = nama3.title()
print("Daftar Siswa : ['"+a+"', '"+r+"', '"+t+"']")
proses = input("Masukkan siswa yang ingin ditambahkan : ")
prosesx = proses.title()
x = prosesx.upper()

#mengambil output
if prosesx == a:
    print("Siswa atas nama", x,"sudah berada dalam daftar siswa")
elif prosesx == r:
    print("Siswa atas nama", x,"sudah berada dalam daftar siswa")
elif prosesx == t:
    print("Siswa atas nama", x,"sudah berada dalam daftar siswa")
else:
    print("Hasil penambahan pada daftar siswa : ['"+a+"', '"+r+"', '"+t+"', '"+x+"']")