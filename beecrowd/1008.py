numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")
print("=" * 50)
print("NUMBER = {}\nSALARY = U$ {:.2f}".format(numero_funcionario, salario))
