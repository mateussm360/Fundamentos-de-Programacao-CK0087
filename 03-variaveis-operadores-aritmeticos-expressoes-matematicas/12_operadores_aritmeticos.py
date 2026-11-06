numero1 = 10
numero2 = 5

soma = numero1 + numero2
print(f"{numero1} + {numero2} = {soma}")

subtracao = numero1 - numero2
print(f"{numero1} - {numero2} = {numero1 - numero2}")

multiplicacao = numero1 * numero2
print(f"{numero1} * {numero2} = {multiplicacao}")

divisao = numero1 / numero2
print(f"{numero1} / {numero2} = {divisao}")

divisao_inteira = numero1 // (numero2 + 2)
print(f"{numero1} // {numero2 + 2} = {divisao_inteira}")

resto = numero1 % numero2
print(f"{numero1} % {numero2} = {resto}")

potenciacao = numero1 ** numero2
print(f"{numero1} ** {numero2} = {potenciacao}")

print("\nUnitarios:")

operacao_unitario_positivo = -numero2 + numero1
print(f"{-numero2} + {numero1} = {operacao_unitario_positivo}")

operacao_unitario_negativo = -numero1 + numero2
print(f"{-numero1} + {numero2} = {-numero1 + numero2}")

print(f"{-5} - ({-5}) = {-5--5}")