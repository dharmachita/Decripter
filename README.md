##### Subido a Git para postulación de Computrabajo (Resolvé el desafío)

# Decripter
### Algoritmo que desencripta un texto utilizando sustitución monoalfabetica simple. Mediante el uso de un diccionario de pesos (frecuencia) de cuadragramas (4 caracteres) evalúa la probabilidad de que el texto sustituído pertenezca al idioma dado, devolviendo como resultado un *Array* con el *String* de mayor probabilidad y el alfabeto de sustitución usado.    


Se pueden identificar 4 partes escenciales que componen la resolución del problema:

1. La primera parte realiza una transliteración de los caracteres que se quiere decifrar a caracteres latinos en mayúscula.
2. Importando el archivo de frecuencia según el idioma seleccionado crea un diccionario de probabilidad de 4 caracteres, 
que determina la probabilidad de que un String de 4 caracteres pertenezca al idioma selecionado.
3. Genera una función de sustitución simple monoalfabetica que acepta el String a evaluar.
4. Compara el puntaje de probabilidad entre String sustituidos y vuelve a iterar hasta obtener el minimo puntaje (mayor probabilidad).


#### INSTANCIACION

1. Se crea una instancia del objeto **Funcion**. Los parámetros para la construcción del objeto Función son:
	1. *String - Texto Codificado* = El Texto que se quiere desencriptar.
	2. *Chr - Idioma* = **E** para español. **I** para Inglés.
	3. *Int - Iteraciones* = El número de veces que el algoritmo itera para obtener el String de mejor puntaje. Puede tomar valores entre 5000 y 100000.
	4. *Chr - Opcion* = Elije si se va a reemplazar un caracter del texto codificado por un espacio. (podría reemplazarse por un valor tipo Booleano).
	5. *Chr - Caracter* = Si opción es **True** o **S** (Si) acepta el caracter será reemplazado por un espacio.
2. Llamar al método *resolver()*. 
3. La variable devuelta es un *arreglo* cuyo primer elemento es un *String* con la mayor probabilidad y cuyo segundo elemento corresponde al alfabeto de sustitución usado para transliterar el texto codificado. 



##### FUENTE

Para el proyecto reuitilicé el código del siguiente enlace, y lo adapté a las necesidades del requerimiento:

[Décrypter une substitution monalphabétique](http://bribes.org/crypto/substitution_mono.html)
