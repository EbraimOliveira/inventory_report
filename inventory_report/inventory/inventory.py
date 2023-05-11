from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        
        if type == 'simples':
            return SimpleReport.generate(read_file)
        return CompleteReport.generate(read_file)
