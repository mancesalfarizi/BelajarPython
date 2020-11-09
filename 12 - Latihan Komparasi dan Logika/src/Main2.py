# ----------0++++++++5------8++++++11------

inputUser = float(input("masukkan nilai\nlebih dari 0 dan kurang dari 5"
                        "\natau\n"
                        "lebih dari 8 dan kurang dari 11:"))

# --------0+++++++
# memeriksa lebih dari 0
lebihDari0 = inputUser > 0
print("lebih dari 0: ", lebihDari0)

# ++++++++5-------
# memeriksa kurang dari 5
kurangDari5 = inputUser < 5
print("kurang dari 5: ", kurangDari5)

# --------8+++++++
# memeriksa lebih dari 8
lebihdari8 = inputUser > 8
print("lebih dari 8: ", lebihdari8)

# ++++++++11------
# memeriksa kurang dari 11
kurandari11 = inputUser < 11
print("kurang dari 11: ", kurandari11)

# ----------0++++++++5------8++++++11------
isCorrect = (lebihDari0 and kurangDari5) or (lebihdari8 and kurandari11)
print("angka yang anda masukkan: ", isCorrect)



