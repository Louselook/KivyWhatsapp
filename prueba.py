from twilio.rest import Client

account_sid = 'AC4088660cb6f697068fae1a53e2b9befb'
auth_token = 'f1f51662d8b72e4940f87aa66d07dc0c'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',  # Número de WhatsApp que enviará el mensaje
    body='Este es un mensaje de prueba desde Twilio.',
    to='whatsapp:+573224976097'  # Reemplaza con el número de WhatsApp al que deseas enviar el mensaje
)

print(message.sid)