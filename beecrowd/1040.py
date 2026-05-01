n1, n2, n3, n4 = map(float, input("").split(" "))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:    
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input(""))
    print(f"Nota do exame: {exame:.1f}")
    nova_media = (exame + media) / 2
    if nova_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media:.1f}")
