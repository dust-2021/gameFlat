import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from apCelery.config import Config


def send_email(mail_text: str, target: str, mail_type: str = 'plain'):
    smtp = smtplib.SMTP()
    smtp.connect(Config.SMTP_SERVER_HOST, Config.SMTP_SERVER_PORT)
    smtp.login(Config.SMTP_EMAIL_ADDRESS, Config.SMTP_EMAIL_PASSWORD)

    message = MIMEText(mail_text, mail_type, 'utf-8')
    message['From'] = Header('admin', 'utf-8')
    message['To'] = Header('webUser', 'utf-8')
    message['Subject'] = Header('web user register', 'utf-8')

    smtp.sendmail(from_addr=Config.SMTP_EMAIL_ADDRESS, to_addrs=target, msg=message.as_string())
