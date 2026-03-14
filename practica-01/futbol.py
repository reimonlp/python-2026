"""
ACTIVIDAD EXTRA - TABLA DE POSICIONES

Desarrollar un programa que simule la tabla de posiciones de un torneo de fútbol.
El programa debe tener un menú interactivo con las siguientes opciones:
- Agregar un equipo al torneo.

- Registrar un resultado ingresando equipo local, equipo visitante y marcador en formato 4 - 2.
  El programa debe actualizar los puntos automáticamente (3 puntos por victoria, 1 por empate, 0 por derrota).

- Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.

- Eliminar un equipo del torneo.

- Salir del programa.

Se deben manejar situaciones como intentar agregar un equipo ya existente, registrar un resultado con un equipo
desconocido, o ingresar un marcador con formato inválido.
"""
from operator import itemgetter

def agregar_equipo(equipos):
    # .strip().title() limpia espacios y pone en mayusculas
    equipo = input("Ingrese el nombre del equipo: ").strip().title()
    
    if not equipo:
        print("El nombre no puede estar vacío.")
    elif equipo in equipos:
        print("El equipo ya existe en el torneo.")
    else:
        equipos.append(equipo)
        print(f"Equipo '{equipo}' agregado al torneo.")

def registrar_resultado(equipos, partidos):
    local = input("Ingrese el equipo local: ").strip().title()
    visitante = input("Ingrese el equipo visitante: ").strip().title()
    
    if local == visitante:
        print("\nUn equipo no puede jugar contra sí mismo.")
        return
    elif local not in equipos or visitante not in equipos:
        print("\nUno o ambos equipos no existen en el torneo.")
        return
    elif any(local in p[:2] and visitante in p[:2] for p in partidos):
        print("\nEstos equipos ya jugaron entre sí.")
        return

    marcador = input("Ingrese el marcador (formato 'local - visitante'): ")
    try:
        # Se divide asumiendo que hay un guión, independientemente de los espacios
        goles_local, goles_visitante = [int(g.strip()) for g in marcador.split('-')]

    except ValueError:
        print("\nFormato de marcador inválido. Use 'local - visitante'.")
        return

    partidos.append((local, visitante, goles_local, goles_visitante))
    print(f"\nResultado registrado: {local} {goles_local} - {goles_visitante} {visitante}")

def mostrar_tabla(equipos, partidos):
    if not equipos:
        print("No hay equipos registrados en el torneo aún.")
        return

    tabla = {equipo: 0 for equipo in equipos}

    for local, visitante, goles_local, goles_visitante in partidos:
        if goles_local > goles_visitante:
            tabla[local] += 3
        elif goles_local < goles_visitante:
            tabla[visitante] += 3
        else:
            tabla[local] += 1
            tabla[visitante] += 1

    # sorted_tabla es una lista de tuplas (equipo, puntos)
    # key=itemgetter(1) indica que se ordena por el segundo elemento de la tupla
    # y reverse=True indica que se ordena de mayor a menor
    sorted_tabla = sorted(tabla.items(), key=itemgetter(1), reverse=True)

    print("Tabla de Posiciones:")
    for equipo, puntos in sorted_tabla:
        print(f"{equipo}: {puntos} puntos")

def eliminar_equipo(equipos, partidos):
    if not equipos:
        print("No hay equipos registrados en el torneo para eliminar.")
        return

    equipo = input("Ingrese el nombre del equipo a eliminar: ").strip().title()
    
    if equipo in equipos:
        equipos.remove(equipo)
        partidos[:] = [p for p in partidos if equipo not in p[:2]]
        print(f"Equipo '{equipo}' y sus partidos han sido eliminados.")
    else:
        print("El equipo no existe en el torneo.")

def main():
    equipos = []
    partidos = []

    while True:      
        print("\nMenú:")
        print("    1. Agregar equipo")
        print("    2. Registrar resultado")
        print("    3. Mostrar tabla de posiciones")
        print("    4. Eliminar equipo")
        print("    5. Salir")
              
        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case '1':
                agregar_equipo(equipos)
            case '2':
                registrar_resultado(equipos, partidos)
            case '3':
                mostrar_tabla(equipos, partidos)
            case '4':
                eliminar_equipo(equipos, partidos)
            case '5':
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
