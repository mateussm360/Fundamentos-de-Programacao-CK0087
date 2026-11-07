"""
Exercício 4: x = y versus x = 'y'

Antes de executar, tente prever: o que o código abaixo vai mostrar?
Qual é a diferença entre x = y e x = 'y'?

Execute a célula abaixo e confira se sua previsão estava certa.
"""

y = 13

x = y
print(f"x: {x}, tipo: {type(x)}") # type => int

x = 'y'
print(f"x: '{x}', tipo: {type(x)}") # type => str

# A diferença: string (str) != inteiro (int)

x = '3'
print(f"x: '{x}', tipo: {type(x)}") # type => str

x = int('3')
print(f"x: {x}, tipo: {type(x)}") # type => int