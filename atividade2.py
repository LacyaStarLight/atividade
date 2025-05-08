nome = input("Qual seu nome?")
idade = (int(input("Qual sua idade?")))
cidade = input("Você mora em qual cidade?")
hobby = input("Qual seu hobby?")
print("Ola",nome,",", "voce tem",idade, "anos e mora em",cidade,".", "Ouvi dizer que voce adora",hobby,".", "Parabens, voce concluiu seu cadastro, boas compras.")

valor = int(input("Qual será o valor do pagamento?"))


n100 = valor // 100
valor = valor % 100

n50 = valor // 50
valor= valor % 50

n20 = valor // 20
valor = valor % 20

n10 = valor // 10
valor = valor % 10

n5 = valor // 5
valor = valor % 5

n2 = valor // 2
valor = valor % 2

print("notas de 100R$:", n100)
print("notas de 50R$:", n50)
print("notas de 20R$:", n20)
print("notas de 10R$:", n10)
print("notas de 5R$:", n5)
print("notas de 2R$:", n2)


forma_de_pagamento = (input("Qual vai ser a forma de pagamento? Pagando no débito, você ganha 10% de desconto. Mas, se for no crédito, tem um juros de 5%"))
print("Ok, sua forma de pagamento foi,", forma_de_pagamento)

debito = 0.90
valor_final = valor

print("Sua compra foi completa com sucesso o valor final é ", valor_final)

troco = valor - valor_final
print("Por fim, seu troco é", troco)