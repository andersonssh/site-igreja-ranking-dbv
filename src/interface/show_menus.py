from . import COLOR_NONE, COLOR_RED, COLOR_GREEN, TABLE_POINTS, Members
from src.utils import is_user_updated_today


def show_points_and_description(data: list):
    """EXIBE LISTA DE SCORE_DETAILS"""

    for item in data:
        print(f'Pontos: {item["points"]} | Description: {item["description"]}')


def show_points_menu(name_dbv: str, list_used_options: set) -> int:
    """
    Exibe menu com todos os itens da tabela de pontos e
    retorna indice da lista da TABELA DE PONTOS (TABLE_POINTS)

    Args:
         name_dbv: nome do desbravador
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


def show_users_menu() -> int:
    """
    Exibe menu com todos os usuarios (RECEBIDOS DA API)

    Returns:
        int: retorna o numero da opcao escolhida ou -1 para opcao invalida
    """
    max_option = len(Members.MEMBERS) - 1
    for i in range(len(Members.MEMBERS)):
        if is_user_updated_today(Members.MEMBERS[i]):
            color = COLOR_GREEN
        else:
            color = COLOR_NONE

        print(f'{color}{i}) {Members.MEMBERS[i]["name"]}{COLOR_NONE}')

    option = input('Insira a opção: ').strip()
    if option.isnumeric() and int(option) <= max_option:
        return int(option)
    return -1
