# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
numero = float(input('digite o numero : '))
sucessor = numero + 1
antecessor = numero - 1
print(f'O seu numero que vc escolhe foi {numero:.2f}, o sucessor dele e {antecessor:.2f}')