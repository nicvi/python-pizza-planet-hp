from app.test.utils.functions import *
from app.test.fixtures.beverage import beverage_mock
from app.test.fixtures.size import size_mock
from app.test.fixtures.ingredient import ingredient_mock
from app.test.fixtures.order import client_data_mock
from app.repositories.models import Ingredient, Order, OrderDetail, Size, Beverage, SideOrder, db
from app.repositories.serializers import SizeSerializer
import requests


def create_order(customer_data: dict) -> dict:
    order_dict = {
        'client_name': customer_data['client_name'],
        'client_dni': customer_data['client_dni'],
        'client_address': customer_data['client_address'],
        'client_phone': customer_data['client_phone'],
        'date': random_date(),
        'size_id': random_size_id(),
        "ingredients": random_id_list(),
        "beverages": random_id_list()
    }
    return order_dict


def create_clients() -> list:
    number_clients = 20
    client_list = []
    client_number = 0
    while client_number < number_clients:
        client_list.append(client_data_mock())
        client_number += 1
    return client_list


def post_entity(url_endpoint: str, number_entities: int, dict_entity=None):
    url = f'http://127.0.0.1:5000/{url_endpoint}/'
    entity_number = 0
    if (url_endpoint == 'order'):
        clients_list = create_clients()
        while entity_number < number_entities:
            order_dict = create_order(random.choice(clients_list))
            requests.post(url, json=order_dict)
            entity_number += 1
    else:
        while entity_number < number_entities:
            requests.post(url, json=dict_entity())
            entity_number += 1


if __name__ == '__main__':
    post_entity('ingredient', 10, ingredient_mock)
    post_entity('beverage', 10, beverage_mock)
    post_entity('size', 5, size_mock)
    post_entity('order', 100)
    pass
