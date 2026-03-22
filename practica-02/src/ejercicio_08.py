def cesar_cipher(text, shift):
    """Aplica el cifrado César a letras ASCII (A-Z, a-z) con un desplazamiento específico."""

    encrypted = ""
    shift_amount = shift % 26

    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            encrypted += chr((ord(char) - base + shift_amount) % 26 + base)
        elif 'A' <= char <= 'Z':
            base = ord('A')
            encrypted += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encrypted += char

    return encrypted

def print_encrypted_message():
    """Solicita al usuario un mensaje y un desplazamiento, luego muestra el mensaje cifrado y descifrado usando el cifrado César."""

    text = input("Ingrese un mensaje: ")
    shift = int(input("Ingrese el desplazamiento: "))
    encrypted_message = cesar_cipher(text, shift)

    print(f"Mensaje cifrado: {encrypted_message}")
    print(f"Mensaje descifrado: {cesar_cipher(encrypted_message, -shift)}")

if __name__ == "__main__":
    print_encrypted_message()
