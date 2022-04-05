def calculo_imc(alt = 0, pes = 0, gen = '', idade = 0):
    """
    :param alt: Entrada da altura da pessoa
    :param pes: Entrada do peso da pessoa
    :param gen: Genero da Pessoa
    :param idade: Idade da pessoa
    :return: Retorna o resultado do calculo do IMC
    """
    if alt.isnumeric() and pes.isnumeric() and gen != '' and idade.isnumeric():

        imc = float(pes) / (float(alt) / 100) ** 2

        if(int(idade) >= 18):
            if(gen.strip().upper()[0] == "M"):
                if (imc < 20.7):
                    return("Abaixo do peso")
                if (imc >= 20.7 and imc < 26.4):
                    return("Peso ideal")
                if (imc >= 26.5 and imc < 27.8):
                    return("Pouco acima do peso")
                if (imc >= 27.9 and imc < 31.1):
                    return("Acima do peso")
                if (imc >= 31.2):
                    return"Obesidade"

            if(gen.strip().upper()[0] == "F"):
                if (imc < 19.1):
                    return("Abaixo do peso")
                if (imc >= 19.1 and imc < 25.8): 
                    return("Peso ideal")
                if (imc >= 25.9 and imc < 27.3):
                    return("Pouco acima do peso")
                if (imc >= 27.4 and imc < 32.3):
                    return("Acima do peso")
                if (imc >= 32.4):
                    return('Obesidade')
            else:
                return("Ainda não temos informações para pessoas com menos de 18 anos")
        else:
            return("Algum parametro foi digitado incorretamente, não foi possivel definir sua Situação corretamente")
    else:
        return("Parametros Incorretos!")

