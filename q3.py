import cmath

H1 = complex(0, 30)
H2 = complex(0, 50)
p = 320
v = 165
R = 10
I1 = cmath.sqrt(p*2/R)
x = cmath.sqrt(cmath.sqrt(123363-1210000)+1300)
W = 1
M = x/W
k = M/cmath.sqrt(1500)
Zin = complex(10, 30) + 38.13**2/complex(20,50)
I2 = 165/complex(-1100.201, -1301.22)
print(f'A impedância de entrada é {Zin:.2f} ohns')
print(f'O fator de acoplamento é {k:.2f}')
print(f'A corrente I2 é {I2:.2f} A')

