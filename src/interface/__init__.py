import json
from src import api_connection

with open('../configs/table_points.json', 'r', encoding='utf-8') as f:
    TABLE_POINTS = json.load(f)

USERS = api_connection.get_members()
COLOR_NONE = '\033[m'
COLOR_RED = '\033[1;31m'
COLOR_GREEN = '\033[32m'
