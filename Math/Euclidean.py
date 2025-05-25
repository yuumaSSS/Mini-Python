# Menghitung FPB dan KPK dengan method Euclidean

def FPB (a, b) -> int:
    x = a
    y = b
    while y!=0:
        x, y = y, x % y
    return x

def KPK (a, b) -> int:
    return a*b//FPB(a, b)

print('Kalkulator FPB dan KPK\nMenggunakan Metode Euclidean\n')
a = int(input('Masukkan angka pertama: '))
b = int(input('Masukkan angka kedua: '))
print(f'\nFPB dari {a} dan {b} = {FPB(a,b)}')
print(f'KPK dari {a} dan {b} = {KPK(a,b)}')
