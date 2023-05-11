from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:

    @classmethod
    def products_by_company(cls, products):
        companies = SimpleReport.companies(products)
        quantities = Counter(companies)
        products_by_company = ''
        for company in quantities:
            products_by_company += f'- {company}: {quantities[company]}\n'
        return products_by_company

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)
        products_by_company = cls.products_by_company(products)

        return f"""{simple_report}
Produtos estocados por empresa:
{products_by_company}"""
