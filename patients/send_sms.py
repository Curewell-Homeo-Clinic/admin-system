from twilio.rest import Client
from decouple import config


def send_sms(self, phone_no, body):
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=body,
                                     from_=config('TWILIO_PHONE_NUMBER'),
                                     to=f'whatsapp:+91{phone_no}')
    return message.sid
