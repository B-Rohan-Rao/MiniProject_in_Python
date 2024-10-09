from twilio.rest import Client

# Uncomment the following 2 lines and add your details-->
# ACCOUNT_SID = "YOUR_ACCOUNT_SID"
# AUTH_TOKEN = "YOUR_ACCOUNT_TOKEN"

class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters: message_body (str): The text content of the SMS message to be sent.
        Returns: None
        """
        try:
            message = self.client.messages.create(
                from_="+15109014405",
                body=message_body,
                to="+91 95088 84063"
            )
            print(f"Message sent successfully with SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")