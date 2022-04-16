"""
TODAS AS FUNCOES DESTE ARQUIVO RETORNAM UMA LISTA DE
DICIONARIOS FORMATADOS DE ACORDO COM O SCHEMA DA API
[{"points": INT, "description": STRING},...]
"""
from . import TABLE_POINTS


def _insert_point_and_description(points: int, description: str) -> dict:
    """RETORNA 1 ITEM DO CAMPO score_details"""
    return {'points': points, 'description': description}


def special_personalizado():
    """TRATAMENTO PARA PONTOS PERSONALIZADOS"""
    print('* MODO PERSONALIZADO! (Points: "stop" para parar)\n')
    data = []
    while True:
        points = input('Pontos: ').strip()

        if points.lower() == 'stop':
            break
        if not points.isnumeric():
            continue
        points = int(points)

        description = input('Descrição: ')
        print(f'Confirme os dados ---> pontos: {points} | description: {description}')
        if input('"q" -> cancela | <ENTER> -> confirma: ').strip() == 'q':
            print('Os dados dessa sessao foram descartados')
        else:
            data.append(_insert_point_and_description(points, description))
            print('Inserido no rascunho')

    return data


def special_eventos_igreja():
    """TRATAMENTO PARA MISSAO EVENTOS IGREJA"""
    print('* EVENTOS IGREJA\n')
    attendance_number = input('Número de presenças: ').strip()

    if not attendance_number.isnumeric():
        return None

    points = 100 + 50 * int(attendance_number)
    description = 'Participar ativamente dos eventos da igreja'
    for item in TABLE_POINTS:
        if item.get('code') == 'eventos-igreja':
            description = item['description']
            break
    return [_insert_point_and_description(points, description)]


def special_dinamicas():
    """Tratamento para dinamicas"""
    print('* MODO DINAMICAS! (Points: "q" para parar)\n')
    data = []
    while True:
        points = input('Pontos: ').strip()

        if points.lower() == 'q':
            break
        if not points.isnumeric():
            continue
        points = int(points)

        description = 'Dinamicas'
        for item in TABLE_POINTS:
            if item.get('code') == 'dinamicas':
                description = item['description']
                break

        data.append(_insert_point_and_description(points, description))

    return data


def insert_points(index):
    """
    Insere pontos para o item posicionado no indice passado como parametro

    Args:
         index: indice da posicao da missao na tabela de pontos (TABLE_POINTS)
    """
    item_table_points = TABLE_POINTS[index]
    points = item_table_points['points']
    description = item_table_points['description']

    additional_data = ''
    if item_table_points.get('additionalData'):
        additional_data = ': ' + input('Insira os dados adicionais (QUAL ou QUEM?)-> ').strip()

    return [_insert_point_and_description(points, f'{description}{additional_data}')]
