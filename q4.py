import cmath
n = 6
Z3 = complex(36, 18)
Zr = complex(12, 2)/4 
Zin = complex(5,-2) + Zr
I1 = 24/Zin
I3 = 1/n*I1
print(f'A corrente I1 é {I1:.2f} A')
print(f'A corrente I3 é {I3:.2f} A')
print(f'A impedância de entrada é {Zin:.2f} ohns')