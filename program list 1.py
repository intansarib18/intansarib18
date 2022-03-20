#membuat list
nama_hewan = ["monyet","kucing","kuda","ular"]
print(nama_hewan)
#menampilkan list dengan perulangan
for i in nama_hewan:
    print(i)
i = 0
while i< len(nama_hewan):
    print(nama_hewan[i])
    i += 1
#mengupdate salah satu list
nama_hewan [0] = "buaya"
print(nama_hewan)

#menghapus list
nama_hewan.pop()
print(nama_hewan)

del nama_hewan [0:2]
print(nama_hewan)

nama_hewan.remove("kuda")

#menambahkan list
nama_hewan.append("monyet")
print(nama_hewan)

nama_hewan.extend(["kucing","kuda"])
print(nama_hewan)

nama_hewan.insert(2,"ular")
print(nama_hewan)
