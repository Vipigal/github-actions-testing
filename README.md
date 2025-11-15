# Calculator - Projeto de CI/CD com GitHub Actions

Projeto simples demonstrando testes automatizados com GitHub Actions em múltiplos sistemas operacionais e versões Python.

## 📋 Descrição

Classe `Calculator` com operações matemáticas básicas:

- Adição
- Subtração
- Multiplicação
- Divisão (com tratamento de divisão por zero)
- Potenciação

## 🧪 Testes

9 testes unitários cobrindo:

- Casos normais
- Números negativos
- Edge cases (divisão por zero, potência zero)

## 🚀 CI/CD

GitHub Actions configurado para executar testes em:

**Sistemas Operacionais:**

- Ubuntu (Linux)
- MacOS
- Windows

**Versões Python:**

- 3.9
- 3.12

Isso resulta em **6 combinações** diferentes testadas a cada commit.

## 💻 Executar Localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar testes
pytest -v
```

## 📊 Status dos Testes

[![Tests](https://github.com/Vipigal/github-actions-testing/actions/workflows/tests.yml/badge.svg)](https://github.com/Vipigal/github-actions-testing/actions/workflows/tests.yml)
