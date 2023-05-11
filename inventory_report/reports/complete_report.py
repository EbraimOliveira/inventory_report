from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)

        return f"""{simple_report}
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE"""
