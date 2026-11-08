"""
Exercício 12: Extraindo e remontando dígitos

Dado o número 847, use os operadores // e % para:

* Extrair o dígito das centenas (8), o das dezenas (4) e o das unidades (7).
* Calcular a soma dos dígitos (8 + 4 + 7 = 19).
* Construir o número invertido (748).

Seu código deve funcionar para qualquer número de 3 dígitos. Teste trocando 847 por 123 e depois por 905.
"""

numero = 847

centenas = numero // 100 # 8
dezenas = (numero // 10) % 10 # 4
unidades = numero % 10 # 7

soma_digitos = centenas + dezenas + unidades

print(f"centenas: {centenas} / dezenas: {dezenas} / unidade: {unidades}")
print(f"soma de dígitos: {centenas} + {dezenas} + {unidades} [{numero}] = {soma_digitos}")

# 8 [centenas] 4 [dezenas] 7 [unidades]
# 7 [unidades] 4 [dezenas] 8 [centenas]

valor_intermediario = unidades
unidades = centenas # unidades = 8
centenas = valor_intermediario # centenas = 7

numero_invertido = int(f"{centenas}{dezenas}{unidades}")

print(f"\nNúmero normal: {numero}")
print(f"Número invertido: {numero_invertido}")