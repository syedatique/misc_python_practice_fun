import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
from email.utils import COMMASPACE, formatdate, formataddr


def send_email(send_from=None, send_to=[], subject=None, username=None , password=None, text=None, files=None, servername=None):
    
    assert isinstance(send_to, list)
    username = "syed.atique@eurekasolutions.co.uk"
    send_from = "syed.atique@eurekasolutions.co.uk"
    send_to = ["syed.atique@gmail.com"]
    subject = "Testing my function"
    password = getpass.getpass("%s's password: " % username) #Promt for password
    text = "Email with attachment"
    html = """\
        <html>
          <head></head>
          <body>
            <p>
               %s
            </p>
          </body>
        </html>
        """ % text
    servername = "smtp.office365.com"


    # Create the message
    msg = MIMEMultipart()
    # msg['To'] = email.utils.formataddr(('Recipient', to_email))
    msg['From'] = formataddr(('Syed Atique', send_from))
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # msg.attach(MIMEText(text))
    msg.attach(MIMEText(html, 'html'))

    files = ["/Users/syedatique/Dropbox/store data locally.docx"]

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    # server operation
    server = smtplib.SMTP(servername)
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        server.set_debuglevel(True)
        # identify ourselves, prompting server for supported features
        server.ehlo()
        # If we can encrypt this session, do it
        if server.has_extn('STARTTLS'):
            server.starttls()
            server.ehlo() # re-identify ourselves over TLS connection

        server.login(username, password)
        server.sendmail(send_from, send_to, msg.as_string())
    finally:
        server.quit()


# send_email(files=["prime.py"])

def main():
    a = "/Users/syedatique/Dropbox/store data locally.docx"
    send_email(files=[a])

if __name__ == "__main__":
    main()

