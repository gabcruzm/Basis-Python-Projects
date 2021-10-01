def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escriba una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
    # if palindromo(palabra) == True: --> Esto se puede hacer para simplificar
        print("Es palíndromo")
    else: 
        print("No es palíndromo")

#EntryPoint = Punto de entrada 
if __name__ == "__main__":
    run()

