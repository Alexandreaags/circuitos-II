import cmath
import numpy as np

A = np.array([[complex(44,-18), complex(-38,15)],
            [complex(16.75,-6), complex(-10,6)]])
B = np.array([200,complex(87.5, -21.65)])
x = np.linalg.solve(A, B)
Ia = x[0]
Ic = x[1]
Ib = complex(-2.5, -4.33) + Ia/4 + Ic/2
Ia1 = Ia
Ib1 = Ib - Ia
Ic1 = (-1)*Ib
print(f'A corrente de linha Ia é igual a {Ia1:.2f} A')
print(f'A corrente de linha Ib é igual a {Ib1:.2f} A')
print(f'A corrente de linha Ic é igual a {Ic1:.2f} A')

Pa = abs(Ia - Ic)**2 * 8
Pb = abs(Ic)**2 * 4
Pc = abs(Ib - Ic)**2 * 10
Pativa = Pa + Pb + Pc
##print(f'{Pa:.2f} {Pb:.2f} {Pc:.2f}')
print(f'A potência ativa total absorvida é {Pativa:.2f} W')
