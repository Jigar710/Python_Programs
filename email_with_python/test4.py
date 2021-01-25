import smtplib
from email.message import EmailMessage

send_email = "py.testing.python@gmail.com"

msg = EmailMessage()
msg['Subject'] = "Good morning"
msg['From'] = send_email 
msg['To'] = "py.testing.python@gmail.com"
msg.set_content("Hello there")

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	smtp.login(send_email,"py123python")
	smtp.send_message(msg)
	