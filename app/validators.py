"""Validação e formatação de CPF e CNPJ (documentos brasileiros).

Implementa o cálculo dos dígitos verificadores conforme o algoritmo
oficial usado pela Receita Federal, sem depender de nenhum serviço
externo — o que torna os testes rápidos e determinísticos.
"""
import re


def _somente_digitos(documento: str) -> str:
    return re.sub(r"\D", "", documento or "")


def _calcular_digito_verificador(numeros: str, pesos: list[int]) -> str:
    soma = sum(int(digito) * peso for digito, peso in zip(numeros, pesos))
    resto = soma % 11
    return "0" if resto < 2 else str(11 - resto)


def is_valid_cpf(cpf: str) -> bool:
    """Retorna True se o CPF informado é matematicamente válido."""
    digitos = _somente_digitos(cpf)

    if len(digitos) != 11 or digitos == digitos[0] * 11:
        return False

    primeiro_dv = _calcular_digito_verificador(digitos[:9], list(range(10, 1, -1)))
    segundo_dv = _calcular_digito_verificador(
        digitos[:9] + primeiro_dv, list(range(11, 1, -1))
    )

    return digitos[-2:] == primeiro_dv + segundo_dv


def is_valid_cnpj(cnpj: str) -> bool:
    """Retorna True se o CNPJ informado é matematicamente válido."""
    digitos = _somente_digitos(cnpj)

    if len(digitos) != 14 or digitos == digitos[0] * 14:
        return False

    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_dv = _calcular_digito_verificador(digitos[:12], pesos_1)
    segundo_dv = _calcular_digito_verificador(digitos[:12] + primeiro_dv, pesos_2)

    return digitos[-2:] == primeiro_dv + segundo_dv


def format_cpf(cpf: str) -> str:
    """Formata um CPF (só dígitos ou já formatado) como 000.000.000-00."""
    d = _somente_digitos(cpf)
    if len(d) != 11:
        raise ValueError("CPF precisa ter 11 dígitos para ser formatado")
    return f"{d[0:3]}.{d[3:6]}.{d[6:9]}-{d[9:11]}"


def format_cnpj(cnpj: str) -> str:
    """Formata um CNPJ (só dígitos ou já formatado) como 00.000.000/0000-00."""
    d = _somente_digitos(cnpj)
    if len(d) != 14:
        raise ValueError("CNPJ precisa ter 14 dígitos para ser formatado")
    return f"{d[0:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:14]}"
