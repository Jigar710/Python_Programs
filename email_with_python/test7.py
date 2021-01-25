import smtplib
from email.message import EmailMessage

send_email = "py.testing.python@gmail.com"

to[] = ["py.testing.python@gmail.com","gisumit1@gmail.com"]

msg = EmailMessage()
msg['Subject'] = "Good morning"
msg['From'] = send_email 
msg['To'] = ", ".join(to)
msg.set_content("This is demo image python program...")

with open("APPLET.pdf","rb") as f:
	file_data = f.read()
	file_name = f.name

msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	smtp.login(send_email,"py123python")
	smtp.send_message(msg)
