#1) Solicita ao usuario que digita seu nome

nome = str(input("Digite o seu nome: "))


#2) Solicita ao usuário que digita o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_user = float(input("Digite o seu salário: "))


#3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))


#4) Calcule o valor do bônus final

bonus_final = bonus + salario_user

print(f"O {nome} recebeu ", bonus_final )



#5) Imprima cálculo do KPI para o usuário