from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from app.services.crud_calls_decorator.crud_decorator import (DecoratorCreate,
                                                              DecoratorGetById,
                                                              DecoratorGet,
                                                              DecoratorUpdate)
from app.services.crud_calls_decorator.general_entity_component import ConcreteEntity

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return DecoratorCreate(
        ConcreteEntity(BeverageController, request.json)).crud_call()


@beverage.route('/', methods=PUT)
def update_beverage():
    return DecoratorUpdate(
        ConcreteEntity(BeverageController, request.json)).crud_call()


@beverage.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return DecoratorGetById(
        ConcreteEntity(BeverageController, _id)).crud_call()


@beverage.route('/', methods=GET)
def get_beverage():
    return DecoratorGet(
        ConcreteEntity(BeverageController)).crud_call()
