import smtplib
from email.message import EmailMessage
from decouple import config


msg = EmailMessage()
msg["Subject"] = ""
msg["From"] = config("EMAIL_ADDRESS")
msg["To"] = ["raykipkorir@gmail.com"]


with open("email_template.html", "r") as f:
    content = f.read()

msg.add_alternative(content, subtype="html")

with open("cool.jpg", "rb") as f:
    file_data = f.read()
    file_name = f.name

#to attach an image
msg.add_attachment(file_data, maintype="image", subtype="jpg", filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(config("EMAIL_ADDRESS"), config("EMAIL_PASSWORD"))
    smtp.send_message(msg)
