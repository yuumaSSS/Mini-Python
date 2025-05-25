# Calculating GCD and LCM with the Euclidean method

def GCD (a, b) -> int:
    x = a
    y = b
    while y!=0:
        x, y = y, x % y
    return x

def LCM (a, b) -> int:
    return a*b//GCD(a, b)

print('GCD and LCM Calculator\nUsing The Euclidean Method\n')

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

print(f'\nThe GCD of {a} and {b} = {GCD(a,b)}')
print(f'The LCM of {a} and {b} = {LCM(a,b)}')

print('\nThanks for using!')
print('github.com/yuumaSSS')
