import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_PASS = "kagkribhousvpfzc"
EMAIL_USER = "stefantraian.iancu@gmail.com"
EMAIL_SERVER = "smtp.gmail.com"
EMAIL_SERVER_PORT = 465 # post smtp pentru conexiuni securizate


def send_welcome_email(user_email, user_name):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to IT School"
    message["From"] = EMAIL_USER
    message["To"] = user_email

    html = f"""
    <html>
    <body>
        <h2>Hello {user_name}! Welcome to IT School!</h2>
        <p>Hello from py code. This email is sent from a <b>Python</b> script.</p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)


    server = smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_SERVER_PORT)
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(
        EMAIL_USER,
        user_email,
        message.as_string()
    )

send_welcome_email("iancustefan28@yahoo.com", "Stefan Iancu")