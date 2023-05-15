from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        path_extension = path.split(".")
        print("LOG >>>>>>>", path_extension)
        if path_extension[1] == "csv":
            products = CsvImporter.import_data(path)
        if path_extension[1] == "json":
            products = JsonImporter.import_data(path)
        if path_extension[1] == "xml":
            products = XmlImporter.import_data(path)
        if type == "simples":
            return SimpleReport.generate(products)
        return CompleteReport.generate(products)
