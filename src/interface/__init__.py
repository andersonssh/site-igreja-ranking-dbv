import json
import os
from src import api_connection

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

with open(os.path.join(parent_dir, 'configs/table_points.json'), 'r', encoding='utf-8') as f:
    TABLE_POINTS = json.load(f)

MEMBERS = api_connection.get_members()
COLOR_NONE = '\033[m'
COLOR_RED = '\033[1;31m'
COLOR_GREEN = '\033[32m'


def update_users_list():
    global MEMBERS
    MEMBERS = api_connection.get_members()


def clear():
    print('limpando tela')
    try:
        os.system('clear')
    except:
        os.system('cls')
