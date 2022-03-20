#membuat set
nama = {"intan", 10, False, 15, "hilda"}
#menampilkan set dengan perulangan
for i in nama:
    print(i)
nama = list(nama)
i = 0
while i < len(nama):
    print(nama[i])
    i += 1
#mengupdate set
nama = list(nama)
nama[2] = "fani"
print(nama)
nama = set(nama)
#menghapus set
nama.remove("hilda")
print(nama)
nama.pop()
print(nama)
nama.clear()
print(nama)
#menambahkan set
nama.add("intan")
print(nama)

nama.update(["hilda","yanto"])
print(nama)
