sisi = float(input("Masukkan sisi persegi: "))
pilihan = input("pilih luas/keliling: ")

sisi_persegi = sisi * sisi
keliling_persegi = 4 * sisi

dict_hasil = {"luas": sisi_persegi, "keliling": keliling_persegi}
pesan_error = "Oops, hanya bisa input \"luas\" atau \"keliling\". Periksa kembali input-an Anda"

print(dict_hasil.get(pilihan, pesan_error))