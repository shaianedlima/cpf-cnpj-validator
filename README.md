# Validador de CPF/CNPJ

API simples em Python (FastAPI) para validar e formatar CPF e CNPJ, feita
como projeto prático das atividades formativas de DevOps: controle de
versão com Git/GitHub, pipeline de CI/CD com GitHub Actions e Docker.

## Endpoints

| Método | Rota            | Descrição                          |
|--------|-----------------|-------------------------------------|
| GET    | `/health`       | Healthcheck da aplicação            |
| POST   | `/validar/cpf`  | Valida e formata um CPF             |
| POST   | `/validar/cnpj` | Valida e formata um CNPJ            |

Exemplo de requisição:

```bash
curl -X POST http://localhost:8000/validar/cpf \
  -H "Content-Type: application/json" \
  -d '{"numero": "529.982.247-25"}'
```

Resposta:

```json
{
  "numero": "529.982.247-25",
  "valido": true,
  "formatado": "529.982.247-25"
}
```

## Rodando localmente (sem Docker)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

A API sobe em `http://localhost:8000`. Documentação interativa automática
em `http://localhost:8000/docs`.

## Testes

```bash
pytest -v
```

## Rodando com Docker

```bash
docker build -t cpf-cnpj-validator .
docker run -d -p 8000:8000 --name cpf-cnpj-validator cpf-cnpj-validator
docker ps
```

## CI/CD

- **CI** (`.github/workflows/ci.yml`): instala as dependências e roda os
  testes automatizados a cada push e pull request.
- **CD** (`.github/workflows/cd.yml`): builda a imagem Docker a cada push
  e pull request, garantindo que a aplicação está sempre pronta para ser
  implantada (continuous delivery).
- **Publicação no Docker Hub** (`.github/workflows/docker-publish.yml`):
  desafio opcional — builda e publica a imagem no Docker Hub a cada push
  no `main`. Requer os secrets `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN`
  configurados no repositório (Settings → Secrets and variables → Actions).
