# 🧠 Projeto: User Manager (CRUD em Python - Terminal)

Este projeto consiste em um sistema de gerenciamento de usuários rodando no terminal, desenvolvido em Python puro. O objetivo foi praticar lógica de programação, organização de código e criação de validações reais — simulando o funcionamento básico de um back‑end.

---

## 📌 Funcionalidades implementadas

- Adicionar usuário
- Editar usuário
- Deletar usuário
- Listar usuários
- Menu interativo contínuo

Cada usuário possui:
- Nome
- Email
- Data de nascimento

---

## 🧱 Estruturas de programação aprendidas

### 1. Estruturas de dados

Uso de **lista + dicionário** para simular um banco de dados em memória:

```python
users = [
    {
        "name": "Livia",
        "email": "livia@email.com",
        "birthdate": "19/11/2003"
    }
]
```

Aprendizado:
- Como armazenar múltiplos registros
- Como percorrer registros
- Como atualizar informações específicas

---

### 2. Funções e reutilização (DRY)

Separação de responsabilidades:

- `nameValid()` → valida nome
- `validEmail()` → valida email
- `validBirthdate()` → valida data
- `addUser()` → cria usuário
- `editUser()` → altera dados
- `deleteUser()` → remove usuário
- `mainMenu()` → controla fluxo

Aprendizado:
- Evitar repetição de código
- Funções devem retornar valores
- Cada função deve ter apenas uma responsabilidade

---

### 3. Loops

Uso de `while True` para criar sistema contínuo:

```python
while True:
    option = input("Escolha uma opção: ")
```

Aprendizado:
- Criar aplicações interativas
- Controlar saída com `break`
- Repetir até entrada válida

---

### 4. Validação de dados

#### Validação de Nome
- Campo vazio
- Apenas números

#### Validação de Email
Regras implementadas manualmente:
- Deve conter `@`
- Apenas um `@`
- Deve conter domínio
- Domínio deve possuir `.`
- Não pode começar ou terminar com ponto

#### Validação de Data
Uso de `datetime.strptime()`:

```python
from datetime import datetime
```

Aprendizado:
- Tratamento de formato inválido
- Comparação de datas
- Impedir datas futuras

---

### 5. Tratamento de erros (try/except)

```python
try:
    date = datetime.strptime(birthdate, "%d/%m/%Y")
except ValueError:
    print("Formato inválido")
```

Aprendizado:
- Evitar quebra do programa
- Capturar erros do usuário
- Validar entrada sem travar aplicação

---

### 6. Manipulação de lista

Remover usuário:

```python
users.remove(user)
```

Editar usuário:

```python
user["name"] = novo_nome
```

Buscar usuário:

```python
for user in users:
    if user["email"] == email:
```

Aprendizado:
- Percorrer estruturas
- Alterar valores internos
- Identificar registros únicos

---

### 7. Fluxo de programa

Criação de um menu principal controlando toda a aplicação:

```
1 - Add user
2 - Edit user
3 - Delete user
4 - List users
5 - Exit
```

Aprendizado:
- Organização de sistema real
- Separação entre interface e lógica

---

## 🧠 Conceitos absorvidos

- CRUD (Create, Read, Update, Delete)
- Entrada e saída de dados
- Validação de input
- Tratamento de exceções
- Estruturação de projeto
- Funções com retorno
- Estruturas de dados mutáveis
- Controle de fluxo

---

## 🚀 Próximos passos possíveis

- Salvar usuários em arquivo JSON
- Impedir emails duplicados
- Calcular idade automaticamente
- Criar versão com interface gráfica
- Transformar em API (Flask/FastAPI)

---

## 🎯 Objetivo educacional

Esse projeto serviu como base prática para compreender como sistemas de cadastro funcionam internamente antes do uso de banco de dados ou frameworks.

Ele representa a fundação lógica de qualquer sistema back‑end real.

