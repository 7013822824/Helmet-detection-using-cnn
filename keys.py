import smtplib

mail_sender = 'padavala.narendra66@gmail.com'
sender_app_password = 'efkr suyi zkvv kwdk'

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(mail_sender, sender_app_password)
    print("Login successful!")
    smtp.quit()
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: {e}")
except Exception as e:
    print(f"Error: {e}")