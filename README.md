# Sistema de Gerenciamento de Notas

## Descrição

Este projeto consiste em um sistema simples de gerenciamento de notas desenvolvido em Python. O sistema tem como objetivo armazenar e manipular dados acadêmicos de estudantes, calcular médias automaticamente, verificar a situação de aprovação e gerar relatórios organizados no terminal.

O projeto aplica conceitos fundamentais de programação, como listas, dicionários, funções, modularização, documentação com docstrings e testes unitários.

## Funcionalidades

* Armazenamento de estudantes e notas utilizando lista de dicionários;
* Cálculo automático de médias;
* Verificação de aprovação ou reprovação;
* Geração de relatórios acadêmicos;
* Estrutura modular baseada em funções;
* Testes unitários para validação do sistema.

## Tecnologias Utilizadas

* Python 3
* Biblioteca `unittest`

## Aprendizados

Depois de fazer o projeto, consegui consolidar diversos conceitos importantes de programação em Python, principalmente o uso de listas, dicionários, funções, controle de fluxo, documentação de código e testes unitários.

## Como executar o sistema

### 1. Abrir o terminal

Abra o terminal do VS Code ou o Prompt de Comando na pasta onde os arquivos do projeto estão salvos.

### 2. Executar o sistema principal

Digite o comando:

```bash
python gerenciador_notas.py
```

O programa exibirá no terminal o relatório contendo:

* nome do estudante;
* média calculada;
* situação final (Aprovado ou Reprovado).

## Como executar os testes

Para executar os testes unitários do sistema, utilize o comando:

```bash
python test_notas.py
```

Os testes verificam:

* cálculo correto da média;
* aprovação com média acima da mínima;
* reprovação com média abaixo da mínima;
* comportamento da função com lista de notas vazia;
* funcionamento da aprovação quando a média mínima é igual a zero.

## Estrutura do Projeto

```text
gerenciador_notas.py
test_notas.py
README.md
```

## Autor

Projeto desenvolvido para a disciplina de Programação de Computadores.
