from math import exp
from math import log10
import random


class Funcion(object):

	def __init__(self, textoCodificado, idioma, iteraciones,opcion,caracter=" "):
		self.textoCodificado=textoCodificado
		self.idioma=idioma
		self.iteraciones=iteraciones
		self.opcion=opcion
		self.caracter=caracter
		
	def transliterar(self, texto, alfabeto):
		transliterado = '' 
		alpha = {}
		idx = 0
		for c in texto:
			if c not in alpha:
				alpha[c] = alfabeto[idx]
				idx += 1
			transliterado += alpha[c]
		return transliterado		

	alpha26 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	def elijeIdioma(self, idioma, opcion):		
		if self.idioma == 'E':
			idi='espanol'
		else:
			idi='ingles'	
		if self.opcion == "S":
			sp='_espacios'
		else: sp=''		
		ruta='frecuencias\\'+idi+sp+'.txt'
		f = open(ruta)
		f4g={}
		total=0
		for line in f:
			(w,c)=line.split(" ")
			f4g[w]=int(c)
			total += int(c)
		for w in f4g:
			f4g[w] /= total
		f.close
		return f4g	

	def string_shuffle(self,alfabeto):
		c = list(alfabeto)
		random.shuffle(c)
		return ''.join(c)

	def logscore(self,textoAnalisis, cuadragrama):
		logsum=0
		min_freq = 1e-100
		for i in range(len(textoAnalisis)-3):
			logsum += log10(cuadragrama.get(textoAnalisis[i:i+4], min_freq))
		return -logsum

	
	def simple_substitution(self,alpha,s):
		r=''
		for c in s:
			if c in self.alpha26:
				r += alpha[ord(c)-ord('A')]
			else:
				r += c
		return r 	

	def new_state(self,alpha):
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

	def criterion(self,delta,T):
		if delta <= 0: return True
		if random.random()<exp(-delta/T):return True
		return False  				


	def resolver(self, CoolRatio = 0.8):
		transliteracion = self.transliterar(self.textoCodificado,self.alpha26)
		if self.caracter is not " ":
			cadena = self.textoCodificado
			lista = []
			pos_inicial = -1
			try:
				while True:
					pos_inicial = cadena.index(self.caracter, pos_inicial+1)
					lista.append(pos_inicial)
			except ValueError:
				for i in lista:
					transliteracion=transliteracion.replace(transliteracion[i],"_")
		quadragrame=self.elijeIdioma(self.idioma,self.opcion)
		alpha  =  self.string_shuffle(self.alpha26) 
		old_score  =  self.logscore(self.simple_substitution(alpha, transliteracion),quadragrame)
		T  =  0 		
		for  i  in  range ( 100 ):   
			alpha  =  self.string_shuffle ( alpha)
			new_score  =  self.logscore ( self.simple_substitution ( alpha ,  transliteracion ),quadragrame)
			delta  =  new_score  -  old_score
			if  delta  >  T :  T  =  delta
			old_score  =  new_score
		T  *=  10                
		best_alpha  =  alpha 
		best_score  =  old_score 
		freeze  =  0 
		while  True : 
			nb_iter  =  0 
			while  nb_iter  < self.iteraciones :
				Nalpha  =  self.new_state ( alpha ) 
				new_score  =  self.logscore ( self.simple_substitution ( Nalpha ,  transliteracion ),quadragrame) 
				delta  =  new_score  -  old_score 
				if  self.criterion ( delta ,  T ):  
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
		resultado=self.simple_substitution ( best_alpha ,  transliteracion )
		resultado=resultado.replace("_"," ")		 
		return (resultado, best_alpha)



