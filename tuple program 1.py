#membuat tuple
buah = ("apel", "manggis", "durian", "mangga", "jeruk")
#menampilkan tuple dengan perulangan
for i in buah :
    print(i)
a = 0
while a< len(buah):
    print(buah[a])
    a += 1
buah = list(buah)

#mengupdate salah satu tuple
buah [2] = "anggur"
print(buah)

#menghapus tuple
buah.pop()
print(buah)

buah.remove ("mangga")
print(buah)

del buah [0:2]
print(buah)



#menmabhkan tuple
buah.append ("apel")
print(buah)

buah.extend (["jeruk","manggis"])
print(buah)

buah.insert (2,"jambu")
print(buah)
