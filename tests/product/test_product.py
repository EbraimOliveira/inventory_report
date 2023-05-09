from inventory_report.inventory.product import Product


def test_cria_produto():
    my_product = Product(
        1,
        'óleo de peixe',
        'Duom',
        '20/05/2021',
        '20/05/2023',
        7898938,
        'Manter em local seco')

    assert my_product.id == 1
    assert my_product.nome_do_produto == 'óleo de peixe'
    assert my_product.nome_da_empresa == 'Duom'
    assert my_product.data_de_fabricacao == '20/05/2021'
    assert my_product.data_de_validade == '20/05/2023'
    assert my_product.numero_de_serie == 7898938
    assert my_product.instrucoes_de_armazenamento == 'Manter em local seco'
