from app.common.http_methods import GET
from flask import Blueprint
from datetime import datetime

from ..controllers import OrderController
from app.services.crud_calls_decorator.crud_decorator import DecoratorGet, ConcreteEntity

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    orders_json_resopnse, status_code = DecoratorGet(
        ConcreteEntity(OrderController)).crud_call()
    orders_json= orders_json_resopnse.get_json()

    report_dict = {}
    clients_dict = {}
    months_revenue_dict = {}
    ingredients_dict = {}

    for order in orders_json:
        if order['client_name'] in clients_dict.keys():
            clients_dict[order['client_name']] = clients_dict[order['client_name']] + 1
        else:
            clients_dict[order['client_name']] = 1
        
        date_object = datetime.strptime(order['date'], "%Y-%m-%dT%H:%M:%S")
        if str(date_object.month) in months_revenue_dict.keys():
            months_revenue_dict[str(date_object.month)]= months_revenue_dict[str(date_object.month)] + order['total_price']
        else:
            months_revenue_dict[str(date_object.month)]= order['total_price']

        for ingredient in order['detail']:
            if ingredient['ingredient']['name'] in ingredients_dict.keys():
                ingredients_dict[ingredient['ingredient']['name']] = ingredients_dict[ingredient['ingredient']['name']] + 1
            else:
                ingredients_dict[ingredient['ingredient']['name']] = 1

    sorted_client_dict = sorted(clients_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_month_revenue_dict = sorted(months_revenue_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_ingredient_dict = sorted(ingredients_dict.items(), key=lambda x:x[1], reverse=True)
    
    report_dict['top_customers'] = [sorted_client_dict[0], sorted_client_dict[1], sorted_client_dict[2]]
    report_dict['wealthy_month'] = sorted_month_revenue_dict[0]
    report_dict['popular_ingredient'] = sorted_ingredient_dict[0]

    return report_dict, status_code
