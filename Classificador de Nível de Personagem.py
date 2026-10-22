# Autor: Michael Douglas
# Data: 22/10/2026
# Linguagem: Python

nome = "Baiano"

# ETAPA 1: Receber e validar a quantidade de XP.

while True:
    try:
        xp = int(input("Digite a quantidade de XP do herói: "))
        if xp < 0:
            print("XP inválido. O valor deve ser maior ou igual a 0.")
            continue
        break
    except ValueError:
        print("XP inválido. Por favor, digite um número inteiro.")  

# ETAPA 2: Classificar o herói conforme sua faixa de XP.

if xp <= 1000:
        nivel = "Ferro"
elif xp <= 2000:
        nivel = "Bronze"
elif xp <= 5000:
        nivel = "Prata"
elif xp <= 7000:
        nivel = "Ouro"
elif xp <= 8000:
        nivel = "Platina"
elif xp <= 9000:
        nivel = "Ascendente"
elif xp <= 10000:
        nivel = "Imortal"
else:
        nivel = "Radiante"

# ETAPA 3: Exibir o resultado da classificação.

print(f"O Herói {nome} está no nível {nivel}.")