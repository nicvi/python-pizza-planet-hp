from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column
from sqlalchemy import func

from .models import Ingredient, Order, OrderDetail, Size, Beverage, SideOrder, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)

        cls.session.add_all((OrderDetail(order_id=new_order._id,
                                         ingredient_id=ingredient._id,
                                         ingredient_price=ingredient.price)
                             for ingredient in ingredients
                             ))
        cls.session.add_all((SideOrder(order_id=new_order._id,
                                       beverage_id=beverage._id,
                                       beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class ReportManager(BaseManager):

    @classmethod
    def hola(cls):
        return 'hola'

    @classmethod
    def get_report(cls):
        clients_coincidences = cls.session.query(
            Order.client_name,
            func.count(Order.client_name)
        ).group_by(Order.client_name)\
            .order_by(func.count(Order.client_name).desc())\
            .all()
        top_clients = clients_coincidences[0:3] if len(clients_coincidences) >= 3 else None

        ingredients_id = cls.session.query(
            OrderDetail.ingredient_id,
            func.count(OrderDetail.ingredient_id)
        ).group_by(OrderDetail.ingredient_id)\
            .order_by(func.count(OrderDetail.ingredient_id).desc())\
            .all()
        top_ingredient = ingredients_id[0]
        top_ingredient_name = db.session.query(Ingredient.name).filter(
            Ingredient._id == top_ingredient[0]).first()[0]

        months_revenue = cls.session.query(
            Order.date,
            Order.total_price
        ).group_by(Order.date)\
            .order_by(Order.date)\
            .all()
        return top_clients, (top_ingredient_name, top_ingredient[1]), months_revenue


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
