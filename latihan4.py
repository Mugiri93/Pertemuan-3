# Kalkulator Sederhana
print("=== Calculator ===")
angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua   = int(input("Masukkan angka kedua: "))

print("Hasil penjumlahan:", angka_pertama + angka_kedua)
print("Hasil pengurangan:", angka_pertama - angka_kedua)
print("Hasil perkalian:", angka_pertama * angka_kedua)
print("Hasil pembagian:", angka_pertama / angka_kedua)

# Celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
fahrenheit = (celcius * 9 / 5) + 32
print(celcius, "derajat Celsius sama dengan", fahrenheit, "derajat Fahrenheit")