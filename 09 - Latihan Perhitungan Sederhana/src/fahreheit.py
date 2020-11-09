print("\n PROGRAM KONVERSI FAHRENHEIT\n")

#fahrenheit ke kelvin
'''jadi kita harus cari dulu nilai celcius dengan rumus
5/9(f-32) lalu diubah ke kelvin setelah dapet nilai celciusnya
'''
fahrenheit = int(input("Masukkan nilai fahrenheit: "))
print("====nilai celcius====")
celcius = 5/9*(fahrenheit-32)
print(5,'/',9,'(',fahrenheit,'-',32,')','=', celcius)
print("====nilai kelvin====")
kelvin = 9 / 5 * celcius + 32
print(9,'/',5,'*',celcius,'+',32,'=',kelvin)