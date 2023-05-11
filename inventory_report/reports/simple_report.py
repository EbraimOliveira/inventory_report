from datetime import datetime


class SimpleReport:

    @classmethod
    def earliest_manufacturing_date(cls, products):
        earliest_manufacturing = products[0]["data_de_fabricacao"]
        for product in products:
            if earliest_manufacturing > product["data_de_fabricacao"]:
                earliest_manufacturing = product["data_de_fabricacao"]
        return earliest_manufacturing

    @classmethod
    def valid_dates(cls, products):
        currency_data = datetime.today().strftime('%Y-%m-%d')
        valid_dates = []
        for product in products:
            if product['data_de_validade'] >= currency_data:
                valid_dates.append(product['data_de_validade'])
        return valid_dates

    @classmethod
    def closest_expiration_day(cls, products):
        valid_dates = cls.valid_dates(products)
        closest_expiration = valid_dates[0]
        for date in valid_dates:
            if closest_expiration > date:
                closest_expiration = date
        return closest_expiration

    @classmethod
    def count_companies(cls, products):
        companies = []
        for product in products:
            companies.append(product["nome_da_empresa"])
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
        earliest_manufacturing = cls.earliest_manufacturing_date(products)

        return f"""Data de fabricação mais antiga: {earliest_manufacturing}
Data de validade mais próxima: {closest_expiration}
Empresa com mais produtos: {company}"""
