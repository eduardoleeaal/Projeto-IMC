import scripts



altura = str(input("Digite sua altura em CM: "))
peso = str(input("Digite seu peso: "))
sexo = str(input("Digite seu genêro: "))
idade = int(input("Digite sua idade: "))

imc = scripts.calculo_imc(altura, peso)
print(f'IMC: {imc:.5f}')
situação = scripts.result_imc(sexo, imc, idade)
print(f'{situação}')