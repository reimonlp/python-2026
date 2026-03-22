def input_friends(force=None):
    """Solicita al usuario ingresar los nombres de sus amigos invisibles separados por coma y devuelve una lista de nombres no duplicados."""

    raw = force if force is not None else input("Ingrese los participantes (separados por coma): ")

    unique_names = []
    seen_keys = set()

    for name in raw.split(","):
        cleaned = " ".join(name.split())   # quita espacios extra (inicio, fin y repetidos)
        if not cleaned:
            continue

        key = cleaned.casefold()           # solo para comparar, no para mostrar
        if key not in seen_keys:
            seen_keys.add(key)
            unique_names.append(cleaned)   # conserva formato original limpio

    return unique_names

def draw_invisible_friends(friends):
    """Realiza el sorteo de amigo invisible y devuelve un diccionario con los resultados."""

    invisible_pairs = {}

    import random
    friends_left = friends[:]
    random.shuffle(friends_left)

    for friend in friends:
        available = [inv for inv in friends_left if inv != friend]
        if available:
            invisible = available[0]
            invisible_pairs[friend] = invisible
            friends_left.remove(invisible)
        else:
            return draw_invisible_friends(friends)
    
    return invisible_pairs

def print_invisible_friends():
    """Solicita al usuario ingresar los nombres de sus amigos invisibles y luego los muestra en pantalla."""

    friends = input_friends()

    # Para pruebas, se puede usar la siguiente línea en lugar de la anterior:
    # friends = input_friends("Alice, Bob, Charlie, David, Eve, Frank, Grace, Heidi, Ivan, Judy")

    if not friends:
        print("No se ingresaron participantes.")
        return
    elif len(friends) < 3:
        print(f"Debe haber al menos 3 participantes.")
        return

    invisible_pairs = draw_invisible_friends(friends)

    print("Sorteo de amigo invisible:")
    for friend in friends:
        print(f"  {friend} → {invisible_pairs[friend]}")

if __name__ == "__main__":
    print_invisible_friends()
