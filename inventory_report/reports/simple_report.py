from typing import List
from datetime import datetime


class SimpleReport:
        
    @classmethod
    def closest_expiration_day(cls, products):
        currency_data = datetime.today().strftime('%Y-%m-%d')
        closest_expiration = products[0]['data_de_validade']

        for product in products:
            diff1 = (currency_data - product['data_de_validade'])
            diff2 = (currency_data - closest_expiration)
            if diff1 < diff2:
                closest_expiration = product['data_de_validade']
        return closest_expiration    

    @classmethod
    def count_companies(cls, products):
        companies = []
        for product in products:
            companies.append(product['nome_da_empresa'])
        return companies
    
    @classmethod
    def most_frequent(cls, products):
        companies = cls.count_companies(products)
        counter = 0
        company = companies[0]

        for i in companies:
            curr_frequency = companies.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                company = i
        return company

    @classmethod
    def generate(cls, products):
        company = cls.most_frequent(products)
        closest_expiration = cls.closest_expiration_day(products)

        return f"""Data de fabricação mais antiga: {list} 
Data de validade mais próxima: {closest_expiration}
Empresa com mais produtos: {company}"""


# Por convenção um metódo de classe usa o cls para referenciar a classe (assim como o self referencia o objeto)   
# O decorator @classmethod define o metodo como metodo de classe. Metodos de classe são aqueles referentes a informações da classe, que não mudam independente da instância.