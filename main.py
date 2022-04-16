from src import api_connection
from src.interface import (MEMBERS,
                           TABLE_POINTS,
                           update_users_list,
                           score_handler,
                           show_menus,
                           clear)
import pprint


def handler_update_member():
    name = input('Digite o novo nome do usuario: ').strip()
    role = input('Digite a nova funcao do usuario: ').strip()

    data, status_code = api_connection.update_member(name=name, role=role)
    if status_code == 200:
        print('USUARIO ATUALIZADO COM SUCESSO!')
    else:
        print('Falha ao atualizar usuario')
        print(data)


def handler_ranking():
    while True:
        clear()
        print('Atualizar dados dos membros (digite "q" para sair)\n')
        index_member = show_menus.show_users_menu()

        if index_member == -1:
            break

        used_options = set()
        name_dbv = MEMBERS[index_member]['name']
        while True:
            clear()
            print('digite "q" para voltar ao menu anterior')
            index_table_points = show_menus.show_points_menu(name_dbv, used_options)
            used_options.add(index_table_points)

            if index_table_points == -1:
                break

            score_details = []
            code = TABLE_POINTS[index_table_points].get('code')
            if code:
                if code == 'outro':
                    score_details = score_handler.special_personalizado()
                elif code == 'eventos-igreja':
                    score_details = score_handler.special_eventos_igreja()
                elif code == 'dinamicas':
                    score_details = score_handler.special_dinamicas()
            else:
                score_details = score_handler.insert_points(index_table_points)

            if input('PERSISTIR ALTERAÇÕES? "q"  cancela | <ENTER>  confirma: ').strip().lower() == 'q':
                print('As alteracoes foram descartadas')
            else:
                data, status_code = api_connection.update_member(MEMBERS[index_member]['_id'],
                                                                 score_details=score_details)
                if status_code == 200:
                    print('PONTOS CONTABILIZADOS COM SUCESSO!')
                else:
                    print('OS PONTOS NÂO PUDERAM SER CONTABILIZADOS!')
                    print(data)

        used_options = set()


def handler_show_members():
    print('Ver todos os usuarios\n')
    for user in MEMBERS:
        pprint.pprint(user)


def handler_post_members():
    print('Inserir novo membro\n')
    name = input('Insira o nome do novo membro: ').strip().title()
    role = input('Insira a funcao do novo membro: ').strip()
    if input('Digite "s" para inserir os dados ou qualquer'
             ' outra tecla para cancelar: ').strip().lower() == 's':
        data, status_code = api_connection.insert_member(name, role)
        if status_code == 201:
            print('Usuario cadastrado!')
        else:
            print('Falha ao cadastrar usuario')
            print(data)
    return None


def show_menu():
    print('Menu principal')
    print('1) Atualizar dados dos membros')
    print('2) Ver dados de todos os membros')
    print('3) Inserir novos membros\n')
    option = input('Opção: ')

    if option == '1':
        handler_ranking()
    if option == '2':
        handler_show_members()
    elif option == '3':
        handler_post_members()
    input('\nPRESSIONE QUALQUER TECLA PARA CONTINUAR...')
    update_users_list()


if __name__ == '__main__':
    while True:
        clear()
        show_menu()
