nome_produto = "Teclado Gamer"
preco_produto = 456.90
quantidade_produto = 53

print(f"Nome do produto: {nome_produto}")
print(f"Preço do produto: R$ {preco_produto}")
print(f"Quantidade: {quantidade_produto}")

desconto = 0.2
preco_descontado = preco_produto * desconto

print(f"\nexemplo: R$ {456.90} - R$ {0.2 * 456.90} = R$ {456.90 - 0.2 * 456.90}")
preco_produto -= preco_descontado

print(f"Preço do produto (atualizado/desconto): R$ {preco_produto}")

print(f"\nexemplo: R$ {preco_produto} - R$ {round(0.115 * preco_produto)} = R$ {round(preco_produto - 0.115 * preco_produto, 2)}")

frete_produto = round(0.115 * preco_produto, 2)
preco_produto -= frete_produto
print(f"Preço do produto (atualizado/frete): R$ {preco_produto}")

print(f"\nexemplo: R$ {preco_produto} - R$ {round(0.23 * preco_produto, 2)} = R$ {preco_produto - round(0.23 * preco_produto, 2)}")
cupom_desconto = round(0.23 * preco_produto, 2)
preco_produto -= cupom_desconto
print(f"Preço do produto (atualizado/cupom): R$ {preco_produto}")