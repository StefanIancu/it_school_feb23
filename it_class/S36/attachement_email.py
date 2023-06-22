import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

EMAIL_PASS = "fshbrcqyywpavsbd"
EMAIL_USER = "pythontest.odyssey2001@gmail.com"
EMAIL_SERVER = "smtp.gmail.com"
EMAIL_SERVER_PORT = 465 # post smtp pentru conexiuni securizate


def send_welcome_email(user_email, user_name):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Your ticket at FlyHome"
    message["From"] = EMAIL_USER
    message["To"] = user_email

    html = f"""
    <html>
    <body>
        <h2>Hello {user_name}! You will find your boarding pass attached below.!</h2>
        <p>Hello from py code. This email is sent from a <b>Python</b> script.</p>
        <p>For any details regarding the reservation please email as at support@flyhome.com</p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    ticket_path = "/Users/stefantraianiancu/Desktop/it_school/final_project/tickets/planeticket_B111.pdf"

    with open(ticket_path, "rb") as fin:
        opened_file = fin.read()
    attached_file = MIMEApplication(opened_file, _subtype = "pdf")
    attached_file.add_header('content-disposition', 'attachment', filename = f"123")

    message.attach(attached_file)


    server = smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_SERVER_PORT)
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(
        EMAIL_USER,
        user_email,
        message.as_string()
    )

send_welcome_email("iancustefan28@yahoo.com", "Stefan")