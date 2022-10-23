from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..controllers import OrderController
from app.services.crud_calls_decorator.crud_decorator import (DecoratorCreate,
                                                              DecoratorGetById,
                                                              DecoratorGet)
from app.services.crud_calls_decorator.general_entity_component import ConcreteEntity

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return DecoratorCreate(
        ConcreteEntity(OrderController, request.json)).crud_call()


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return DecoratorGetById(
        ConcreteEntity(OrderController, _id)).crud_call()


@order.route('/', methods=GET)
def get_orders():
    return DecoratorGet(
        ConcreteEntity(OrderController)).crud_call()
