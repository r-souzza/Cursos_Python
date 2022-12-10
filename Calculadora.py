#-*- coding: utf-8 -*-

"""
Calculadora
Autor: Roger
Função: Realizar cálculos
"""

print ("---CALCULADORA---")

sair = False

while sair == False:

	valor1 = input("Digite o primeiro valor:")
	valor1 = int(valor1)
	#Linha acima define o valor1 como int, para que o mesm possa ser calculado
	operador = input("Digite o operador (+ - / *):")
	valor2 = input("Digite o segundo valor:")
	valor2 = int(valor2)

	if operador == "+":
		operacao = valor1 + valor2

	if operador == "-":
		operacao = valor1 - valor2

	if operador == "/":
		operacao = valor1 / valor2

	if operador == "*":
		operacao = valor1 * valor2

	print ("O resultado da operação foi:")
	print (operacao)

	teste = input("Deseja sair? (s/n)")
	if teste == "s":
		sair = True