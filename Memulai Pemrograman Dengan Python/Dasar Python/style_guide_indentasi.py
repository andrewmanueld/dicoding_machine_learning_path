# indentasi 4 spasi
def statement1():
    print('Hello Statement')
    statement2('John')

def statement2(nama):
    print('Hello', nama)

# Baris lanjutan
def baris1():
    param = baris2('John', 'Doe',
                    'Wall Street', 'Lawyer')
    print(param)

def baris2(nama_depan, nama_belakang, alamat, pekerjaan):
    print(nama_depan, nama_belakang, 
            alamat, pekerjaan)

# indentasi pada kurung siku
def kurung_siku(listdata):
    for x in listdata:
        print(x)

statement1()
baris1()

data = [
    1, 5, 7,
    9, 11, 13,
    15, 17, 19
]

kurung_siku(data)

# Maksimal komentar 72 karakter perbaris, 79 untuk kode + whitespace