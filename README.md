# Monitoramento

Projeto relacionado ao monitoramento e identificação de fraudes em licitações, desenvolvido como parte de projeto de pesquisa da UFPB. O sistema inclui um guia completo sobre fraudes em licitações e uma interface web baseada em Django.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Django
- **Frontend:** HTML, CSS

## Estrutura do Projeto

- `fraudes/`: Diretório principal da aplicação Django.
  - `config/`: Arquivos de configuração do projeto Django (`settings.py`, `urls.py`, etc).
  - `core/`: Aplicativo principal que contém as lógicas de negócio, modelos (`models.py`) e visualizações (`views.py`).
  - `templates/`: Templates HTML do projeto (ex: `index.html`, `fraude_licitacoes.html`, `guia_relatorio.html`).
  - `static/`: Arquivos estáticos como estilos CSS (`guia.css`).
- `requirements.txt`: Lista de dependências Python necessárias.
- `fraude_licitacoes_guia_completo.html`: Documento do guia na raiz do repositório.

## Configuração e Execução Local

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/francisco-carlos-ufpb/monitoramento.git
   cd monitoramento
   ```

2. **Crie e ative um ambiente virtual:**
   - **No Windows:**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - **No Linux/MacOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Nota: O diretório `fraudes` também contém seu próprio `requirements.txt`. Certifique-se de instalar as dependências necessárias)*.

4. **Navegue até a pasta do projeto Django e execute as migrações:**
   ```bash
   cd fraudes
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

A aplicação deverá ficar disponível pelo navegador no endereço `http://127.0.0.1:8000/`.

## Licença

Este projeto é desenvolvido para fins de pesquisa pela UFPB.
