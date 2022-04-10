import cmath

Ia1 = complex(17.321, 10)/complex(7.102,14.408)
Ia2 = Ia1*5/7
Ia0 = Ia1 - Ia2
p = abs(Ia2)**2 * 10

print(f'A corrente I1 é igual a {Ia1:.2f} mA')
print(f'A corrente I2 é igual a {Ia2:.2f} mA')
print(f'A corrente I0 é igual a {Ia0:.2f} mA')
print(f'A potência média liberada é igual a {p:.2f} W')