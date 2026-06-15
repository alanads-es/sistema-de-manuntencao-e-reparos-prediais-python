# sistema-de-manuntencao-e-reparos-prediais-python

## Descrição

O Sistema de Manutenção e Reparos Prediais é uma aplicação desenvolvida em Python para o gerenciamento de ordens de serviço. O sistema permite cadastrar, listar, editar e remover solicitações de manutenção, armazenando os dados em um arquivo local para garantir a persistência das informações entre diferentes execuções do programa. O projeto foi desenvolvido utilizando conceitos fundamentais de programação, como orientação a objetos, manipulação de arquivos, validação de dados, expressões regulares e modularização do código.

## Funcionalidades

- Cadastro de ordens de serviço;
- Geração automática de identificador único (ID) para cada ordem;
- Validação de campos obrigatórios;
- Validação de datas no formato DD/MM/AAAA;
- Validação e formatação de números de telefone;
- Listagem de todas as ordens cadastradas;
- Edição de ordens de serviço;
- Remoção de ordens por ID;
- Armazenamento permanente dos dados em arquivo texto.

## Estrutura do Projeto

```text
classOrdemDeServico.py
dataManager.py
main.py
options.py
ordensdeservico.txt
```

## Arquivos do Projeto

### classOrdemDeServico.py

Contém a classe OrdemDeServico, responsável por representar uma ordem de serviço e armazenar seus dados. A classe possui os atributos: ID da ordem, requisitante, telefone, descrição e data da ordem de serviço. Também possui métodos para formatação e armazenamento dos dados.

### dataManager.py

Responsável pela persistência dos dados do sistema. Possui as funções `loadData()` para carregar as ordens salvas no arquivo e `saveData()` para salvar as ordens cadastradas.

### options.py

Contém as funcionalidades do sistema, como adicionar, listar, editar e remover ordens de serviço. Também realiza validações para garantir a integridade dos dados.

### main.py

Arquivo principal do sistema. Responsável por exibir o menu, receber a opção do usuário, executar as funcionalidades correspondentes e manter o sistema em execução até a opção de saída.

## Tecnologias Utilizadas

Python 3, Programação Orientada a Objetos (POO), Manipulação de arquivos, Expressões regulares (Regex), Biblioteca datetime, Biblioteca pathlib.

## Como executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd nome-do-projeto
```

3. Execute o programa:

```bash
python main.py
```

## Exemplo de uso

```text
Sistema de Manutenção e Reparos Prediais

[1] Adicionar ordem de serviço
[2] Remover ordem de serviço
[3] Editar ordem de serviço
[4] Listar ordens de serviço
[5] Sair

Cadastro de uma ordem:

Digite o nome do requisitante: João Silva
Digite o telefone: 83999999999
Digite a descrição da ordem de serviço: Troca de lâmpada
Digite a data da ordem de serviço: 15/06/2026
```

## Validações implementadas

### Campos obrigatórios

Não permite cadastro vazio.

### Data

Aceita apenas formato DD/MM/AAAA.

Exemplo:

```text
15/06/2026
```

### Telefone

Aceita números com DDD e formata automaticamente.

Exemplo:

```text
83999999999 → (83) 99999-9999
```

## Armazenamento dos dados

Os dados são armazenados no arquivo `ordensdeservico.txt` no formato:

```text
ID:REQUISITANTE:TELEFONE:DESCRIÇÃO:DATA
```

Exemplo:

```text
1:João Silva:(83) 99999-9999:Troca de lâmpada:15/06/2026
```

## Conceitos aplicados

Programação Orientada a Objetos, classes e objetos, métodos construtores, manipulação de arquivos, estruturas de repetição, estruturas condicionais, tratamento de exceções, expressões regulares, modularização de código e validação de dados.

## Autores

Projeto desenvolvido para fins acadêmicos na disciplina de Algoritmos.

**Integrantes do grupo:**

- José Alan Dias Almeida;
- Emanuelle Aparecida Martim Vicente;
- Glendha Santos de Souza.
