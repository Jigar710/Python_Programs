import smtplib

send_email = "testing.jigar@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	
	smtp.login(send_email,"testroot")
	
	subject = "Good morning"
	body = "I am Jigar shekhat. happy new year"
	
	msg = f"Subject: {subject}\n\n{body}"
	
	for i in range(500):
		smtp.sendmail(send_email,"shingarajiya123@gmail.com",msg)
	