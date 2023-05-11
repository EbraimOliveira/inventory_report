from inventory_report.importer.importer import Importer
from xml.etree.ElementTree import parse


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            response = parse(file).getroot()
            produtcs = []
            for itens in response:
                element = {}
                for item in itens:
                    element[item.tag] = item.text
                produtcs.append(element)
        return produtcs
