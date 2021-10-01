#Imprimir todas las potencias de 2 hasta llegar al # 1000
#contador = 0
# print("2 elevado a " + str(contador) + "es igual a: " + str(2**contador))

#contador = 1
# print("2 elevado a " + str(contador) + "es igual a: " + str(2**contador))

#contador = 2
# print("2 elevado a " + str(contador) + "es igual a: " + str(2**contador))

#Es por esto que aprender bucles - ciclo while es IMPORTANTE! Buenas prácticas

def run(): 
    LIMITE = 1000000 #variable NO cambia. Variable Constante.

    contador = 0 #va a ir aumentando para multiplicar a 2 por tantas veces que el contador lo diga.
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: #mientras la potencia de 2 sea menor al limite se va a ejecutar lo de abajo. Mientras esa condicion se cumple, se va a ejecutar lo que se coloca debajo de la prox. linea
        print("2 elevado a " + str(contador) + "es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador 


if __name__ + "__main__":
    run()