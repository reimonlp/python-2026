# Práctica 02 - Python

Este proyecto contiene ejercicios prácticos de Python con soporte para Jupyter Notebooks.

## Requisitos previos

- Python 3.14.3 o superior
- pip (administrador de paquetes de Python)
- Virtual environment (venv)

## Instalación

### 1. Crear el entorno virtual

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

**En Linux/macOS:**
```bash
source .venv/bin/activate
```

**En Windows:**
```bash
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```
practica-02/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias del proyecto
├── notebooks/                   # Jupyter Notebooks con ejercicios
│   ├── ejercicio_01.ipynb
│   ├── ejercicio_02.ipynb
│   ├── ejercicio_03.ipynb
│   ├── ejercicio_04.ipynb
│   ├── ejercicio_05.ipynb
│   ├── ejercicio_06.ipynb
│   ├── ejercicio_07.ipynb
│   ├── ejercicio_08.ipynb
│   ├── ejercicio_09.ipynb
│   └── ejercicio_10.ipynb
└── src/                         # Archivos Python ejecutables
    ├── ejercicio_01.py
    ├── ejercicio_02.py
    ├── ejercicio_03.py
    ├── ejercicio_04.py
    ├── ejercicio_05.py
    ├── ejercicio_06.py
    ├── ejercicio_07.py
    ├── ejercicio_08.py
    ├── ejercicio_09.py
    └── ejercicio_10.py
```

## Ejecución

### Ejecutar scripts Python

Para ejecutar un ejercicio específico:

```bash
python src/ejercicio_01.py
python src/ejercicio_02.py
# ... etc
```

### Ejecutar Jupyter Notebooks

Para iniciar Jupyter Lab:

```bash
jupyter lab
```

Para iniciar Jupyter Notebook:

```bash
jupyter notebook
```

Luego navega a la carpeta `notebooks/` y abre el notebook que desees trabajar.