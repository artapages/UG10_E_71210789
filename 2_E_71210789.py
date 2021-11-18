#mengambil input
temperatur = float(input("Masukkan suhu tubuh Anda : "))

#mengambil output
if temperatur >= 50:
    print("Anda bukan manusia :)")
elif temperatur <= 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif 50 >= temperatur > 37.5:
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
elif 37.5 >= temperatur > 32:
    print("Suhu Anda normal!")