import scripts



altura = str(input("Digite sua altura em CM: "))
peso = str(input("Digite seu peso: "))

print(f'IMC: {scripts.calculo_imc(altura, peso):.5f}')