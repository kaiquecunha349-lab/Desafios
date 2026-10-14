# Um professor quer sortear um dos seus quatro alunos para ajudar o Rian.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
### importando a biblioteca random
from random import choice
nomes = ["Miguel", "Kaio", "Leonardo", "Gustavo A"]


# Um professor quer sortear um dos seus quatro alunos para ajudar o Rian.
# Faça um programa que leia os nomes deles e escreva o nome do escolhido.

import random

nomes = ["Miguel", "Kaio", "Leonardo", "Gustavo A"]

escolhido = random.choice(nomes)

print("O aluno escolhido foi:", escolhido)

