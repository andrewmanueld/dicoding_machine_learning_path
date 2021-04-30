import sys

# Output sederhana 
print("Hello world")

# Formatting string
nama = "John Doe"
print("Hello {}".format(nama))

# Format dengan nomor
print("%d modulus %d hasilnya %d %s" % (10, 3, (10 % 3), "valid"))

# input pada python 3
angka = int(input("Masukkan angka: "))

print("Angka yang diinput: %d" % (angka))

print("Argumen %s. Panjang : %d" % (sys.argv[0], len(sys.argv)))