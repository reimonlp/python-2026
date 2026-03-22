review = """La película sigue a un grupo de astronautas que viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo a través
de tormentas solares y fallos en el sistema de navegación. Al llegar
a Marte descubren que la base está abandonada y los suministros
destruidos. Torres decide sacrificar la nave nodriza para salvar
al equipo y logran volver a la Tierra en una cápsula de emergencia.
El final revela que Torres sobrevivió gracias a un pasaje secreto."""

def hide_spoilers(review, spoiler_words):
    """Reemplaza las palabras spoiler en la reseña con asteriscos."""

    import re
    for word in spoiler_words:
        review = re.sub(re.escape(word), "*" * len(word), review, flags=re.IGNORECASE)

    return review

def spoiler_words_input():
    """Solicita al usuario que ingrese las palabras spoiler y las devuelve como una lista."""

    spoiler_words = input("Ingrese las palabras spoiler (separadas por coma): ").split(",")

    # Eliminar espacios en blanco alrededor de las palabras
    spoiler_words = list(map(str.strip, spoiler_words))

    return spoiler_words

def print_review_without_spoilers(review=review):
    """Solicita al usuario las palabras spoiler, oculta esas palabras en la reseña y muestra el resultado."""
    
    spoiler_words = spoiler_words_input()
    review_clean = hide_spoilers(review, spoiler_words)
    
    print(f"\n{review_clean}")

if __name__ == "__main__":
    print_review_without_spoilers()

