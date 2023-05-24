import pandas as pd
import smtplib
import email.message
import os
from dotenv import load_dotenv
load_dotenv()

tabela_vendas = pd.read_excel("./Vendas.xlsx")

# FATURAMENTO POR LOJA
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()\
    .sort_values(by="Valor Final", ascending=False)

# QUANTIDADE DE PRODUTOS VENDIDOS POR LOJA
quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()\
    .sort_values(by="Quantidade", ascending=False)

# TICKET MÉDIO DOS PRODUTOS POR LOJA
ticket_medio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})


def enviar_email():
    mensagem = f"""
    <p>Prezado,</p>

    <p>Segue o relatório de vendas em cada loja.</p>

    <p>Faturamento:</p>
    {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

    <p>Quantidade vendida:</p>
    {quantidade.to_html()}

    <p>Ticket médio dos produtos em cada loja:</p>
    {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}
    """

    msg = email.message.Message()
    msg["Subject"] = "Relatório de Vendas"
    msg["From"] = "REMETENTE@gmail.com" # EDITAR EMAIL
    msg["To"] = "DESTINATARIO@gmail.com" # EDITAR EMAIL
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(mensagem)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()

    password = os.environ["password"]
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    print("Email enviado com sucesso!")


enviar_email()
