"""3️⃣ Maior e menor

(versão treino do que você já fez)

👉 retorna maior e menor número"""

numeros = [1, 2, 3, 4, 5]
maior = numeros[0]
menor = numeros[0]

for i in numeros:
    if i > maior:
        maior = i

    print(f"o maior numero é: {maior}")
