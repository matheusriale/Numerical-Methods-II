import sympy
from sympy import *

def function(x):
  return sin(x)

#parâmetros: limite inferior, limite superior, numero de pontos, vetor dos x(alpha1), x(alpha2)...
def GaussLegendre( xi, xf, n_pontos,w, vxs):
  soma = 0
  for i in range(0,n_pontos):
    soma = soma + (function(vxs[i]) * w[i]) 
  result = ((xf-xi)/2)* soma
  
  return result
#retorna resultado da aproximacao por Gauss-Legendre


#parâmetros: Polinomio que iremos encontrar as raizes
def roots(polinomio):
  solutions = sympy.solve(polinomio,'a')
  return solutions
#retorna vetor de soluções do polinomio de legendre

def x_s(xi,xf,grau,solutions):
  v = [0]*grau #vetor que possui os x_s
  for i in range(0,grau):
    v[i] = ((xi+xf)/2) - ((xf -xi)/2)*solutions[i] 
    #print(((xi+xf)/2) - ((xf -xi)/2)*solutions[i])
  return v



def weight(grau, solutions ):
  w = [0]*grau #vetor de pesos
  L = [1]*grau
  #a = 0
  a = Symbol('a')
  for j in range(0,grau):
    for i in range(0,grau):
      if j != i:
        
        L[j] = L[j]* ((a - solutions[i])/(solutions[j] - solutions[i]))
        
  for i in range(0,grau):
    w[i] = integrate(L[i],('a',-1,1))
    
  return w



def factorial(n):
  if n>1:
    return n*factorial(n-1)
  else:
    return 1

#função para retornarmos o polinômio de Legendre de determinado grau
def LegendreP(grau):
  a = Symbol('a')
  y = ((a**2) - 1) ** grau
  
  for i in range(0,grau):
    y = y.diff(a) 
    
  polinomio = (1/((2**grau)*factorial(grau))) * y  
  return polinomio


#--------------------------------------------------------------#
#teste = x_s(2,2,4,roots(LegendreP(4))) 
#print(roots(LegendreP(4)))
#print(teste)
#print(weight(3,[-5,1,2] )) 

solutions = roots(LegendreP(4))
vxs = x_s(0,1,4,solutions)

#calcular os x(alpha 1), x(alpha 2) ... e atribuir ao vetor vxs

w = weight(4,solutions)
sol = GaussLegendre( 0, 1, 4,w, vxs)

#print(vxs)
#print(w)
print("Solucao:",sol)