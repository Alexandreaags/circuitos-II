import cmath

Va = 110
Za1 = complex(1, 2)
Za2 = complex(15, 25)
Ia = Va/(Za1 + Za2) 
print(f'A corrente de linha Ia é igual a {Ia:.2f} A')

Vb  = complex(-55, -95.263)
Zb1 = complex(1, 2)
Zb2 = complex(9, 12)
Ib = Vb/(Zb1 + Zb2)
print(f'A corrente de linha Ib é igual a {Ib:.2f} A')

Vc = complex(-55, 95.263)
Zc1 = complex(1, 2)
Zc2 = complex(12, 15)
Ic = Vc/(Zc1+Zc2)
print(f'A corrente de linha Ic é igual a {Ic:.2f} A')

In = (-1)*(Ia+Ib+Ic)
print(f'A corrente de neutro In é igual a {In:.2f} A')

Pa = Va*Ia*cmath.cos(0)
print(f'A potência ativa na fase A é igual a {Pa:.2f} VA') 
Qa = Va*Ia*cmath.sin(0)
print(f'A potência reativa na fase A é igual a {Qa:.2f} VA')

Pb = Vb*Ib*cmath.cos(240)
print(f'A potência ativa na fase B é igual a {Pb:.2f} VA') 
Qb = Vb*Ib*cmath.sin(240)
print(f'A potência reativa na fase B é igual a {Qb:.2f} VA')

Pc = Vc*Ic*cmath.cos(120)
print(f'A potência ativa na fase C é igual a {Pc:.2f} VA') 
Qc = Vc*Ic*cmath.sin(120)
print(f'A potência reativa na fase C é igual a {Qc:.2f} VA')

