#-*- coding: utf-8 -*-

"""
Calculadora
Autor: Roger
Função: Realizar cálculo do Indice de Massa Corporal (IMC)
"""

print ("---CÁLCULO IMC---")

peso = input("Digite seu peso:")
peso = float(peso)

altura = input("Digite sua altura:")
altura = float(altura)

imc = peso // (altura * altura)
imc = float(imc)
print ("O seu IMC é de :", imc)