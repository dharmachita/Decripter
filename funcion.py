"""
***************** DECODIFICADOR EN PYTHON **********************
***************Autor: MAURO EMMANUEL RAMBO *****************"""

from math import exp
from math import log10
import random


k = input("Ingrese el texto que desea decodificar: ")
k = k.replace(' ','') #en caso de que el texto tenga espacios
alpha26 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #alfabeto de 26 caracteres
t = '' 
alpha = {}
idx = 0

"""Reemplazo de los caracteres en el texto cifrado  
por texto con caracteres latino en mayuscula"""

for c in k:
  if c not in alpha:
    alpha[c] = alpha26[idx]
    idx += 1
  t += alpha[c]

print('-----------------------------------------------------------------')
print(' ')
print('La transliteracion del texto seleccionado es la siguiente:',t)
print(' ')
print('-----------------------------------------------------------------')
print(' ')

"""Si se sabe que el texto posee espacio, y se tiene una hipótesis sobre el caracter
que se usa como espacio, se puede reemplazar el mismo por un guion bajo y 
usar el archivo xxxx_espacios.txt

Si no se reconoce el espacio comentar esta instruccion y usar el archivo sin espacios"""

caracter=input('Seleccione el caracter que corresponde a los espacios: ')
t=t.replace(caracter,'_')
print('-----------------------------------------------------------------')
print(' ')


#Elegir el idioma con el que se va a hacer la prueba


while True:
  idioma=input('Seleccione el idioma del texto a analizar Ingles(I), Español(E), Frances(F), Aleman(A), Italiano (IT): ')
  print('-----------------------------------------------------------------')
  print(' ')
  if idioma == 'I':
    f = open('frecuencias\\ingles_espacios.txt')
    print("Idioma seleccionado Ingles")
    print('-----------------------------------------------------------------')
    print(' ')
    break
  elif idioma == 'E':
    f = open('frecuencias\\espanol_espacios.txt')
    print("Idioma seleccionado Español")
    print('-----------------------------------------------------------------')
    print(' ')
    break
  elif idioma == 'A':
    f = open('frecuencias\\aleman_espacios.txt')
    print("Idioma seleccionado Español")
    print('-----------------------------------------------------------------')
    print(' ')
    break
  elif idioma == 'F':
    f = open('frecuencias\\frances_espacios.txt')
    print("Idioma seleccionado Español")
    print('-----------------------------------------------------------------')
    print(' ')
    break 
  elif idioma == 'IT':
    f = open('frecuencias\\italiano_espacios.txt')
    print("Idioma seleccionado Español")
    print('-----------------------------------------------------------------')
    print(' ')
    break       
  else:
    print("Idioma No Seleccionado")
    print(' ')


"""Se crea un diccionario que devuelve la frecuencia de
un conjunto determinado de 4 letras para un idioma definido 
ver Proyecto Gutenberg"""

f4g={}
total=0
for line in f:
  (w,c)=line.split(" ")
  f4g[w]=int(c)
  total += int(c)
for w in f4g:
  f4g[w] /= total
f.close


"""Se determina un puntaje en base logaritmica para poder comparar cadenas de longitud variable
y determinar la probabilidad de que dicha cadena pertenezca a un idioma determinado"""

def logscore(s):
  logsum=0
  min_freq = 1e-100
  for i in range(len(s)-3):
    logsum += log10(f4g.get(s[i:i+4], min_freq))
  return -logsum


"""Funcion de subsitucion monoalfabetica simple
recibe un alfabeto y un String"""
def simple_substitution(alpha,s):
  r=''
  for c in s:
    if c in alpha26:
      r += alpha[ord(c)-ord('A')]
    else:
      r += c
  return r


"""Funcion que mezcla aleatoreamente los caracteres de un String s"""
def string_shuffle(s):
  c = list(s)
  random.shuffle(c)
  return ''.join(c)


def new_state(alpha):
  c=list(alpha)
  i=random.randint(0,25)
  j=random.randint(0,25)
  while j == i:
    j=random.randint(0,25)
  if random.random()<0.5:
    c[i],c[j]=c[j],c[i]
  else:
    if i>j:
      i,j=j,i
    m=c[i:j]
    m.append(m.pop(0))
    c[i:j]=m
  return ''.join(c)


""""La funcion criterion se utiliza para comparar los logscore de las 
subsituciones y aceptarlas o rechazarlas segun"""

def criterion(delta,T):
  if delta <= 0: return True
  if random.random()<exp(-delta/T):return True
  return False


"""El algoritmo acepta un String cifrado, al cual le realiza sustituciones simples con un
alfabeto y calcula la probabilidad (logscore) de que dicha sustitucion pertenezca a un idioma
determinado, a su vez realiza una aleatorizacion de dicho alfabeto y realiza las comparacion
anteriormente mencionada de forma iterada para comparar los scores hasta obtener el minimo conforme
a las iteraciones aplicadas.
Devuelve el mensaje sustituido con el alfabeto que ha obtenido el score mas bajo (mayor probabilidad) 
"""

def  AnnouncementSS ( crypto ,  max_iter  =  8000 ,  CoolRatio  =  0.8  ): 
    alpha  =  string_shuffle ( alpha26 ) 
    old_score  =  logscore ( simple_substitution ( alpha ,  crypto )) 
    T  =  0 
    for  i  in  range ( 100 ):   
        alpha  =  string_shuffle ( alpha) 
        new_score  =  logscore ( simple_substitution ( alpha ,  crypto )) 
        delta  =  new_score  -  old_score 
        if  delta  >  T :  T  =  delta 
        old_score  =  new_score 
    T  *=  10                
    best_alpha  =  alpha 
    best_score  =  old_score 
    freeze  =  0 
    while  True : 
        nb_iter  =  0 
        while  nb_iter  < max_iter : 
            Nalpha  =  new_state ( alpha ) 
            new_score  =  logscore ( simple_substitution ( Nalpha ,  crypto )) 
            delta  =  new_score  -  old_score 
            if  criterion ( delta ,  T ):  
                alpha  =  Nalpha 
                old_score  =  new_score 
                if  old_score  <  best_score : 
                    best_score  =  old_score 
                    best_alpha  = alpha 
                freeze  =  0 
            else :                              
                freeze  +=  1 
            nb_iter  +=  1 
        T  *=  CoolRatio 
        if  freeze  >  25 :
            break 
    return simple_substitution ( best_alpha ,  crypto )  


iteraciones=int(input("Ingrese el numero de iteraciones (generalmente entre 8000 y 30000: "))

decifrado = AnnouncementSS(t, max_iter=iteraciones)

print(decifrado)




