import random, string

WORDS = {
    "elementos básicos": ["python", "programa", "variable"],
    "estructuras de control": ["funcion", "bucle"],
    "tipos de datos": ["entero", "cadena", "lista"],
}
VALID_CHARS = string.ascii_lowercase + "áéíóúüñ"
TRIES = 6

score = 0
category = None

print("¡Bienvenido al Ahorcado!")
while True:
    while not category:
        print("\nCategorías disponibles:")
        for i, cat_name in enumerate(WORDS):
            print(f"- {i + 1}. {cat_name}")

        selected_category = int(input("\nSeleccioná una categoría: ")) - 1

        if selected_category in range(0, len(WORDS)):
            # Obtengo el nombre de la categoría seleccionada a partir del índice
            category = list(WORDS.keys())[selected_category]

            # Verifico que la categoría tenga palabras disponibles
            if len(WORDS[category]) == 0:
                category = None
                print("No hay palabras en esta categoría.\n")
                continue
        else:
            # El número ingresado no corresponde a ninguna categoría
            print("Categoría no válida.\n")
            continue
        
    # Recorro las palabras de la categoría en orden aleatorio
    for word in random.sample(WORDS[category], len(WORDS[category])):
        guessed = []
        missed = 0

        # Verifico cuantos intentos le quedan al jugador
        while missed < TRIES:

            # Verificar si el jugador ha adivinado todas las letras
            if all(letter in guessed for letter in word):

                # Sumo 6 por haber acertado
                score += 6

                # Resto 1 por cada letra errada
                score -= missed

                print(f"¡Ganaste! La palabra era {word}", end=" | ")
                break

            # Muestro las letras adivinadas y guiones bajos para las no adivinadas
            print(
                " ".join(
                    letter if letter in guessed else "_" 
                    for letter in word
                ),
                end="\n\n"
            )

            print(f"Categoría: {category:<15}", f"Letras usadas: [{', '.join(guessed)}]", sep=" | ")
            print(f"Intentos restantes: {TRIES - missed}", f"Ingresá una letra: ", sep=" | ", end="")

            letter = input().lower()

            # Verificar que se haya ingresado una sola letra
            if len(letter) != 1:
                print("Ingresá una sola letra.")
                continue

            # Validar que se haya ingresado una letra válida
            if letter not in VALID_CHARS:
                print("Entrada no válida.")
                continue

            # Verificar si la letra ya fue utilizada
            elif letter in guessed:
                print("Ya usaste esa letra.")
                continue

            # La letra no está en la palabra
            elif letter not in word:
                missed += 1

            # Agregar la letra a las utilizadas
            guessed.append(letter)

            print()
        else:
            # Pongo el score en 0 porque el jugador perdió
            score = 0

            print(f"¡Perdiste! La palabra era: {word}", end=" | ")

        print(f"Puntaje: {score}\n")

    # Al terminar todas las palabras de la categoría
    while True:
        print("\nNo quedan más palabras en esta categoría!")
        match input("¿Querés jugar otra vez? (S/n): ").lower():
            case "s" | "":
                # Resetear la categoría para jugar de nuevo
                category = None
                break
            case "n":
                # Salir del juego
                print("\n¡Gracias por jugar!")
                exit()
            case _:
                # Entrada no válida, preguntar de nuevo
                continue
