## Instruções para rodar no Windows

> É necessário ter o Python instalado no computador.

<br/>

1. Criar um ambiente virtual.

```
python -m venv venv
```

2. Ativar o ambiente virtual.

```
.\venv\Scripts\Activate.ps1
```

3. Instalar as libs necessárias.

```
pip install -r requirements.txt
```

4. Gerar uma senha de email em "Senhas de App" nas [configurações da conta do Google](https://myaccount.google.com/apppasswords).

5. Salvar essa senha como uma variável chamada "password" no arquivo .env.

6. Rodar o arquivo main.py.

```
python .\main.py
```

<br/>

- Observação 1: Para o passo 4 funcionar, é preciso que a verificação em duas etapas esteja ativada na conta.

- Observação 2: Se der erro no passo 2, abrir o terminal do computador como administrador e rodar o comando:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
