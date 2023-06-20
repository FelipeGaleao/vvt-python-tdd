# TDD utilizando Python

Introdução ao TDD utilizando Python

## Autores

- [Maycon Felipe Mota](https://github.com/felipegaleao)
- [Eduardo Godoy](https://google.com)
- [Thiago Lutz](https://google.com)
- [Vitor Oliveira Brandão](https://google.com)

## Ferramentas

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/stable/)

## Como preparar o ambiente?

1. Clone o repositório
2. Instale as dependências

```bash
pip install -r requirements.txt
```

## Introdução

O objetivo deste projeto é criar uma solução de calculadora utilizando a técnica de desenvolvimento de software chamada TDD (Test Driven Development).
Para a introdução, vamos utilizar a linguagem de programação Python.

## Roteiro

### 1. Contexto

Nós já sabemos que o [TDD](https://pt.wikipedia.org/wiki/Test-driven_development) é uma técnica de desenvolvimento de software que utiliza testes unitários para guiar o desenvolvimento. Embasadas pelas metodologias [SCRUM](https://www.desenvolvimentoagil.com.br/scrum/) e [XP](https://www.desenvolvimentoagil.com.br/xp/), TDD se baseia na filosofia "Teste primeiro, código depois". Essa técnica é composta por 3 etapas:

1. **Red**: O teste é escrito e executado, mas falha, pois o código ainda não existe.
2. **Green**: O código é escrito para que o teste passe.
3. **Refactor**: O código é refatorado para que o mesmo fique mais legível e performático.

Importante destacarmos que TDD é ir além de criar testes, é desenvolver (design) o software de forma incremental e iterativa, com foco na qualidade e sabendo que durante os incrementos, teremos a garantia que todas as funcionalidades já implementadas continuam funcionando.

### 2. Requisitos da Classe

É necessário criarmos uma classe que seja possível realizar as operações básicas de uma calculadora, como: soma, subtração, multiplicação e divisão. A aplicação deve receber dois números e retornar o resultado da operação.

### 3. Criando a primeira massa de teste

Vamos criar um arquivo `calculadora_test.py` que irá armazenar a massa de testes da nossa aplicação. Para isso, vamos utilizar o framework de testes [Pytest](https://docs.pytest.org/en/stable/)
Vamos relembrar nossos requisitos:

- A aplicação deve somar;
- A aplicação deve subtrair;
- A aplicação deve multiplicar;
- A aplicação deve dividir;
- A aplicação deve retornar o resultado da operação;
- A aplicação deve retornar uma mensagem de erro caso o divisor seja 0;

Vamos criar o primeiro teste:

```python
def test_soma():
    assert calculadora.soma(1, 1) == 2
```

Em seguida, vamos criar o arquivo `calculadora.py` e implementar o código para que o teste passe:

```python
class Calculadora:
    pass
```

Agora, vamos executar o teste:

```bash
pytest calculadora_test.py
```

Ao executar, o teste irá falhar, pois a classe `Calculadora` não possui o método `soma`, conforme o resultado abaixo:
    
```bash
====================================================================================================================== short test summary info ======================================================================================================================= 
FAILED calculadora_test.py::TestCalculadora::test_divisao - AttributeError: 'Calculadora' object has no attribute 'divisao'
FAILED calculadora_test.py::TestCalculadora::test_divisao_por_zero - AttributeError: 'Calculadora' object has no attribute 'divisao'
FAILED calculadora_test.py::TestCalculadora::test_multiplicacao - AttributeError: 'Calculadora' object has no attribute 'multiplicacao'
FAILED calculadora_test.py::TestCalculadora::test_soma - AttributeError: 'Calculadora' object has no attribute 'soma'
FAILED calculadora_test.py::TestCalculadora::test_subtracao - AttributeError: 'Calculadora' object has no attribute 'subtracao'
```

Vamos implementar o método `soma` na classe `Calculadora`:

```python
class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2
```

Agora, vamos executar o teste novamente:

```bash
pytest calculadora_test.py
```

Com isso, veremos que o teste passou. 

### 4. Criando os demais testes
Após criarmos o primeiro teste, vamos criar os demais testes para que a nossa aplicação atenda todos os requisitos. 

### 5. Refatoração
Após criarmos todos os testes, vamos refatorar o código para que fique mais enxuto e legível.

### 6. Conclusão
Após a conclusão do projeto, podemos percerber as vantagens do TDD, como:
- Código mais limpo;
- Código mais confiável;
- Segurança para realizar alterações no código;
- Maior produtividade;

## Referências
[TDD - Test Driven Development](https://www.devmedia.com.br/tdd-test-driven-development/18533)
[O que é TDD?](https://www.casadocodigo.com.br/pages/sumario-tdd)

"# vvt-python-tdd" 
