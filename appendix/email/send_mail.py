# Sending Email via SMTP (part 1)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# inputs for from, to, subject and body text
fromaddr = input("Sender's email: ")
toaddr = input('To: ')
sub = input('Subject: ')
text = input('Body: ')

# email account info from where we'll be sending the email from
smtp_host = 'smtp.gmail.com'
smtp_port = 587
user = 'hermanmu@gmail.com'
password = "it's a secret - sorry"

# parts of the actual email
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = sub
msg.attach(MIMEText(text))

# connect to the server
server = smtplib.SMTP(smtp_host,smtp_port)

# initiate communication with server
server.ehlo()

# use encryption
server.starttls()

# login to the server
server.login(user, password)

# send the email
server.sendmail(fromaddr, toaddr, msg.as_string())

# close the connection
server.quit()
