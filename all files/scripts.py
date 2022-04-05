def calculo_imc():
    """
    :return: Retorna o resultado do calculo do IMC
    """
    from PySimpleGUI import PySimpleGUI as sg
    
    sg.theme('DarkPurple1')

    layout = [
        [sg.Text('Nome: '), sg.Input(key = '_nome', size = (20, 1))],
        [sg.Text('Altura (cm): '), sg.Input(key = '_altura', size = (20, 1))],
        [sg.Text('Peso (Kg): '), sg.Input(key = '_peso', size = (20, 1))],
        [sg.Text('Sexo: '), sg.OptionMenu(values=['Masculino', 'Feminino'], size = (8, 1), default_value = '', key = '_sexo')],
        [sg.Button('Entrar')]
    ]

    #Janela
    janela = sg.Window('Tela de cadastro', layout)
    #Ler eventos

    while True:
        eventos, valores = janela.read()

        nome = valores['_nome']
        alt = str(valores['_altura'])
        pes =  str(valores['_peso'])
        gen = str(valores['_sexo']).upper()

        break
#############################################################################################################
    if alt.isnumeric() and pes.isnumeric() and gen != '':

        imc = float(pes) / (float(alt) / 100) ** 2

        if(gen.strip().upper()[0] == "M"):
            if (imc < 20.7):
                situacao = ("Abaixo do peso")
            if (imc >= 20.7 and imc < 26.4):
                situacao = ("Peso ideal")
            if (imc >= 26.5 and imc < 27.8):
                situacao = ("Pouco acima do peso")
            if (imc >= 27.9 and imc < 31.1):
                situacao = ("Acima do peso")
            if (imc >= 31.2):
                situacao = "Obesidade"
        elif(gen.strip().upper()[0] == "F"):
            if (imc < 19.1):
                situacao = ("Abaixo do peso")
            if (imc >= 19.1 and imc < 25.8): 
                situacao = ("Peso ideal")
            if (imc >= 25.9 and imc < 27.3):
                situacao = ("Pouco acima do peso")
            if (imc >= 27.4 and imc < 32.3):
                situacao = ("Acima do peso")
            if (imc >= 32.4):
                situacao = ('Obesidade')
        else:
            situacao = ("Algum parametro foi digitado incorretamente, não foi possivel definir sua Situação corretamente")
    else:
        situacao = ("Parametros Incorretos!")
    return imc, situacao, nome

def resultados():
    imc, situacao, nome = calculo_imc()
    print("-=-" * 20)
    print(f'Olá {nome}, Bem Vindo(a)!')
    print(f'Seu IMC atual é: {imc:.5f}')
    print(f'Sua situação é: {situacao}')
    print("-=-" * 20)
