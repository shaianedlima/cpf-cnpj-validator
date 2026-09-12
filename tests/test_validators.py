from app.validators import format_cnpj, format_cpf, is_valid_cnpj, is_valid_cpf


def test_cpf_valido():
    assert is_valid_cpf("529.982.247-25") is True


def test_cpf_invalido_digito_verificador_errado():
    assert is_valid_cpf("529.982.247-26") is False


def test_cpf_invalido_todos_digitos_iguais():
    assert is_valid_cpf("111.111.111-11") is False


def test_cpf_invalido_tamanho_errado():
    assert is_valid_cpf("123456") is False


def test_cnpj_valido():
    assert is_valid_cnpj("11.222.333/0001-81") is True


def test_cnpj_invalido_digito_verificador_errado():
    assert is_valid_cnpj("11.222.333/0001-82") is False


def test_cnpj_invalido_todos_digitos_iguais():
    assert is_valid_cnpj("11.111.111/1111-11") is False


def test_format_cpf():
    assert format_cpf("52998224725") == "529.982.247-25"


def test_format_cnpj():
    assert format_cnpj("11222333000181") == "11.222.333/0001-81"
