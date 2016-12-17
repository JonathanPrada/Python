#Inside the twilio folder import the contents of the rest folder
from twilio import rest

account_sid = "AC301090ece2ede1d2b15c578b30f6c7d6" # Your Account SID from www.twilio.com/console
auth_token  = "6b67e93b54e9aa486d4b27961b6f05c7"  # Your Auth Token from www.twilio.com/console

#Inside the rest
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hey i am sending = this using a Python script",
    to="+447471502094",    # Replace with your phone number
    from_="+41798072569") # Replace with your Twilio number

print(message.sid)
