def email_validation(email):
    """Valida un email ingresado por el usuario utilizando una expresión regular."""

    # Explicación de la expresión regular:
    # ^ - Inicio de la cadena
    # [^@\.] - Cualquier carácter excepto @ o .
    # [^@]* - Cualquier cantidad de caracteres excepto @ 
    # @ - El carácter @
    # [^@\.]+ - Al menos un carácter después del @ que no sea @ o .
    # \. - El carácter .
    # [^@\.]{2,} - Al menos dos caracteres después del último punto que no sean @ o .

    import re
    pattern = r'^[^@\.][^@]*@[^@\.]+\.[^@\.]{2,}$'

    return True if re.match(pattern, email) else False

def print_email_info():
    """Solicita al usuario que ingrese un email y muestra si es válido o no."""

    email = input("Ingrese un email: ")
    print("El email es válido" if email_validation(email) else "El email es inválido")

if __name__ == "__main__":
    print_email_info()