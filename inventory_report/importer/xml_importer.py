from inventory_report.importer.importer import Importer
from xml.etree.ElementTree import parse


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            