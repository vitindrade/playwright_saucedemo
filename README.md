# Projeto: Automação de Testes com Playwright e Pytest

Este repositório contém testes automatizados para o site [Sauce Demo](https://www.saucedemo.com/), desenvolvida em **Python** utilizando **Playwright** e **Pytest**, seguindo o padrão **Page Object**. O objetivo é demonstrar a cobertura das principais açoes de usuário na aplicação, buscando possiveis falhas.

## Conteúdo

* **fixtures/**: dados de teste (usuários com credenciais válidas, inválidas e bloqueadas).
* **pages/**: objetos de página (Login, Products, Cart, Checkout).
* **tests/**: casos de teste, executando login, adição/remoção de itens, ordenação, persistência de carrinho e fluxo de checkout.
* **reports/**: relatorios html de falhas.
* **conftest.py**: configurações de fixtures do Pytest (inicialização do Playwright, browser, page e carregamento dos dados).
* **pytest.ini**: configurações globais do Pytest (timeout e navegadores).
* **requirements.txt**: dependências do projeto.

---

## Pré-requisitos

* **Python 3.8+**
* **Playwright**
* **Pytest**

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/vitindrade/playwright_saucedemo.git
```

### 2. Crie e ative um ambiente virtual

* **Linux / macOS**

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

* **Windows (PowerShell)**

  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

### 3. Instale dependências

```bash
pip install -r requirements.txt
```

### 4. Instale navegadores do Playwright

```bash
playwright install
playwright install-deps  # Apenas Linux
```

---

## Estrutura de Diretórios

```
saucedemo_playwright/
├── fixtures/           # Dados de usuários (users.json)
├── pages/              # Page Objects (login, products, cart, checkout)
├── tests/              # Test suites (test_login.py, test_products.py, ...)
├── reports/            # Relatorios html
├── conftest.py         # Fixtures Pytest (browser, page, users)
├── pytest.ini          # Config Pytest (env, timeout)
└── requirements.txt    # Dependências Python
```

---

## Execução dos Testes

Para rodar em um navegador específico:

```bash
pytest --browser=chromium
pytest --browser=firefox
pytest --browser=webkit
```

---

## Relatórios e Traces

* **Relatório HTML**: adicione `--html=report.html` ao comando Pytest.