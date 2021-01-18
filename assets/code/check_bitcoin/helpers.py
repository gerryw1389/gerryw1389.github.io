
import logging
import logging.handlers
from datetime import datetime
import sys
import os
import smtplib
from email.mime.text import MIMEText

def send_email(user, password, to):

    text = 'Records indicate this fund is on decline for the last 3 days'

    html = """\
    <html>
    <head>
    </head>
        <body>
        <p style="color:#006400"><b>{}</b></p>
        </body>
    </html>
    """.format(text)
    msg = MIMEText(html, 'html')
    msg['Subject'] = 'Buy Bitcoin'

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(user, password)
    mailserver.sendmail(user, to, msg.as_string())
    mailserver.quit()
    return "completed"

def load_logging():

    # create path to log file, create logs dir if it doesn't exist
    current_path = os.path.dirname(os.path.realpath(__file__))

    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    logname = "check_bitcoin_" + date + ".log"
    
    log_filename = f"{current_path}/logs/{logname}"

    if not os.path.exists(f"{current_path}/logs"):
        os.makedirs(f"{current_path}/logs")

    # import base logging module
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    # add handler
    handler = logging.handlers.RotatingFileHandler(
        log_filename, maxBytes=(1048576*5), backupCount=7
    )

    # set formatting
    formatter = logging.Formatter("%(asctime)s => %(levelname)s : %(message)s", datefmt='%Y-%m-%d %I:%M:%S %p')
    handler.setFormatter(formatter)

    # apply handler to default logger
    logger.addHandler(handler)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    return None