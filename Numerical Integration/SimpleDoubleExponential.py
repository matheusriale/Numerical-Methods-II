import math
from sympy import *

def funcao_exemplo_1(x): #INTEGRAL DE -1 A 1
  return 1.0 / ((x**2)**(1/3))

def funcao_exemplo_2(x): # INTEGRAL DE -2 A 0
  return 1.0 / ((4 - (x**2))**(1/2))

def x_s (ini, fim, s): #x(s)
  return ( ( ini + fim ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * tanh(s) )

def s_barra (ini, fim, s):
  return ( ( fim + ini ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * s )

def f_barra(ini, fim, s, funcao):
  return funcao(x_s(ini, fim, s)) \
       * ( ( fim - ini ) / 2.0 ) \
       * ( 1.0 / pow( cosh(s), 2 ) )

def f_barra_dupla(ini, fim, s, funcao): #
  return funcao(x_s_dupla(ini,fim,s)) * ((fim-ini)/2)*((math.pi/2)*(cosh(s))/pow(cosh((math.pi/2)*sinh(s)),2))

def x_s_dupla (ini, fim, s): #x(s)
  return ( ( ini + fim ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * tanh((math.pi/2)* sinh(s) ) )


def GaussLegendreExpSimples (ini, fim, iniC, fimC, qtdPontos, funcao, funcao_f_barra):
  
  if qtdPontos == 2:
    w1 = 1.0
    w2 = 1.0
    s1 = - 1.0 / sqrt( 3.0 )
    s2 = + 1.0 / sqrt( 3.0 )

    resultado = ( ( fimC - iniC ) / 2.0 ) \
          * ( ( funcao_f_barra( ini, fim, s_barra( iniC, fimC, s1 ), funcao ) * w1 ) \
          + ( funcao_f_barra( ini, fim, s_barra( iniC, fimC, s2 ), funcao ) * w2 ) )

  elif qtdPontos == 3:
    w1 = w3 = 5.0 / 9.0
    w2 = 8.0 / 9.0

    s1 = - sqrt( 3.0 / 5.0 )
    s2 = 0.0
    s3 = + sqrt( 3.0 / 5.0 )

    resultado = ( ( fimC - iniC ) / 2.0 ) \
            * ( ( funcao_f_barra(ini, fim, s_barra(iniC, fimC, s1), funcao) * w1 ) \
            + ( funcao_f_barra( ini, fim, s_barra( iniC, fimC, s2 ), funcao ) * w2 ) \
            + ( funcao_f_barra( ini, fim, s_barra( iniC, fimC, s3 ), funcao ) * w3 ) )

  return resultado

def GaussLegendreParticoesExpSImples (ini, fim, iniC, fimC, qtdPontos, eps, funcao, funcao_f_barra):
  print("\nGauss Legendre - - ")
  integralVelha = 0
  integralNova = integralVelha + eps + 1 #inicializar como infinito estava dando erro - esse valor garante que entrará no while
  N = 1

  while abs( ( integralNova - integralVelha ) / integralNova ) > eps:
    integralVelha = integralNova
    
    deltaX = ( fimC - iniC ) / N

    integralNova = 0
    print("  Calculando integral para N = ", N)
    for i in range(N):
      xIn = iniC + ( i * deltaX )
      xFin = xIn + deltaX
      integralNova += GaussLegendreExpSimples( ini, fim, xIn, xFin, qtdPontos, funcao, funcao_f_barra)

    N *= 2

    print("Nova = ", integralNova, 
          "| Diferença:", abs( ( integralNova - integralVelha ) / integralNova ))

  return integralNova


#exp - número exponenciacao | inicio/fim - inicio/fim do intervalo | qtdPontos - quantidade de partições | cInicial - primeiro valor de C | eps - tolerância | passo - passo de incremento de C
def substituicoes_de_C(exp, inicio, fim, qtdPontos, cInicial, funcao, eps = 0.0001, passo = 0.1):
  
  while exp != 1 and exp!=2:
    exp = int(input("Insira 1 ou 2 para a exponenciação: "))
    
  funcao_f_barra = f_barra if exp == 1 else f_barra_dupla
      
      

    
  #não deixar o usuário escolher outra quantidade de pontos que não seja 2 ou 3
  while qtdPontos != 2 and qtdPontos !=3:
    qtdPontos = int(input("Insira 2 ou 3 para a quantidade de pontos: "))
  
  print("Iniciando - - -")
  print("quantidade de pontos: ", qtdPontos)
  print("Intervalo: Inicio = ", inicio, "| Fim: ", fim)
  print("C inicial = ", cInicial, "| Passo = ", passo)
  print("Tolerância = ", eps)
  
  
  
  resultadoAntigo = 0
  resultadoNovo = resultadoAntigo + eps + 1 #inicializar como infinito estava dando erro - esse valor garante que entrará no while
  c = cInicial

  while abs( ( resultadoNovo - resultadoAntigo ) / resultadoNovo ) > eps:
    resultadoAntigo = resultadoNovo

    resultadoNovo = GaussLegendreParticoesExpSImples(inicio, fim, -1*c, c, qtdPontos, eps, funcao, funcao_f_barra)

    c += passo
    print("\nContinuando o incremento de C - -")
    print("Resultados : Novo = ", resultadoNovo,
        "| Antigo =  ", resultadoAntigo, 
         "| Diferença = ", abs( ( resultadoNovo - resultadoAntigo ) / resultadoNovo ))
    print("c = ", c)

    #caso não tenha obtido um resultado válido
    if math.isnan( resultadoNovo ) or resultadoNovo == float('inf') :
    
      c = cInicial
      passo /= 10
      resultadoNovo =  resultadoAntigo + eps + 1 #deixar inifnito tava dando erro. Essa expressão garante que entrará no while
      continue
    

  print(resultadoNovo, "\nPasso:", passo)
  return resultadoNovo
  

#Para funcao 1:
#substituicoes_de_C(2, -1, 1, 2, 1, funcao_exemplo_1, eps = 0.01, passo = 0.5)

#Para funcao 2:
substituicoes_de_C(2, -2, 0, 2, 1, funcao_exemplo_2, eps = 0.01, passo = 0.5)