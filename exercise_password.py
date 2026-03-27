def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """

    contraseña = input()
    if "0" in contraseña or "1" in contraseña or "2" in contraseña or "3" in contraseña or "4" in contraseña or "5" in contraseña or "6" in contraseña or "7"in contraseña or "8" in contraseña or "9" in contraseña:
        tiene_numero = True
    else:
        tiene_numero = False

    if len(contraseña) >= 8:
        buena_longitud = True
    else:
        buena_longitud = False

    if tiene_numero == True and buena_longitud == True:
        print("Contraseña valida")

    elif tiene_numero == True and buena_longitud == False:
        print("Contraseña muy corta")

    elif tiene_numero == False and buena_longitud == True:
        print("Debe contener un numero")

    elif tiene_numero == False and buena_longitud == False:
        print("Contraseña muy corta\nDebe contener un numero")

