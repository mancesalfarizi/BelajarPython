# ++++++++++0--------5++++++8------11++++++

inputUser = float(input("masukkan nilai\nkurang dari 0 atau lebih dari 5"
                        "\natau\n"
                        "kurang dari 8 atau lebih dari 11:"))

# --------0+++++++
# memeriksa lebih dari 0
kurangDari0 = inputUser < 0
print("lebih dari 0: ", kurangDari0)

# ++++++++5-------
# memeriksa kurang dari 5
lebihDari5 = inputUser > 5
print("kurang dari 5: ", lebihDari5)

# --------8+++++++
# memeriksa lebih dari 8
kurangDari8 = inputUser < 8
print("lebih dari 8: ", kurangDari8)

# ++++++++11------
# memeriksa kurang dari 11
lebihDari11 = inputUser < 11
print("kurang dari 11: ", lebihDari11)

# ++++++++++0--------5++++++8------11++++++

isCorrect = (kurangDari0 or lebihDari5) and (kurangDari8 or lebihDari11)
print("angka yang anda masukkan: ", isCorrect)