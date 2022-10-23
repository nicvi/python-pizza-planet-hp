from app.common.http_methods import GET
from flask import Blueprint

from app.controllers.report import ReportController

from app.services.crud_calls_decorator.crud_decorator import DecoratorGet, ConcreteEntity

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return DecoratorGet(
        ConcreteEntity(ReportController)).crud_call()
