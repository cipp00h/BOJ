A = input()
B = input()

print(A * (B % 10))
print(A * ((B % 100) // 10))
print(A * (B // 100))
print((A * (B // 100)) * 100 + (A * ((B % 100) // 10)) * 10 + (A * (B % 10)))
