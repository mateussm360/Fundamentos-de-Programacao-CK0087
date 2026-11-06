nome_usuario1 = "mateus"
nome_usuario2 = "lucas"
nome_usuario3 = "andré"

print(f"nome_usuario1: {nome_usuario1}")
print(f"nome_usuario2: {nome_usuario2}")
print(f"nome_usuario3: {nome_usuario3}\n")

nome_usuario4 = "fernanda"
nome_usuario5 = "paula"
nome_usuario6 = "rafaela"

print("="*25)
print(f"nome_usuario4: {nome_usuario4}")
print(f"nome_usuario5: {nome_usuario5}")
print(f"nome_usuario6: {nome_usuario6}")
print("="*25)

# nome_usuario1 [mateus] = nome_usuario6 [rafaela] => nome_usuario1: "rafaela"
# nome_usuario2 [lucas] = nome_usuario4 [fernanda] => nome_usuario2: "fernanda"
# nome_usuario3 [andré] = nome_usuario5 [paula] => nome_usuario3: "paula"

nome_usuario1 = nome_usuario6
nome_usuario2 = nome_usuario4
nome_usuario3 = nome_usuario5

print(f"\nnome_usuario1: {nome_usuario1}")
print(f"nome_usuario2: {nome_usuario2}")
print(f"nome_usuario3: {nome_usuario3}")