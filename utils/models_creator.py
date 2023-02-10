import os
import json
import random
from models.models import *
from flask import current_app


def get_customer(pk):
    path_to_resource = os.path.join(current_app.config['BASE_DIR'], 'data_resources', 'users.json')
    with open(path_to_resource) as f:
        items = json.load(f)

    for data in items:
        if data['client_id'] == pk:
            return data


def gen_code():
    list_ = [random.randint(1, 5) for _ in range(5)]
    res = int(''.join(map(str, list_)))
    return res


def create_new_type(code, name):
    try:   
        type = Type()
        type.code = code
        type.name = name
        db.session.add(type)
        db.session.commit()
        return type.id
    except Exception as error:
        return error


def create_new_customer(name, surname, patronymic, inn, birth_date):
    try:
        customer = Customer()
        customer.name = name
        customer.surname = surname
        customer.patronymic = patronymic
        customer.inn = inn
        customer.birth_date = birth_date
        db.session.add(customer)
        db.session.commit()
        return customer.id
    except Exception as error:
        return error


def create_new_document(doc_number, customer_id, type_id):
    try:   
        document = Document()
        document.doc_number = doc_number
        document.customer_id = customer_id
        document.type_id = type_id
        db.session.add(document)
        db.session.commit()
        return 'Ok'
    except Exception as error:
        return error