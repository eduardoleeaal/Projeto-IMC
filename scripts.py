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