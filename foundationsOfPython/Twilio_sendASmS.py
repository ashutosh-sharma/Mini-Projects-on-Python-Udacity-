from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8d53400abea926640dfea0a7829297f8"
# Your Auth Token from twilio.com/console
auth_token  = "ce883001d4019da26580135a990c51ae"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917015056768", 
    from_="+15415161927",
    body="Hello from Twilio & Python!")

print(message.sid)
