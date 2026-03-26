tarifas = {
    "local": (500, 1000, 2000),
    "regional": (1000, 2500, 5000),
    "nacional": (2000, 4500, 8000),
}

def _input_weight_and_zone():
    """Solicita al usuario que ingrese el peso del paquete y la zona de destino."""

    peso = float(input("Ingrese el peso del paquete (kg): "))
    zona = input("Ingrese la zona de destino (local/regional/nacional): ").strip().lower()

    return peso, zona

def _calculate_shipping_cost(peso, zona, tarifas):
    """Calcula el costo de envío de un paquete según su peso y la zona de destino."""

    if zona not in tarifas:
        return "Zona no válida. Las zonas disponibles son: local, regional, nacional."

    if peso <= 1:
        costo = tarifas[zona][0]
    elif peso <= 5:
        costo = tarifas[zona][1]
    else:
        costo = tarifas[zona][2]

    return f"Costo de envío: ${costo}"

def print_shipping_cost(tarifas):
    """Calcula el costo de envío de un paquete según su peso y la zona de destino."""

    peso, zona = _input_weight_and_zone()
    print(_calculate_shipping_cost(peso, zona, tarifas))

if __name__ == "__main__":
    print_shipping_cost(tarifas)