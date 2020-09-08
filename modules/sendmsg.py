from textsbanners.banner import Banner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socks

Banner()


class Sendmsg:
    msg = MIMEMultipart()

    print("""  \nType your correct email information and recipient address. 
Your message will be sent through a Proxy server to ensure Anonymity.""")

    msg['From'] = input("\n[*] Sender Address> ")
    password = input("[*] Password> ")
    msg['To'] = input("[*] Recipient Address> ")
    msg['Subject'] = input("[*] Subject> ")
    message = input("[*] Message> ")

    try:
        msg.attach(MIMEText(message, "Plain"))

        # set email to be sent through a proxy server
        proxy = "167.71.203.212"  # Replace with any proxy server and
        port = 1080  # port of your choice

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy, port)
        socks.wrapmodule(smtplib)

        # start smtp server and send email
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print("Sent Successfully")
        import subtera

    except Exception as e:
        print(e)
        pass
