quantidade_pessoas = 356
pessoas_por_grupo = 18

quantidade_grupos_completos = quantidade_pessoas // pessoas_por_grupo
quantidade_pessoas_sem_grupo = quantidade_pessoas % pessoas_por_grupo

# 356 - 342 => 14 (resto) | 356 = 18 * 19 + r => r = 356 - 18 * 19
# r = 356 - 342 = 14

print(f"Quantidade de pessoas: {quantidade_pessoas}")
print(f"Quantidade de pessoas por grupo: {pessoas_por_grupo}")

print(f"\nGrupos completos (quantidade): {quantidade_grupos_completos}")
print(f"Quantidade de pessoas sem grupo: {quantidade_pessoas_sem_grupo}")