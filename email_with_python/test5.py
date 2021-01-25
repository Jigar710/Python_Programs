import smtplib
from email.message import EmailMessage
import imghdr

send_email = "py.testing.python@gmail.com"

msg = EmailMessage()
msg['Subject'] = "Good morning"
msg['From'] = send_email 
msg['To'] = "py.testing.python@gmail.com"
msg.set_content("Hello there")

with open('java.png','rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)
	print(file_type)

'''
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	smtp.login(send_email,"py123python")
	smtp.send_message(msg)
'''