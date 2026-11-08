"""
Exercício 10: operadores aritméticos

Siga as instruções da célula de código para responder às perguntas.
"""

def exibirTitulo(titulo):
    print("="*50)
    print(titulo)

"""
Item A: Uma pesquisa de campo tem 100 questionários para serem separados em pilhas de 11.
Quantas pilhas completas serão formadas? Quantos questionários sobram?
"""

total_questionarios = 100
total_pilhas = 11

# 100 // 11 => 11 * 9 => 99, pilhas_completas: 9
pilhas_completas = total_questionarios // total_pilhas

# 100 % 11 => 100 = 11 * 9 + r => r = 100 - 99, r = 1, pilhas_sobra: 1
pilhas_sobra = total_questionarios % total_pilhas

exibirTitulo("Item A)")
print(f"total_questionarios: {total_questionarios} / total_pilhas: {total_pilhas}")
print(f"pilhas_completas: {pilhas_completas}")
print(f"pilhas_sobra: {pilhas_sobra}")

"""
Item B: Uma prova tem 60 questões e uma pessoa precisa acertar 70% delas para ser aprovada.
Quantas questões ela precisa acertar?
"""

total_questoes_prova = 60
percentual_aprovacao = int(total_questoes_prova * 0.7)
percentual_minima_erro = int(total_questoes_prova * 0.3)

exibirTitulo("Item B)")
print(f"total_questoes_prova: {total_questoes_prova}")
print(f"total de questões (aprovação): {percentual_aprovacao}")
print(f"total de questões erradas (mínima): {percentual_minima_erro}")
print(f"=> {percentual_aprovacao} (acertos) + {percentual_minima_erro} (erros) = {total_questoes_prova}")

"""
Item C: A nota final de uma disciplina é calculada pela média aritmética de 3 notas.
Calcule a nota final de uma pessoa que tirou notas 7.5, 9 e 6, respectivamente.
"""

nota1, nota2, nota3 = 7.5, 9, 6
media = (nota1 + nota2 + nota3) / 3

exibirTitulo("Item C)")
print(f"nota1: {nota1}, nota2: {nota2}, nota3: {nota3}")
print(f"media: Q({nota1} + {nota2} + {nota3}) / {3} = {media}")

"""
Item D: Uma população de 100 indivíduos dobra de tamanho a cada ano.
Qual será o tamanho da população após 3 anos? E após 10 anos?
"""

exibirTitulo("Item D)")

total_populacao = 100
print(f"Quantidade inicial da população: {total_populacao}")

# Após 3 anos
quantidade_anos = 3
valor_transformador = 2
total_populacao *= valor_transformador ** quantidade_anos
print(f"Quantidade da população (após {quantidade_anos} anos): {total_populacao}")

# Após 10 anos (3 + 7)
quantidade_anos += 7
total_populacao = 100
total_populacao *= valor_transformador ** quantidade_anos
print(f"Quantidade da população (após {quantidade_anos} anos): {total_populacao}")

"""
Item E: O número 10 é par e o número 7 é ímpar.
Calcule o resto da divisão de cada um por 2.
"""

numero_par = 10
numero_impar = 7
numero_referencia = 2

numero_par_resto_por_referencia = numero_par % numero_referencia
numero_impar_resto_por_referencia = numero_impar % numero_referencia

exibirTitulo("Item E)")

# 10 % 2 => 10 = 2 * 5 + r => r = 10 - 10, r = 0
print(f"{numero_par} % {numero_referencia} = {numero_par_resto_por_referencia}")

# 7 % 2 => 7 = 2 * 3 + r => r = 7 - 6 => r = 1
print(f"{numero_impar} % {numero_referencia} = {numero_impar_resto_por_referencia}")

"""
Item F: O IMC (Índice de Massa Corporal) é calculado dividindo a massa em kg pela altura ao quadrado em metros.
Calcule o IMC de uma pessoa com 70 kg e 1m e 70cm de altura.
"""

peso = 78.85
altura = 1.74
imc = peso / altura ** 2

exibirTitulo("Item F)")
print(f"Peso: {peso}kg / Altura: {altura}cm")
print(f"Imc: {imc}")

"""
Item G: Um produto custa R$ 80,00 e está com 25% de desconto.
Qual o valor do desconto? Qual o preço final?
"""

preco_produto = 80.00
desconto = 0.25
valor_preco_desconto = preco_produto * desconto
preco_produto -= valor_preco_desconto

exibirTitulo("Item G)")
print(f"Preço do produto: R$ {preco_produto + valor_preco_desconto}")
print(f"Qual o valor do desconto? R$ {valor_preco_desconto}")
print(f"Qual o preço final? R$ {preco_produto}")

"""
Item H: Um ônibus percorreu 90 km em 1,5 h.
Qual a velocidade média em km/h? E em m/s?
"""

distancia = 90
tempo = 1.5

exibirTitulo("Item H)")
velocidade_media = distancia / tempo
print(f"Velocidade média: {distancia}km / {tempo}h => {velocidade_media} km/h")

velocidade_media /= 3.6
print(f"Velocidade média: {distancia * 10 ** 3} / {tempo / 60} => {velocidade_media:.2f}m/s")
print(f"Verificação: {distancia * 10 ** 3} / {tempo * 3600} = {(distancia * 10 ** 3) / (tempo * 3600):.2f}")

"""
Item I: Quantos segundos tem 1 ano? Considere 1 ano = 365 dias.
"""

dias, horas, minutos, segundos = 365, 24, 60, 60
segundos_em_um_ano = dias * horas * minutos * segundos

exibirTitulo("Item I)")
print(f"dias: {dias}, horas: {horas}, minutos: {minutos}, segundos: {segundos}")
print(F"quantidade de segundos em um ano: {segundos_em_um_ano}")