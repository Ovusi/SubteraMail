from textsbanners.banner import Banner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import socks

Banner()


class Sendmsg:
    msg = MIMEMultipart()

    print("""  \nType your correct email information and recipient address. 
Your message will be sent through a Proxy server to ensure Anonymity.""")

    msg['From'] = input("\n[*]Sender Address> ")
    password = input("[*] Password> ")
    msg['To'] = input("[*] Recipient Address> ")
    msg['Subject'] = input("[*] Subject> ")
    message = input("[*] Message> ")

    try:
        msg.attach(MIMEText(message, "Plain"))

        context = ssl.create_default_context()

        # set email to be sent through a proxy server
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "167.71.203.212", 1080)
        socks.wrapmodule(smtplib)

        # start smtp server and send email
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls(context)

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print("Sent Successfully")
        import subtera

    except Exception as e:
        print(e)
    if Exception:  # if error occurs, go back to options screen
        import subtera
        subtera.Subt()


Sendmsg()
