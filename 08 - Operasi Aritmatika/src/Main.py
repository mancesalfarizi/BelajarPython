# operasi aritmatika

a = 10 
b = 3

# Operasi tambah + 
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi pengurangan - 
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi perkalian * 
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi pembagian / 
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi ekponen (pangkat) ** 
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi modulus % 
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi floor division // 
hasil = a // b
print(a, "//", b, "=", hasil)

# proritas operasi, operational presedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman teman * / ** % //
    4. pertambahan dan pengurangan + - 
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)
# kurung akan mengambil paling langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=', hasil)