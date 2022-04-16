import os
from requests import get, post, put

APP_URL = os.getenv('APP_URL', 'http://localhost:5000/')
MEMBERS_ROUTE = APP_URL + 'members/'
LOGIN_ROUTE = APP_URL + 'login'


def jwt_header_generate():
    data = post(LOGIN_ROUTE, json={'username': os.getenv('USERNAME', ''),
                                   'password': os.getenv('PASSWORD', '')}).json()
    token = data.get('token')
    if not token:
        raise RuntimeError('USUARIO OU SENHA INCORRETO')

    return {'Authorization': 'Bearer ' + token}


JWT_HEADER = jwt_header_generate()


def get_members():
    return get(MEMBERS_ROUTE).json()


def get_member(member_id):
    return get(MEMBERS_ROUTE + member_id).json()


def insert_member(name, role):
    response = post(MEMBERS_ROUTE, headers=JWT_HEADER, json={'name': name,
                                                             'role': role})
    return response.json(), response.status_code


def update_member(member_id, name: str = None, role: str = None, score_details: dict = None):
    payload = {}
    if not name:
        payload['name'] = name
    if not role:
        payload['role'] = role
    if not score_details:
        payload['score_details'] = score_details

    response = put(MEMBERS_ROUTE + member_id, headers=JWT_HEADER, json=payload)
    return response.json(), response.status_code
