from fastapi import FastAPI
from pydantic import BaseModel
import os  # Importa el módulo 'os' para acceder a las variables de entorno

app = FastAPI()

def send_emergency_alert(mensaje):
    from twilio.rest import Client

    # Lee las credenciales desde las variables de entorno
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    if not account_sid or not auth_token:
        raise ValueError("Las variables de entorno TWILIO_ACCOUNT_SID y TWILIO_AUTH_TOKEN no están configuradas correctamente.")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Número de WhatsApp que enviará el mensaje
        body=f'{mensaje}',
        to='whatsapp:+573224976097'  # Reemplaza con el número de WhatsApp al que deseas enviar el mensaje
    )

    print(message.sid)

class Message(BaseModel):
    mensaje: str

@app.post("/")
def index(message: Message):
    send_emergency_alert(message.mensaje)
    return 'Mensaje enviado exitosamente'

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
