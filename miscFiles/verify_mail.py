import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def verify_link_mail(name, to_address, link):
    msg = MIMEMultipart()
    msg['From'] = "Hotel Fortune"
    msg['To'] = to_address
    msg['Subject'] = "Email Verification Mail"

    body = "Hey {}! Your verfication link is {}".format(name, link)

    msg.attach(MIMEText(body, "plain"))

    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("logout.me.world@gmail.com", "lostworld#121")
    server.sendmail("logout.me.world@gmail.com", to_address, text)
