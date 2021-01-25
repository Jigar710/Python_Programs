import smtplib

send_email = "testing.jigar@gmail.com"

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	
	smtp.login(send_email,"testroot")
	
	subject = "Good morning"
	body = "Hello there"
	
	msg = f"Subject: {subject}\n\n{body}"
	smtp.sendmail(send_email,"testing.jigar@gmail.com",msg)
	