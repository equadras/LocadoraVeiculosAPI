# API Lcadora de Veículos

# Set up
Primeiro, instale o packet manager do python com o comando
```bash
$ sudo apt install python3-pip
```
Depois instale as depencias do projeto da seguinte forma
```bash
$ pip install -r requirements.txt
```
Após instalar as depencias é necessário matar qualquer processo que esteja presente na porta 8080 do seu computador para poder rodar o servidor localmente
```bash
$ sudo lsof -i :8080
```
Caso após rodar o ```lsof -i :8080``` não listar nenhuma porta, signifca que nenhum processo está ocupando essa porta. 
Pegar o numero do processo e executar o comando abaixo com o número do processo. 
```bash
$ sudo kill 998244353
```
ou caso esteja em um ambiente windows
```bash
$ netstat -ano | findstr :8080
$ taskkill /PID 998244353 /F
```

então execute ```python3 app.py``` para rodar o servidor localmente e ter acesso às rotas http no seu navegador no endereço ```http://127.0.0.1:8080```


## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.
