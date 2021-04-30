# List => objek terurut yang menampung lebih dari 1 tipe
l = [1, 8, 7, 3, 'python']
print(l)
print(l[3])
print(l[2:4])
print(l[-2])
print(l[0:5:2])
print('python'[2:6])

# Tuple => objek yang tidak dapat diubah elemennya
t = (1,3,2,'x')
print(t)

# Set => objek tidak terurut yang tidak mengizinkan data duplikat/ganda
s = {1,1,3,3,5,5,7,9}
print(s)

# Dictionary
d = {'name':'John', 'address':'wallstreet'}
print(d)
print(d['name'])
print(d['address'])

# Cek tipedata masing-masing
print(type(l))
print(type(t))
print(type(s))
print(type(d))