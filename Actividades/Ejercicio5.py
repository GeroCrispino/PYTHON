#5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras,
#y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir
#entre mayúsculas y minúsculas.

frase = input("Ingrese una frase\n")
palabras = frase.lower().split(" ")
string = input("Ingrese una palabra\n")
palabra = string.lower()

print("Cantidad de veces que aparece la palabra",string,": ",palabras.count(palabra))