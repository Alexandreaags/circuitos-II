import cmath

print('a) A conexão é delta-estrela')
n = 1/3
Vlp = 450
Vls = n*Vlp/cmath.sqrt(3)
Ia = Vls/complex(8,-6)
# Ib é igual a Ia defasado de -120 graus
Ib = complex(1.036, -8.598)
I1 = n*cmath.sqrt(3)*Ia
print(f'b) As correntes Ia, Ib e I1 são, respectivamente, {Ia:.2f} A, {Ib:.2f} A e {I1:.2f} A')

p = 3*abs(Ia)**2 * 8/1000
print(f'c) A potência média absorvida pela carga é {p:.1f}kW')