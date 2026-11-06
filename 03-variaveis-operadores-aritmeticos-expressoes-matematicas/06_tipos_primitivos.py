nome_usuario = "mateus"
idade_usuario = 25
altura_usuario = 1.75
status_usuario = True

print(f"nome_usuario: {nome_usuario} => {type(nome_usuario)}")
print(f"idade_usuario: {idade_usuario} => {type(idade_usuario)}")
print(f"altura_usuario: {altura_usuario} => {type(altura_usuario)}")
print(f"status_usuario: {status_usuario} => {type(status_usuario)}")

print("\nImportante:")
numero = 45
numero_string = "45"

print(f"numero: {numero}, {type(numero)} => numero_string: {numero_string}, {type(numero_string)}")

booleano = True
booleano_string = "True"
print(f"booleano: {booleano}, {type(booleano)} => booleano_string: {booleano_string}, {type(booleano_string)}")

print("\nComparação:")
print(f"{numero} == '{numero_string}' = {numero == numero_string}")
print(f"{booleano} == '{booleano_string}' = {booleano == booleano_string}")
print(f"\n{numero} != '{numero_string}' = {numero != numero_string}")
print(f"{booleano} != '{booleano_string}' = {booleano != booleano_string}")