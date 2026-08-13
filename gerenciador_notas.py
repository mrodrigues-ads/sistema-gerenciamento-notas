# Lista de dicionários utilizada para armazenar os estudantes.
# Cada dicionário contém o nome do aluno e uma lista com suas notas.
estudantes = [
    {
        "nome": "Carlos",
        "notas": [8.5, 1.0, 3.0]
    },
    {
        "nome": "Ana",
        "notas": [6.5, 7.5, 8.0]
    },
    {
        "nome": "João",
        "notas": []
    }
]

def calcular_media(notas):
    """
    Calcula a média das notas de um estudante.
    Args:
        notas (list): Lista contendo notas do tipo float.
    Returns:
        float: Média calculada das notas.
    """
    # Trata o caso de uma lista vazia para evitar divisão por zero.
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica a situação do estudante com base na média final.
    Args:
        media (float): Média final do estudante.
        media_minima (float): Média mínima para aprovação.
    Returns:
        str: 'Aprovado' ou 'Reprovado'
    """
    if media >= media_minima:
        return "Aprovado"
    
    return "Reprovado"

def gerar_relatorio(alunos):
    """
    Gera um relatório com a média e a situação dos estudantes.
    Args:
        alunos (list): Lista contendo os dados dos estudantes.
    Returns:
        None
    """
    # Percorre cada estudante da lista.
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = verificar_aprovacao(media)
        print(f"ESTUDANTE: {aluno['nome']} | MÉDIA: {media:.1f} | SITUAÇÃO: {situacao}")

# Executa a função no final do programa.
gerar_relatorio(estudantes)
