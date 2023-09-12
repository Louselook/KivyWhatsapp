import os

# Establecer una variable de entorno personalizada para evitar el error de DISPLAY
os.environ['DISPLAY'] = ":0"

# Ahora puedes importar pywhatkit sin problemas
import pywhatkit as kit
import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def send_emergency_alert(mensaje):
    from twilio.rest import Client

    account_sid = 'AC4088660cb6f697068fae1a53e2b9befb'
    auth_token = 'f1f51662d8b72e4940f87aa66d07dc0c'
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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
#     uvicorn main:app --host 0.0.0.0 --port 10000
