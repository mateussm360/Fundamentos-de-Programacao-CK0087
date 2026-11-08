"""
Exercício 9: prevendo o valor de variáveis encadeadas

Antes de executar, tente prever o valor de cada variável do código abaixo. Depois execute a célula e confira se suas previsões estavam certas.
"""

a = 5
print(f"a: {a}") # a = 5

b = a * 2
print(f"b: {a} * {2}, b: {b}") # b = 5 * 2 = 10, b = 10

c = b + a
print(f"c: {b} + {a}, c: {c}") # 10 + 5 = 15, c = 15

d = c // 4
print(f"d: {c} // {4}, d: {d}") # 15 // 4 = 3, d = 3

e = c % 4
print(f"e: {c} % {4}, e: {e}") # 15 % 4 => 15 = 4 * 3 + r => r = 15 - 12 => 3