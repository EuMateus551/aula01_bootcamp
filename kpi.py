nome = input("Por favor, informe seu nome: ")
salario = float(input("Por favo, informe o seu salário: "))
bonus_recebido = float(input("Por favor, informe o seu bônus: "))
valor_bonus = 1000 + salario * bonus_recebido

print(f"Olá {nome}, o seu bônus foi de R${valor_bonus:.2f}")