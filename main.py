import pywhatkit as kit
import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def send_emergency_alert(mensaje):
    hora_actual = datetime.datetime.now()
    hora_envio = hora_actual.hour
    minuto_envio = hora_actual.minute + 1  # Envía el mensaje 1 minuto después de la hora actual
    print(f"Enviando mensaje: {mensaje}")
        
        # Reemplaza el número de teléfono con el que deseas enviar el mensaje
    numero_destino = "+573224976097"

    kit.sendwhatmsg(numero_destino, mensaje, hora_envio, minuto_envio)

class Message(BaseModel):
    mensaje: str

@app.post("/")
def index(message: Message):
    send_emergency_alert(message.mensaje)
    return 'Mensaje enviado exitosamente'

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
#     uvicorn main:app --host 0.0.0.0 --port 10000
