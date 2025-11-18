# RPA Challenge - Advice Group Solution

Solução desenvolvida por **Marcus Vinicius** para o desafio técnico de RPA da Advice Group. O objetivo é automatizar o preenchimento de formulários dinâmicos no site [RPA Challenge](https://rpachallenge.com).

## 📋 Sobre o Projeto

O robô lê a base de dados Excel (`challenge.xlsx`) e submete os registros no portal, lidando com a mudança dinâmica da posição dos campos a cada rodada.

**Resultado da Execução:** O robô completou as 10 rodadas com **100% de precisão** (70 de 70 campos corretos).

**Tecnologias utilizadas:**
* **Python 3.13** (Linguagem principal)
* **Selenium WebDriver** (Automação Web)
* **Pandas** (Manipulação de dados e Excel)
* **Webdriver Manager** (Gerenciamento automático de drivers)
* **Logging** (Rastreabilidade e registros de execução)

---

## ⚙️ Como Executar

### Repositório e Contato
- **GitHub do Desenvolvedor:** https://github.com/Marcuss-Viniciuss

### Pré-requisitos
* Python 3.7 ou superior instalado.
* Google Chrome instalado.

### Passo a Passo

1.  **Clone este repositório** (ou baixe os arquivos):
    ```bash
    git clone [https://github.com/Marcuss-Viniciuss/RPA-Challenge.git](https://github.com/Marcuss-Viniciuss/RPA-Challenge.git)
    cd RPA-Challenge
    ```
    *(Substitua NOMEDO_SEU_REPO pelo nome real do seu repositório)*

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Robô:**
    Certifique-se de que o arquivo `challenge.xlsx` está na pasta raiz do projeto.
    ```bash
    python main.py
    ```
    *O resultado da execução será exibido no terminal e registrado no arquivo `execucao.log`.*

---

## 🧠 Abordagem Técnica e Diferenciais

### Estratégia para Elementos Dinâmicos (XPath Relativo)

O principal desafio é que os atributos `id`, `name` e a posição visual dos campos mudam a cada rodada.

**Solução:** A automação utiliza a âncora visual que permanece constante: o texto da **Label** (etiqueta) do campo.

**Implementação:** XPaths dinâmicos que localizam a Label e navegam para o campo de entrada (Input) imediatamente associado a ela, garantindo a **robustez** da solução:

```python
xpath = f"//label[text()='{Nome_Do_Campo}']/following-sibling::input"
