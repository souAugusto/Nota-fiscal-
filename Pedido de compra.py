print("BEM VINDO A FARMÁCIA ASSOCIADA")
farmacia={"shampoo":45,"escova de dentes":10,"condicionador":30}
print("Faça seu cadastro para a compra. ")
nome=input("Informe seu nome completo: ")
cpf=input("informe seu cpf: ")
nome_produto=input("Nome do produto: ")
quant_produto=float(input("Quantos? "))
if nome_produto in farmacia:
    print("Nome: "+nome)
    print("-------------------")
    print("Cpf: "+cpf)
    print("-------------------")
    print(f"Seu produto '{nome_produto}' custa {farmacia[nome_produto]:.2f}.")
else:
    print(f"Seu pedido está em falta.")
valortotal=quant_produto * farmacia[nome_produto]
print("------ Valor total : ",valortotal,"reais.")


