import sympy
from sympy import *
import math

def pol_hermite(degree):
    
    x = Symbol('x')
    y = exp((-1)*((x)**2))
    for i in range(0,degree):
        y = y.diff(x)
        
    H = ((-1)**degree) * (exp(x**2))*y 
     
    return H


def pol_laguerre(degree):
    
    x = Symbol('x')
    y = (math.e**(-x)) * (x**degree)
    for i in range(0,degree):
        y = y.diff(x)
    L = ((exp(x))/factorial(degree))*y
    
    return L


def pol_chebyshev(degree):
    x = Symbol('x')
    y = (1-(x**2))**(degree - (1/2))
    for i in range(0,degree):
        y = y.diff(x)
    
    C = (((((-2)**degree) * factorial(degree))/factorial(2*degree))*(1-(x**2))**(1/2)) * y
        
    return C


def find_roots(H,L,C):#receber os 3 polinomios
    
    h_roots = sympy.solve(H,'x')
    l_roots = sympy.solve(L,'x')

    c_roots = sympy.solve(C,'x')
    #Arredondar os valores (precisão de 5 casas decimais)
    
    for i in range(0,len(h_roots)):
      h_roots[i] = round(h_roots[i],5)
    for j in range(0,len(l_roots)):
      l_roots[j] = round(l_roots[j],5)
    for k in range(0,len(c_roots)):
      c_roots[k] = round(c_roots[k],5)
      
    if ((len(l_roots) == 3) and (l_roots[2] <6)):
          l_roots.append(9.39507)#x4 de Laguerre de grau 4#x4 de Laguerre de grau 4
    #para laguerre de grau 4, solve, não retorna a última raiz(problema no solve), vamos contornar apenas esse caso específico
     
      
    v = [h_roots,l_roots,c_roots]
    return v


def weight_h(degree,solutions): #k contador no somatorio, solutions = find_roots
  x = Symbol('x')
  w_hermite = [0]*degree
  L = [1]*degree
# Lagrange L
  for j in range(0,degree):
    for i in range(0,degree):
      if j != i:
        L[j] = L[j] * ((x - solutions[i])/(solutions[j] - solutions[i]))
  #calculo do peso
  for i in range (0,degree): 
    w_hermite[i] = round(integrate(exp(-1*(x**(2)))*L[i],('x',-oo,oo)),5)
  return w_hermite


def weight_l(degree,solutions):                                 
    x = Symbol('x')
    w_laguerre = [0]*degree
    L = [1]*degree
    
    for j in range(0,degree):
      for i in range(0,degree):
        if j != i:
          L[j] = L[j]* ((x - solutions[i])/(solutions[j] - solutions[i]))
    
    for i in range (0,degree):
        
      w_laguerre[i] = round(integrate(exp(-x) *L[i],(x,0,oo)),5)
    return w_laguerre


def weight_c(degree,solutions):                                
    w_chebyshev = [0]*degree
    for i in range (0,degree):
      
      w_chebyshev[i] = round(math.pi/degree , 5)
    return w_chebyshev



def factorial(n):
    if n == 0:
        return 1
    else :
        return n*factorial(n-1)

def function(x):
      return cos(x)

def gauss_hermite(degree,weight_h,solutions): 
    I= 0
    for i in range(0,degree):
        I = I + (weight_h[i]*function(solutions[i]))
    return I
  
def gauss_laguerre(degree,weight_l,solutions):
    I= 0
    for i in range(0,degree):
        I = I + (weight_l[i]*function(solutions[i]))

    return I 
  
def gauss_chebyshev(degree,weight_c,solutions):
    I=0
    for i in range(0,degree):
        I = I + (weight_c[i]*function(solutions[i]))
    return I

#Solucões para grau 4: Vetor solucoes e vetor de pesos.
k = int(input("Escolha o grau para os polinômios(2, 3 ou 4):"))
solutions = find_roots(pol_hermite(k),pol_laguerre(k),pol_chebyshev(k))
pesos_h = weight_h(k,solutions[0])
pesos_l = weight_l(k,solutions[1])
pesos_c = weight_c(k,solutions[2])

print("--- Solucoes para grau = ",k,"---")

print("Hermite: \nRaízes:", solutions[0]," Pesos:", pesos_h)
print("\nLaguerre: \nRaízes:", solutions[1]," Pesos:", pesos_l)
print("\nChebyshev: \nRaízes:", solutions[2]," Pesos:", pesos_c)

print("\nResultado da função com quadratura de Gauss-Hermite:")
print(gauss_hermite(k,pesos_h,solutions[0]))
print("Resultado da função com quadratura de Gauss-Laguerre:")
print(gauss_laguerre(k,pesos_l,solutions[1]))
print("Resultado da função com quadratura de Gauss-Chebyshev:")
print(gauss_chebyshev(k,pesos_c,solutions[2]))


