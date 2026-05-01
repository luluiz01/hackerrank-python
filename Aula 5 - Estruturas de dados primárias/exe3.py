"""3. Use conjuntos para encontrar elementos únicos em duas listas diferentes"""

lista_1 = [1, 2, 3]
lista_2 = [3, 4, 5]

intesecao = []

for i in lista_1:
    if i in lista_2:
        intesecao.append(i)
print(intesecao)

uniao = []
