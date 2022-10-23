from ..repositories.managers import ReportManager
from .base import BaseController
from sqlalchemy.exc import SQLAlchemyError


class ReportController(BaseController):
    manager = ReportManager

    @staticmethod
    def get_top_month_revenue(months_revenue):
        months_revenue_dict = {}
        for date, price in months_revenue:
            if str(date.month) in months_revenue_dict.keys():
                months_revenue_dict[str(date.month)] = round(months_revenue_dict[str(
                    date.month)] + price, 2)
            else:
                months_revenue_dict[str(date.month)] = round(price, 2)
        sorted_month_revenue_dict = sorted(
            months_revenue_dict.items(), key=lambda x: x[1], reverse=True)
        top_month_revenue = sorted_month_revenue_dict[0]
        return top_month_revenue

    @staticmethod
    def sqlalchemy_row_to_list(top_customers_row):
        top_customers_list = []
        for name, ordered_times in top_customers_row:
            top_customers_list.append([name, ordered_times])
        return top_customers_list

    @staticmethod
    def format_response(top_customers_row, top_month_revenue, top_ingredient):
        report = {}
        top_customers_list = ReportController.sqlalchemy_row_to_list(
            top_customers_row)
        report['top_customers'] = [top_customers_list[0],
                                   top_customers_list[1], top_customers_list[2]]
        report['wealthy_month'] = top_month_revenue
        report['popular_ingredient'] = top_ingredient
        return report

    @classmethod
    def get_all(cls):
        try:
            top_customers, top_ingredient, months_revenue = cls.manager.get_report()
            top_month_revenue = cls.get_top_month_revenue(months_revenue)
            report = cls.format_response(
                top_customers, top_month_revenue, top_ingredient)
            return report, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
