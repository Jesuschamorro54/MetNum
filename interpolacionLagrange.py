import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#  Implemento la tabla de valores de x y F(x)
x = np.array( [1, 2, 3, 4, 5, 6] )
Fx = np.array([4.75, 5.00, 5.25, 10.75, 19.75, 36])

# Creo un simbolo para representar la incognita en este caso la letra x
varX = sym.Symbol('x')
polinomio = 0

for i in range(len(x)):
    numerador = 1
    denominador = 1

    for j in range (len(x)):

        if (i!=j):
            numerador = numerador * (varX-x[j]) #  (x - X[j])
            denominador = denominador * (x[i]-x[j]) # (X[i] - X[j])
            
        termino = (numerador/denominador)*Fx[i]

    polinomio += termino

polisimple = sym.expand(polinomio)
Px = sym.lambdify(varX,polinomio)


#vectores para graficas
muestras = 60
a = np.min(x)
b = np.max(x)
p_xi=np.linspace(a, b, muestras)
pfi=Px(p_xi)

print(f"\nPolinomio\n{polinomio}")


print(f"\nPolinomio simple\n{polisimple}")


#grafica
plt.plot(x, Fx, 'o')
plt.plot(p_xi, pfi)
plt.show()
