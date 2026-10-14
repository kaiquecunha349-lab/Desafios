# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
salario = float(input('digite seu salario atual: '))
novo_salario = salario * 1.15
print(f'O seu salario atual é {salario:.2f}, com aumento de 15% seu novo salario é {novo_salario:.2f}')