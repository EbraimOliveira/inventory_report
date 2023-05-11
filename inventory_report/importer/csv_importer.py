from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            read_file = list(DictReader(file))
        return read_file
