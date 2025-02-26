print("Nhap cac dong van ban(Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower()=='done':
        break
    line.append(line)
print("\nCac dong da nhap sai khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())