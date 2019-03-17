from funcion import Funcion


while True:
	inTexto=input("\nIngrese Texto que desea decodificar: ")
	inTexto=inTexto.replace(" ","")
	if inTexto != "":
		break

while True:		
	inOpcionEspacio=input("¿Reemplazar caracter de espacio?(S/N): ")
	if inOpcionEspacio == "S":
		while True:
			inCaracter=input("Ingrese Caracter: ")
			if len(inCaracter) == 1:
				break
		break				
	elif inOpcionEspacio == "N":
		inCaracter=" "
		break
	else:
		print("Opción inválida")	

while True:	
	inIdioma=input("Ingrese Idioma del diccionario \nEspañol (E)/Inglés (I)): ")
	if inIdioma == "E" or inIdioma == "I":
		break
	else:	
		print("Opción inválida")
while True:		
	inIteraciones=int(input("Ingrese nro de iteraciones: "))
	if inIteraciones in range (5000,100001):
		break
	else:	
		print("Opción inválida. Elija una valor entre 5000 y 100000")	


deco = Funcion(inTexto,inIdioma,inIteraciones,inOpcionEspacio,inCaracter)
resultado=deco.resolver()

print(resultado)	