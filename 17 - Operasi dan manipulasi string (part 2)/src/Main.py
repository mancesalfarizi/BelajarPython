# operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case 
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case 
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() --> untuk mengecek huruf
# isalnum() --> huruf dan angka
# isdecimal() --> angka saja
# isspace() --> spasi, tab, newline \n
# istittle() --> semua kata dimulai dengan huruf besar 

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool

print (judul + " is tittle = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() strip()
pisah = ["aku","sayang","kamu"]
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehemsayangehemkamu"
print(gabungan.split("ehem"))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikan -> strip
tengah = tengah.strip("-") # menghilangkan tanda -
print("'"+tengah+"'")