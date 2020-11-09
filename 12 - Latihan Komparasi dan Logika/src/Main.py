# episode latihan dan komparasi

#membuat gabungan rentan dari angka

# ++++++++3-------10++++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# ++++++++3-----------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 = ", isKurangDari)

#----------10++++++++++++++
# memeriksa angka lebih dari 10
isLebihdari = (inputUser > 10)
print("lebih dari 10 = ", isLebihdari)

isCorrect = isKurangDari or isLebihdari
print("angka yang anda masukkan: ", isCorrect)

#----------3++++++++++10----------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

#-------3+++++++++++++
#lebih dari 3
isLebihdari = inputUser > 3
print("lebih dari 3 = ", isLebihdari)

#++++++++10-----------
#kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 = ", isKurangDari)

#----------3++++++++++10----------
isCorrect = isKurangDari and isLebihdari
print("angka yang anda masukkan: ", isCorrect)