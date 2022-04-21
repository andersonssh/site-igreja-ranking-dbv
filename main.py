import pprint
import os
import json
from src import api_connection
from src.interface import (TABLE_POINTS,
                           Members,
                           score_handler,
                           show_menus,
                           clear)


def users_backup():
    members_backup_dir = os.path.join(os.path.expanduser('~'), 'Documentos/Backup-igreja/dbv')
    if not os.path.exists(members_backup_dir):
        os.makedirs(members_backup_dir)

    with open(os.path.join(members_backup_dir, 'members.json'), 'a', encoding='utf-8') as f:
        print('salvando backup na pasta: ', members_backup_dir)
        f.write(json.dumps(Members.MEMBERS, indent=3))


def handler_update_member():
    clear()
    index_member = show_menus.show_users_menu()
    member_id = Members.MEMBERS[index_member]['_id']

    name = input('Digite o novo nome do usuario: ').strip()
    role = input('Digite a nova funcao do usuario: ').strip()

    data, status_code = api_connection.update_member(member_id, name=name, role=role)
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
            return

        used_options = set()
        name_dbv = Members.MEMBERS[index_member]['name']
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
                data, status_code = api_connection.update_member(Members.MEMBERS[index_member]['_id'],
                                                                 score_details=score_details)
                if status_code == 200:
                    input('PONTOS CONTABILIZADOS COM SUCESSO!')
                else:
                    print('OS PONTOS NÂO PUDERAM SER CONTABILIZADOS!')
                    input(data)

        used_options = set()


def handler_show_members():
    clear()
    print('Ver todos os membros\n')
    for i in range(len(Members.MEMBERS)):
        print(f'{i}) {Members.MEMBERS[i]["name"]} | {Members.MEMBERS[i]["role"]} | '
              f'{Members.MEMBERS[i]["score"]}')
    index_member = input('\nInsira a opção: ')
    if not index_member.isnumeric():
        return
    index_member = int(index_member)
    name = Members.MEMBERS[index_member]['name']
    id_ = Members.MEMBERS[index_member]['_id']
    score = Members.MEMBERS[index_member]['score']
    score_details = Members.MEMBERS[index_member]['score_details']
    role = Members.MEMBERS[index_member]['role']

    print(f'_id: {id_}\nNome: {name}\nRole: {role}\nScore: {score}\nScore_details: ', end='')
    pprint.pprint(score_details)


def handler_post_members():
    clear()
    print('Inserir novo membro\n')
    name = input('Insira o nome do novo membro: ').strip().title()
    role = input('Insira a funcao do novo membro: ').strip()

    if input('"q"  cancela | <ENTER>  confirma: ').strip().lower() == 'q':
        return
    data, status_code = api_connection.insert_member(name, role)
    if status_code == 201:
        print('Usuario cadastrado!')
    else:
        print('Falha ao cadastrar usuario')
        print(data)


def show_menu():
    clear()
    print('Menu principal')
    print('1) Atualizar dados dos membros')
    print('2) Ver dados de todos os membros')
    print('3) Inserir novos membros')
    print('4) Atualizar nome e/ou cargo de membro')
    print('5) Fazer backup de dados dos usuarios localmente\n')
    option = input('Opção: ')

    if option == '1':
        handler_ranking()
    elif option == '2':
        handler_show_members()
    elif option == '3':
        handler_post_members()
    elif option == '4':
        handler_update_member()
    elif option == '5':
        users_backup()
    else:
        print('Opção inválida')

    input('\nPRESSIONE QUALQUER TECLA PARA CONTINUAR...')
    Members.update_users_list()


if __name__ == '__main__':
    while True:
        clear()
        show_menu()
