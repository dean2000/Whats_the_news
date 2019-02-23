import smtplib 
import ssl
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import datetime

""" mail the news by connecting to a remote gmail account """

def send_mail(send_from, password, send_to, subject, text,
         files=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open((f), "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(send_from, password)
        server.sendmail(send_from, send_to, msg.as_string())
        server.quit()

#uses in order to get th due date file
date = datetime.datetime.now().strftime('%d-%m-%y')

#can accept multiple adresses in a list
send_mail("your_email@gmail.com", "email_password", ["target_email@gmail.com"]
	, "aptList_backup", "attachments",
	 files=[(f'/apps_installation/installation_file{date}.txt')])


