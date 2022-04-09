import cmath

Va = 110
Za1 = complex(1, 2)
Za2 = complex(15, 25)
Ia = Va/(Za1 + Za2) 
print(f'A corrente de linha Ia é igual a {Ia:.2f}A')

Vb  = complex(-55, -95.263)
Zb1 = complex(1, 2)
Zb2 = complex(9, 12)
Ib = Vb/(Zb1 + Zb2)
print(f'A corrente de linha Ib é igual a {Ib:.2f}A')

Vc = complex(-55, 95.263)
Zc1 = complex(1, 2)
Zc2 = complex(12, 15)
Ic = Vc/(Zc1+Zc2)
print(f'A corrente de linha Ic é igual a {Ic:.2f}A')
