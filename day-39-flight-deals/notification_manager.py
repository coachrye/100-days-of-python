from twilio.rest import Client

TWILIO_SID = "AC7115bff990fa73314af08fc29b00b7ea"
TWILIO_AUTH_TOKEN = "d91e21ebb42396eed12888ee7a393643"
TWILIO_VIRTUAL_NUMBER = "+18566175895"
TWILIO_VERIFIED_NUMBER = "+639062075201"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


