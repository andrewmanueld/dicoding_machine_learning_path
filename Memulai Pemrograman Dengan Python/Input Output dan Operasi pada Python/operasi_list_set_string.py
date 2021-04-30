# Banyak data/karakter dengan len()
listdata = [1, 3, 3, 7, 7, 7, 9, 9, 11, 13]
print(listdata)
print("Banyak data pada list list %d " % (len(listdata))) 

setdata = set(listdata)
print(setdata)
print("Banyak data list yang dikonversi menjadi set %d " % (len(setdata)))

stringdata = "Hello Dicoding"
print(stringdata)
print("Banyak karakter pada string %d " % (len(stringdata)))

# Banyak data/karakter dengan count()
listdata = [1, 3, 3, 7, 7, 7, 9, 9, 11, 13]
print(listdata)
print("Banyak data pada list list %d " % (listdata.count(7))) 

stringdata = "Hello Dicoding"
print(stringdata)
print("Banyak karakter o pada teks \'%s\' %d " % (stringdata, stringdata.count('o')))

# Penggabungan dan Replikasi
list1 = ['H', 'E', 'L', 'L', 'O', ' ']
list2 = ['D', 'I', 'C', 'O', 'D', 'I', 'N', 'G']

print(list1 + list2)
print(list1 * 2)

# Manipulasi list
list1[5] = '!'
print(list1)

# For, and, or, not in
for i in range(5):
    print(i)

for i in range(1,10):
    print(i)

print(True and False)
print(False and True)
print(True and True)
print(False and False)

print(True or False)
print(False or True)
print(True or True)
print(False or False)

# Sort
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)