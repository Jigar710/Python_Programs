import smtplib

send_email = "testing.jigar@gmail.com"

with smtplib.SMTP("localhost",1025) as smtp:
	subject = "Good morning"
	body = "Hello there"
	
	msg = f"Subject: {subject}\n\n{body}"
	
	smtp.sendmail(send_email,"testing.jigar@gmail.com",msg)
	