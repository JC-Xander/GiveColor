from enum import Enum

class Color(Enum):
    """Lista de colores con sus respectivas secuencias de escape ANSI"""
    DEFAULT = '\033[0m'  # Resetear al color original
    BLACK  = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

# Guardar la referencia original de la función print
original_print = print

# Crear una nueva función que envuelve a print con soporte de color
def print(*values: object, color: Color = Color.DEFAULT, sep: str = ' ', end: str = '\n', **kwargs) -> None:
    original_print(color.value, end='')
    original_print(*values, sep=sep, end=end, **kwargs)
    original_print(Color.DEFAULT.value, end='')