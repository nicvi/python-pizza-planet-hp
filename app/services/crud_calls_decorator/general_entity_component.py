from app.controllers.base import BaseController


class AbstEntity:

    def crur_call(self):
        pass

    def get_entityParameter(self):
        pass


class ConcreteEntity(AbstEntity):

    def __init__(self, baseController: BaseController, entityParameter=None):
        self.baseController = baseController
        self.entityParameter = entityParameter

    def crud_call(self):
        return self.baseController

    def get_entityParameter(self):
        return self.entityParameter
