"""API para validação de CPF e CNPJ.

Projeto criado como parte das atividades formativas de DevOps:
Git/GitHub, CI/CD com GitHub Actions e Docker.
"""
from fastapi import FastAPI
from pydantic import BaseModel

from app.validators import format_cnpj, format_cpf, is_valid_cnpj, is_valid_cpf

app = FastAPI(
    title="Validador de CPF/CNPJ",
    description="API simples para validar e formatar documentos brasileiros.",
    version="1.0.0",
)


class DocumentoRequest(BaseModel):
    numero: str


@app.get("/health")
def health():
    """Endpoint de healthcheck — útil para o Docker/monitoramento saberem que a API está de pé."""
    return {"status": "ok"}


@app.post("/validar/cpf")
def validar_cpf(payload: DocumentoRequest):
    valido = is_valid_cpf(payload.numero)
    return {
        "numero": payload.numero,
        "valido": valido,
        "formatado": format_cpf(payload.numero) if valido else None,
    }


@app.post("/validar/cnpj")
def validar_cnpj(payload: DocumentoRequest):
    valido = is_valid_cnpj(payload.numero)
    return {
        "numero": payload.numero,
        "valido": valido,
        "formatado": format_cnpj(payload.numero) if valido else None,
    }
