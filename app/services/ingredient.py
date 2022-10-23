from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from app.services.crud_calls_decorator.crud_decorator import (DecoratorCreate,
                                                              DecoratorGetById,
                                                              DecoratorGet,
                                                              DecoratorUpdate)
from app.services.crud_calls_decorator.general_entity_component import ConcreteEntity

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return DecoratorCreate(
        ConcreteEntity(IngredientController, request.json)).crud_call()


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return DecoratorUpdate(
        ConcreteEntity(IngredientController, request.json)).crud_call()


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return DecoratorGetById(
        ConcreteEntity(IngredientController, _id)).crud_call()


@ingredient.route('/', methods=GET)
def get_ingredients():
    return DecoratorGet(
        ConcreteEntity(IngredientController)).crud_call()
