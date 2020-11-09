# kita belajar casting
#  merubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

data_int = 0
print("data: ", data_int, ", type = ", type(data_int))

## INTEGER
print("====INTEGER=====")
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai integer = 0
print("data: ", data_float, ", type = ", type(data_float))
print("data: ", data_str, ", type = ", type(data_str))
print("data: ", data_bool, ", type = ", type(data_bool))

##FLOAT
print("====FLOAT=====")
data_float = 9.5
print("data: ", data_float, ", type = ", type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai integer = 0
print("data: ", data_int, ", type = ", type(data_int))
print("data: ", data_str, ", type = ", type(data_str))
print("data: ", data_bool, ", type = ", type(data_bool))

##BOOL
print("====BOOL=====")
data_bool = True
print("data: ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool) #akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai integer = 0
print("data: ", data_int, ", type = ", type(data_int))
print("data: ", data_str, ", type = ", type(data_str))
print("data: ", data_float, ", type = ", type(data_float))

##STRING
print("====STRING=====")
data_str = "10"
print("data: ", data_str, ", type = ", type(data_str))

data_int = int(data_str) #string harus angka
data_bool = bool(data_bool) # akan false jika kosong
data_float = float(data_str) #string harus angka
print("data: ", data_int, ", type = ", type(data_int))
print("data: ", data_bool, ", type = ", type(data_bool))
print("data: ", data_float, ", type = ", type(data_float))