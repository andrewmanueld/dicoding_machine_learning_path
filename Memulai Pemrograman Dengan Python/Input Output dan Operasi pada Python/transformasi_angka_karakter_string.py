# Huruf besar dan kecil
print("Hello Dicoding".upper())
print("Hello Dicoding".lower())

# Awalan dan akhiran
print(" Hello Dicoding ".strip())
print(" Hello Dicoding ".lstrip())
print(" Hello Dicoding ".rstrip())

# Pengecekan karakter
print("Hello Dicoding".startswith("Hello"))
print("Hello Dicoding".endswith("Dicoding"))

# Join dan replace
print("hello Dicoding".join(["Hi ", " hello juga"]))
print("Hello Dicoding".replace("Dicoding", "World"))

# Pengecekan string 
print("Hello Dicoding".isupper())
print("Hello Dicoding".islower())
print("Hello Dicoding".isalpha())
print("Hello Dicoding".isalnum())
print("Hello Dicoding".isdecimal())
print("Hello Dicoding".istitle())

# Alignment
print(" Hello Dicoding ".center(20, '-'))
print(" Hello Dicoding ".rjust(20, '-'))
print(" Hello Dicoding ".ljust(20, '-'))

# String literal
print(" Hello Dicoding, sekarang hari Jum\'at ")