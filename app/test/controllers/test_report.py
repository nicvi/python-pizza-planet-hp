import pytest
from datetime import datetime
from app.controllers import ReportController
from app.test.utils.functions import get_random_price, get_random_month
from sqlalchemy.exc import SQLAlchemyError


def _top_customer():
    return [('yejdifbmov', 12), ('zfxiuglpac', 10), ('rhaknuftlz', 8)]


def _top_ingredient():
    return ('hsyqmlfreg', 36)


@staticmethod
def _months_revenue():
    month = get_random_month() - 1
    months_revenue = []
    for _ in range(2):
        months_revenue.append((datetime(
            2022, month, 4,
            20, 3, 5), get_random_price(40, 110))
        )
        month += 1
    return months_revenue


def test__get_all_report_return_successful_response(mocker):
    # report_data = _top_customer(), _top_ingredient(), _months_revenue()
    top_customer = _top_customer()
    top_ingredient = _top_ingredient()
    months_revenue = _months_revenue()
    mocker.patch(
        'app.controllers.report.ReportManager.get_report',
        return_value=(top_customer, top_ingredient, months_revenue)
    )

    report_data_obtained, error = ReportController.get_all()

    assert error == None
    assert len(report_data_obtained['top_customers']) == 3
    assert type(int(report_data_obtained['wealthy_month'][0])) == type(int())
    assert type(report_data_obtained['wealthy_month'][1]) == type(float())
    assert report_data_obtained['popular_ingredient'] == top_ingredient


def test__get_all_report_return_alchemy_error(mocker):
    error_msn = 'SQLAlchemyError'
    mocker.patch(
        'app.controllers.report.ReportManager.get_report',
        side_effect=SQLAlchemyError("SQLAlchemyError"),
    )

    report_data_obtained, error = ReportController.get_all()

    assert report_data_obtained == None
    assert error == error_msn


def test__get_all_report_return_runtime_error_response(mocker):
    error_msn = 'RuntimeError'
    mocker.patch(
        'app.controllers.report.ReportManager.get_report',
        side_effect=SQLAlchemyError("RuntimeError"),
    )

    report_data_obtained, error = ReportController.get_all()

    assert report_data_obtained == None
    assert error == error_msn


def test__get_top_month_revenue():
    months_revenue = _months_revenue()
    top_month = months_revenue[0][0] \
        if months_revenue[0][1] >= months_revenue[1][1] \
        else months_revenue[1][0]

    top_month_revenue = ReportController.get_top_month_revenue(months_revenue)

    assert top_month_revenue[0] == str(top_month.month)
    assert len(str(top_month_revenue[1]).split('.')[1]) <= 2


def test__format_response():
    top_customer_row = _top_customer()
    top_ingredient = _top_ingredient()
    months_revenue = _months_revenue()

    formatted_report = ReportController.format_response(
        top_customer_row, top_ingredient, months_revenue)

    assert formatted_report['top_customers'] != None
    assert formatted_report['wealthy_month'] != None
    assert formatted_report['popular_ingredient'] != None


def test__sqlalchemy_row_to_list():
    top_customer_row = _top_customer()
    index = 0

    top_customers_list = ReportController.sqlalchemy_row_to_list(
        top_customer_row)

    for customer in top_customers_list:
        assert type(customer) == list
        assert customer[0] == top_customer_row[index][0]
        assert customer[1] == top_customer_row[index][1]
        index += 1
