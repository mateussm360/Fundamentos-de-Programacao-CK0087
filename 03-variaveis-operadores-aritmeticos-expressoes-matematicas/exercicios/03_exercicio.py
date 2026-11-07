"""
Exercício 3: Média de Notas

Um aluno realizou duas provas.

* A primeira nota foi 7.5 (guarde na variável nota_prova_um).
* A segunda nota foi 8.5 (guarde na variável nota_prova_dois).

Crie uma terceira variável chamada media_aluno que calcule a média aritmética
simples dessas duas notas. Exiba o resultado final usando o comando
print(media_aluno).
"""

nota_prova_um = 7.5
nota_prova_dois = 8.5
media_aluno = (nota_prova_um + nota_prova_dois) / 2

print(f"nota_prova_um: {nota_prova_um}, {type(nota_prova_um)}")
print(f"nota_prova_dois: {nota_prova_dois}, {type(nota_prova_dois)}")
print(f"media_aluno: {media_aluno}, {type(media_aluno)}")