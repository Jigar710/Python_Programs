import smtplib
from email.message import EmailMessage

send_email = "py.testing.python@gmail.com"

msg = EmailMessage()
msg['Subject'] = "Good morning"
msg['From'] = send_email 
msg['To'] = "py.testing.python@gmail.com"
msg.set_content("This is demo image python program...")

msg.add_alternative("""
<!DOCTYPE HTML>
<html>
	<body>
		<h1 style="color:SlateGray;">Welcome to GI,Surat</h1>
	</body>
</html>
""",subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	smtp.login(send_email,"py123python")
	smtp.send_message(msg)