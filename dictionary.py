#contoh dictionary
identitas = {
    'nama' : 'intan sari b',
    'usia' : 19,
    'status' : 'mahasiswi'
}
#menampilkan dictionary dengan perulangan
for i in identitas.items():
    print(i)
for i in identitas:
    print(i)
for i in identitas.values():
    print(i)
#mengupdate dictionary
identitas ['asal'] = 'mamuju tengah'
print(i)
#menghapus dictionary
identitas.pop('asal')
print(identitas)
print(identitas.popitem())

identitas.clear()
print(identitas)

#menambahkan dictionary
identitas ['asal'] = 'mamuju tengah'
print(identitas)
