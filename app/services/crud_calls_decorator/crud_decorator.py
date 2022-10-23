from flask import jsonify
from .general_entity_component import AbstEntity


class AbstCruDecorator(AbstEntity):

    abstEntity: AbstEntity = None

    def __init__(self, abstEntity: AbstEntity):
        self.abstEntity = abstEntity

    def crud_call(self):
        return self.abstEntity.crud_call()


class DecoratorGet(AbstCruDecorator):

    def __init__(self, abstEntity: AbstEntity):
        super().__init__(abstEntity)

    def crud_call(self):
        entityController = self.abstEntity.crud_call()
        entity, error = entityController.get_all()
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code


class DecoratorCreate(AbstCruDecorator):

    def __init__(self, abstEntity: AbstEntity):
        super().__init__(abstEntity)

    def crud_call(self):
        entityController = self.abstEntity.crud_call()
        entity, error = entityController.create(
            self.abstEntity.get_entityParameter())
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code


class DecoratorUpdate(AbstCruDecorator):

    def __init__(self, abstEntity: AbstEntity):
        super().__init__(abstEntity)

    def crud_call(self):
        entityController = self.abstEntity.crud_call()
        entity, error = entityController.update(
            self.abstEntity.get_entityParameter())
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code


class DecoratorGetById(AbstCruDecorator):

    def __init__(self, abstEntity: AbstEntity):
        super().__init__(abstEntity)

    def crud_call(self):
        entityController = self.abstEntity.crud_call()
        _id = self.abstEntity.get_entityParameter()
        entity, error = entityController.get_by_id(_id)
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code
