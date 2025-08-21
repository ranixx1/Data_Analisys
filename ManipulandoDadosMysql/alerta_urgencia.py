import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import pandas as pd
from datetime import date

# Importa a mesma função de conexão que criamos no dashboard
# (Supondo que está em um arquivo chamado 'database.py' ou podemos copiar aqui)
from test import get_connection, fetch_data # Reutilizando o que já fizemos!

def enviar_alerta_email(lista_chamados):
    """Envia um e-mail de alerta com a lista de chamados urgentes."""

    # Carrega as credenciais de e-mail do arquivo .env
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD") # IMPORTANTE: Usar senha de App
    EMAIL_TO = os.getenv("EMAIL_TO")

    if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_TO]):
        print("Credenciais de e-mail não encontradas no arquivo .env. Abortando.")
        return

    # Monta a mensagem do e-mail
    msg = EmailMessage()
    msg['Subject'] = f"Alerta: {len(lista_chamados)} Chamados Urgentes Abertos - {date.today().strftime('%d/%m/%Y')}"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_TO

    # Corpo do e-mail
    body = "Atenção,\n\nOs seguintes chamados com urgência 'alta' continuam abertos:\n\n"
    for index, chamado in lista_chamados.iterrows():
        body += f"- ID: {chamado['id']}, Assunto: {chamado['assunto']}, Setor: {chamado['setor']}\n"
    body += "\nPor favor, tomar as ações necessárias.\n"

    msg.set_content(body)

    # Envia o e-mail usando o servidor SMTP do Gmail
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"E-mail de alerta enviado com sucesso para {EMAIL_TO}")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")

def verificar_chamados_urgentes():
    """Verifica o banco por chamados urgentes e abertos."""
    print("Iniciando verificação de chamados urgentes...")
    query = "SELECT id, setor, assunto FROM App_chamado WHERE urgencia = 'alta' AND status = 'aberto'"
    df_urgentes = fetch_data(query)

    if not df_urgentes.empty:
        print(f"Encontrados {len(df_urgentes)} chamados urgentes.")
        enviar_alerta_email(df_urgentes)
    else:
        print("Nenhum chamado urgente aberto encontrado. Nenhuma ação necessária.")


if __name__ == "__main__":
    load_dotenv()
    verificar_chamados_urgentes()