import json

with open('./configs/table_points.json', 'r', encoding='utf-8') as f:
    TABLE_POINTS = json.load(f)

COLOR_NONE = '\033[m'
COLOR_RED = '\033[1;31m'
COLOR_GREEN = '\033[32m'


def exibir_menu(name_dbv: str, list_used_options: set) -> int:
    """
    Exibe menu com todos os itens da tabela de pontos e
    retorna indice da lista da TABELA DE PONTOS (TABLE_POINTS)

    Args:
         name_dbv: nome do desbravador
         total_points: total de pontos
         list_used_options: lista com indices de opcoes que já foram usadas

    Returns:
        int: retorna o numero da opcao escolhida ou -1 para opcao invalida
    """
    print(f'Nome: {COLOR_RED}{name_dbv.upper()}\033[m')
    max_option = len(TABLE_POINTS) - 1

    for i in range(len(TABLE_POINTS)):
        if i in list_used_options:
            color = COLOR_GREEN
        else:
            color = COLOR_NONE

        print(f'{color}{i}) {TABLE_POINTS[i]["description"]}{COLOR_NONE}')

    option = input('Insira a opção: ').strip()
    if option.isnumeric() and int(option) <= max_option:
        return int(option)
    return -1



