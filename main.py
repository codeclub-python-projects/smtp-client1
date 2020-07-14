from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import os

msg = MIMEMultipart()   # Объект почтового сообщения

# 1 - Почтовый акаунт отправителя:
# --------------------------------
login = 'itstep.codeclub@gmail.com'
with open('password.txt', 'r') as f:
    data = f.readline()
password = data

# 2 - Параметры почтового сообщения:
# ----------------------------------
msg['From'] = login
msg['To'] = input('Введите адрес получателя сообщения: ')
msg['Subject'] = input('Введите тему сообщения: ')
choice = int(input('Выберите формат сообщения (PlainText -> 1, HTML -> 2): '))
if choice == 1:
    message = input('Введите текст сообщения: ')
    msg.attach(MIMEText(message, 'plain'))
else:
    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                text-align: center;
            }
            h2 {
                color: purple;
            }
            a {
                text-decoration: none;
                font-size: 10pt;
            }
        </style>
    </head>
    <body>
        <h2>Красивое сообщение</h2>
        <hr>
        <main>
            <ol>
                <li><a href="https://www.ukr.net">Украинский информационный портал</a></li>
                <li><a href="https://www.bing.com">Поисковый сервис Microsoft</a></li>
                <li><a href="https://www.yahoo.com">Американский поисковый сервис</a></li>
            </ol>
        </main>
        <footer>
            <h4>Copyright &copy; MyCompany&trade; - Kyiv, 2020</h4>
        </footer>
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

# 3 - Вставка сообщения и прикрепленных файлов:
# ---------------------------------------------
with open('smile2.png', 'rb') as image:
    attachment = MIMEImage(image.read())
attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename('smile2.jpg'))
msg.attach(attachment)

# 4 - Процедура отправки сообщения:
# ---------------------------------
try:
    sender = smtplib.SMTP('smtp.gmail.com:587')
    sender.starttls()
    sender.login(login, password)
    sender.sendmail(msg['From'], msg['To'], msg.as_string())
    sender.quit()
    print('Ваше сообщение успешно отправлено')
except BaseException as err:
    print(err)
