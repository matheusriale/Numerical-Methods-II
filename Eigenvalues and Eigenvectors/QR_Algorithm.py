# -*- coding: utf-8 -*-
"""Tarefa12_QR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pcyw078KvqyMB-sj2wTOxI01ULIqzgEZ
"""

import numpy as np
import math

def identity(n):
  M = []
  for i in range(0,n):
    linha = []
    for j in range(0,n):
      if j == i:
        linha.append(1)
      else:
        linha.append(0)
    M.append(linha)
  return M

def roundMatrizes(M,n):
  R = []
  linhas = []
  for i in range(0,n):
    for j in range(0,n):
      linhas.append(round(M[i][j],2))
    R.append(linhas)
    linhas = []
  return R

def somaQuadradosAbaixoDiagonal(A,n):
  valor = 0
  R = A.copy()
  for i in range(0,n):   
    for j in range(0,n):
      if i>j:
        valor = valor + (R[i][j]**2)
  return valor

def matrizJacobi(A,i,j,n):
    eps = 0.000001
    J_ij = identity(n)
    if (abs(A[i][j])<= eps ):
      return J_ij
    if (abs(A[j][j]) <= eps):
      if(A[i][j] < 0):
        theta = math.pi/2
      else:
        theta = -math.pi/2
    else:
      theta = math.atan(-1*A[i][j]/A[j][j])
    J_ij[i][i] = math.cos(theta)
    J_ij[j][j] = math.cos(theta)
    J_ij[i][j] = math.sin(theta)
    J_ij[j][i] = -math.sin(theta)

    return J_ij

def decompQR(A,n):
  QT = identity(n)
  R_velha = A.copy()
  for j in range(0,n-1):
    for i in range(j+1,n):
      J_ij = matrizJacobi(R_velha,i,j,n)
      R_nova = np.dot(J_ij,R_velha)
      R_velha = R_nova.copy()
      QT = np.dot(J_ij,QT)
  Q = np.transpose(QT)
  R = R_nova.copy()
  return (Q,R)


def metodoQR(A,n,eps):
  val = 100.0
  lamb = []
  P = identity(n)
  A_velha = A.copy() 
  m_iter = [] #guardar iterações das matrizes
  v_A_nova = []#guardar A_novas para caso de householder
  while val > eps:
      (Q,R) = decompQR(A_velha,n)
      m_iter.append(Q)
      m_iter.append(R)
      A_nova = np.dot(R,Q)
      v_A_nova.append(A_nova)
      A_velha = A_nova.copy()
      P = np.dot(P,Q)
      val = somaQuadradosAbaixoDiagonal(A_nova,n)
  #end while
  for i in range(0,n):
    lamb.append(A_nova[i][i])
  A_nova = roundMatrizes(A_nova,5)
  return (P,lamb,A_nova,m_iter,v_A_nova)


A = [[40,8,4,2,1],
     [8,30,12,6,2],
     [4,12,20,1,2],
     [2,6,1,25,4],
     [1,2,2,4,5 ]]

v = metodoQR(A,5,0.00001)

#1.I) Matriz A diagonal
print("\nMatriz A diagonal")
for i in v[2]:
  print(i)

#II) Matriz P acumulada
print("\nMatriz P acumulada")
for i in v[0]:
  print(i)

'''#III)
print("\nMatrizes que saem a cada iteração de QR (Q1, R1, Q2, R2,...)")
for i in v[3]:
  print("")
  for j in roundMatrizes(i,5):
    print(j)
'''
#IV)

print("\n--------Pares Autovalor, Autovetor da matriz A--------")
for i in range(0,5):
  k = np.transpose(v[0])
  print(v[1][i],k[i])



#2.I)
A_tridiagonal = [[40.0, 9.22, 0.0, -0.0, -0.0],
                  [9.22, 39.82, 4.07, -0.0, -0.0],
                  [0.0, 4.07, 15.07, 6.29, 0.0],
                  [-0.0, -0.0, 6.29, 17.59, 5.87],
                  [-0.0, 0.0, 0.0, 5.87, 7.52]]

v2 = metodoQR(A_tridiagonal,5,0.00001)
'''
print("\nImprimir A_nova a cada iteração")
for i in v2[4]:
  for j in roundMatrizes(i,5):
    print(j)
  print("")
'''
#II)
print("Verificar que colunas de P não são autovetores de A")
print(v2[0])
#III)
print("\nFazer P = HP, verificar que as novas colunas de P são autovetores de A.")
H=[[1.0, 0.0, 0.0, 0.0, 0.0], #Matriz resultante H da tarefa anterior
  [0.0, 0.87, -0.44, 0.09, 0.21],
  [0.0, 0.43, 0.55, -0.6, -0.38],
  [0.0, 0.22, 0.7, 0.59, 0.34],
  [0.0, 0.11, -0.08, 0.53, -0.84]]

print(np.dot(H,v2[0]))
#IV)