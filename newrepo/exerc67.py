#A função notas cria um dicionario, apartir dos parametros adicionados quando chamada a função.
def notas(*n, sit=False):
    """
    > Função para analisar notas e situação de varios alunos
    :param n: uma ou mais nota dos alunos, aceita varias
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação da turma.
    :return: dicionario com varias informações sobre a situação da turma.
    """
    
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit: #se o parametro "sit" (SITUAÇÃO) for chamado como True, exibe a situação dos alunos no print.
        if r['media'] >= 7:
            r['situação'] = 'Ótima'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    
    return r
resp = notas(5, 8, 9, 3.5, 5, 4, 10, sit=True)
print(resp)
help(notas)