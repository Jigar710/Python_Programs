import smtplib
from email.message import EmailMessage
import imghdr

send_email = "py.testing.python@gmail.com"

msg = EmailMessage()
msg['Subject'] = "Good morning"
msg['From'] = send_email 
msg['To'] = "py.testing.python@gmail.com"
msg.set_content("This is demo image python program...")

with open('java.png','rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)
	file_name = f.name
	#print(file_type)

msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	smtp.login(send_email,"py123python")
	smtp.send_message(msg)
