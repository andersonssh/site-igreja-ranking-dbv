from datetime import datetime


def is_user_updated_today(user_data: dict) -> bool:
    """
    Verifica se o usuario já sofreu alguma atualizacao no dia atual

    Args:
        user_data: dados do usuario providos da api

    Return:
        bool: True para atualizado e False para nao atualizado
    """
    updated_at = user_data.get('updated_at')
    if not updated_at:
        return False

    # ex: 2022-04-16 00:39:52
    updated_at = updated_at.split()[0]
    current_date = datetime.today().isoformat(' ', 'seconds').split()[0]

    return updated_at == current_date
