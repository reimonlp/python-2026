
# Consigna: Juegos como Módulos

## Objetivo
Crear un menú principal que permita seleccionar y ejecutar uno de 3 juegos disponibles.

## Requisitos

### 1. Menú Principal
- Mostrar opciones para seleccionar entre los 3 juegos
- Importar cada juego como módulo
- Llamar al método que ejecuta el juego seleccionado
- Retornar al menú al finalizar la ejecución

### 2. Modificación de los Juegos
Cada juego debe ser **compatible con módulos**, cumpliendo:
- Tener una función principal ejecutable (ej: `jugar()`)
- Permitir ser **importado como módulo** sin ejecutarse automáticamente
- Permitir ser **ejecutado directamente** manteniendo la funcionalidad original

### 3. Estructura de Código
```python
if __name__ == "__main__":
    # Código que se ejecuta solo si se corre directamente
    funcion_principal()
```

## Resultado Esperado
- Menú interactivo funcional
- Todos los juegos ejecutables de dos formas:
  1. Desde el menú principal
  2. Directamente como script independiente
