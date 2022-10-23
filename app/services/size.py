from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import SizeController
from app.services.crud_calls_decorator.crud_decorator import (DecoratorCreate,
                                                              DecoratorGetById,
                                                              DecoratorGet,
                                                              DecoratorUpdate)
from app.services.crud_calls_decorator.general_entity_component import ConcreteEntity

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return DecoratorCreate(
        ConcreteEntity(SizeController, request.json)).crud_call()


@size.route('/', methods=PUT)
def update_size():
    return DecoratorUpdate(
        ConcreteEntity(SizeController, request.json)).crud_call()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return DecoratorGetById(
        ConcreteEntity(SizeController, _id)).crud_call()


@size.route('/', methods=GET)
def get_sizes():
    return DecoratorGet(
        ConcreteEntity(SizeController)).crud_call()
