import random, string

# words = [
#     "python",
#     "programa",
#     "variable",
#     "funcion",
#     "bucle",
#     "cadena",
#     "entero",
#     "lista",
# ]

# word = random.choice(words)

words = {
    "elementos básicos": ["python", "programa", "variable"],
    "estructuras de control": ["funcion", "bucle"],
    "tipos de datos": ["entero", "cadena", "lista"],
}
word = None

while not word:
    print("Categorías disponibles:")
    for i, category in enumerate(words):
        print(f"- {i + 1}. {category}")
    print()

    selected_category = int(input("Seleccioná una categoría: ")) - 1

    if 0 <= selected_category < len(words):
        category = list(words.keys())[selected_category]
        print(f"Has seleccionado: {category}")

        word = random.choice(words[category])

    print()
    
guessed = []
attempts = 6
mistakes = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        print(f"Puntaje final: {max(0, 6 - mistakes)}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if letter.lower() not in string.ascii_lowercase:
        print("Entrada no válida.")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        mistakes += 1
        print("Esa letra no está en la palabra.")

    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    print("Puntaje final: 0")
