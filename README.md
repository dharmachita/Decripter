##### Subido a Git para postulación de Computrabajo (Resolvé el desafío)

# Decripter
### Algoritmo que desencripta un texto utilizando probabilidad de pertenencia en un idioma y sustitución monoalfabetica simple


Se pueden identificar 4 partes escenciales que componen la resolución del problema:

1. La primera parte realiza una transliteración de los caracteres que se quiere decifrar a caracteres latinos en mayúscula.
2. Importando el archivo de frecuencia según el idioma seleccionado crea un diccionario de probabilidad de 4 caracteres, 
que determina la probabilidad de que un String de 4 caracteres pertenezca al idioma selecionado.
3. Genera una función de sustitución simple monoalfabetica que acepta el String a evaluar.
4. Compara el puntaje de probabilidad entre String sustituidos y vuelve a iterar hasta obtener el minimo puntaje (mayor probabilidad).


#### USO

1. Ingresar el texto a decodificar -> Devuelve el texto transliterado en un alfabeto latino de 26 caracteres.
2. Si en esta instancia se ha identificado que un caracter podría representar un espacio, ingresar dicho caracter. 
De lo contrario comentar ésta instrucción `t=t.replace(caracter,'_')`
*Si se usa el caracter de separación se debe importar el archivo con espacios en el idioma que se quiere analizar*
3. Seleccionar el idioma. Se importará el archivo de frecuencia de los cuadragramas.
4. Ingresar el numero de iteraciones. Generalemente funciona bien con mayores iteraciones, en un rango de 8000 a 30000.



##### FUENTE

Para el proyecto reuitilicé el código del siguiente enlace, y lo adapté a las necesidades del requerimiento:

[Décrypter une substitution monalphabétique](http://bribes.org/crypto/substitution_mono.html)
