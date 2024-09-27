# Projeto de Calculadoras com Flask

Este projeto consiste no desenvolvimento de uma série de calculadoras utilizando o framework Flask em Python. O objetivo principal é explorar boas práticas de design de código, arquitetura de software e testes unitários. Cada calculadora foi desenvolvida seguindo padrões específicos, implementando conceitos como injeção de dependência, uso de interfaces e tratamentos personalizados de erro.

## Funcionalidades

- **Calculadora 1:** Realiza cálculos básicos com um único número fornecido.
- **Calculadora 2:** Lida com uma lista de números, realizando operações matemáticas e cálculos estatísticos.
- **Calculadora 3:** Verifica se a variância de uma lista de números é menor que a multiplicação dos mesmos, utilizando `NumPy` para cálculos mais complexos.


## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web utilizado para criar as rotas e manipular as requisições.
- **NumPy**: Biblioteca usada para cálculos matemáticos e estatísticos, como variância e desvio padrão.
- **PyTest**: Ferramenta para criação e execução de testes unitários.
- **Postman**: Utilizado para testar as rotas da API.

## Instalação e Execução

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/devGabyAlves/flask-calculator-design.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd flask-calculator-design
    ```

3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

4. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o servidor Flask:
    ```bash
    python run.py
    ```

6. Acesse as rotas das calculadoras via Postman ou navegador:
    - `POST /calculator/1`
    - `POST /calculator/2`
    - `POST /calculator/3`

## Testes

Para executar os testes unitários do projeto, utilize o comando:

```bash
pytest
 ```

Isso garantirá que todas as calculadoras estão funcionando corretamente e que as funcionalidades foram devidamente testadas.

## Tratamento de Erros

Implementei um tratamento de erros personalizado com a função handleErrors, que captura exceções em toda a aplicação e retorna mensagens de erro amigáveis e detalhadas ao usuário, melhorando a experiência de uso.

## Contribuição

Se desejar contribuir com o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias e sugestões. Toda contribuição é bem-vinda!

## Contribuição

Este projeto está licenciado sob os termos da MIT License.

