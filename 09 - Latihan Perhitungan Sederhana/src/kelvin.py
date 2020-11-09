print("\n PROGRAM KONVERSI KELVIN\n")

# kelvin ke fahrenheit
'''jadi kita harus cari dulu nilai celcius dengan rumus
K - 273 lalu diubah ke fahrenheit setelah dapet nilai celciusnya
'''
kelvin = int(input("masukkan nilai kelvin: "))
print("====NILAI CELCIUS====")
celcius = kelvin - 273
print(kelvin,'-',273,'=', celcius)
print("====NILAI FAHRENHEIT====")
fahrenheit = celcius + 273
print(celcius,'+',273, '=', fahrenheit)
