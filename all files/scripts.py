def calculo_imc(alt = 0, pes = 0):
    """
    :param alt: Entrada da altura da pessoa
    :param pes: Entrada do peso da pessoa
    :return: Retorna o resultado do calculo do IMC
    """
    if alt.isnumeric() and pes.isnumeric():
        imc = float(pes) / (float(alt) / 100) ** 2
        return (imc)
    else:
        return("Parametros Incorretos!")
    
def result_imc(gen = '', resIMC = 0, idade = 0):
    """
    :param gen: Genero da Pessoa
    :param resIMC: Resultado do calculo IMC
    :param idade: Idade da pessoa
    :return: Retorna a situação da pessoa"""
    if gen != '' and idade.isnumeric():
        if(int(idade) >= 18):
            if(gen.strip().upper()[0] == "M"):
                if (resIMC < 20.7):
                    return("Abaixo do peso")
                if (resIMC >= 20.7 and resIMC < 26.4):
                    return("Peso ideal")
                if (resIMC >= 26.5 and resIMC < 27.8):
                    return("Pouco acima do peso")
                if (resIMC >= 27.9 and resIMC < 31.1):
                    return("Acima do peso")
                if (resIMC >= 31.2):
                    return"Obesidade"
            if(gen.strip().upper()[0] == "F"):
                if (resIMC < 19.1):
                    return("Abaixo do peso")
                if (resIMC >= 19.1 and resIMC < 25.8): 
                    return("Peso ideal")
                if (resIMC >= 25.9 and resIMC < 27.3):
                    return("Pouco acima do peso")
                if (resIMC >= 27.4 and resIMC < 32.3):
                    return("Acima do peso")
                if (resIMC >= 32.4):
                    return('Obesidade')
        else:
            return("Ainda não temos informações para pessoas com menos de 18 anos")
    else:
        return("Algum parametro foi digitado incorretamente, não foi possivel definir sua Situação corretamente")
