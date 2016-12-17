#Inside the twilio folder import the contents of the rest folder
from twilio import rest

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

#Inside the rest
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hey i am sending = this using a Python script",
    to="",    # Replace with your phone number
    from_="") # Replace with your Twilio number

print(message.sid)
