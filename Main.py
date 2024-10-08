from givecolor import Fore, Back, Style

print('Color rojo', fore=31)
print('41 es invalido', fore=41)
print('42 no es invalido', fore='42')
print('Color verde', fore=Fore.GREEN)
print('Color amarillo', fore='33')
print('Color azul', fore='blue')
print('sex no fuciona', fore='sex')
print('-' * 30)
print('No funciona con 31', back=31)
print('Fondo rojo', back=41)
print('Fondo verde', back='42')
print('Fondo azul', back=Back.BLUE)
print('No funciona con la cadena "33"', back='33')
print('fondo blanco', back='white')
print('sex no fuciona', back='sex')
print('-' * 30)
print('No funciona con 31', back=31)
print('Fondo rojo', back=41)
print('Fondo verde', back='42')
print('Fondo azul', back=Back.BLUE)
print('No funciona con la cadena "33"', back='33')
print('fondo blanco -> Texto Rojo', back='white', fore=Fore.RED, style=Style.CROSSED)
print('sex no fuciona', back='sex')
print('-' * 30)
print('Texto en blanco y tachado con fondo azul',
        fore=Fore.GREEN,
        back=Back.BLUE,
        style=Style.CROSSED)

