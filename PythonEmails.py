import smtplib
import getpass
import imaplib
import email
### to login to gmail you have to generate an app password that tells google that the app is authorized by you
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
### port 587 means that you are using tls encryption
smtp_object.ehlo()
smtp_object.starttls()
emailadd = getpass.getpass("What is your email address: ")
password = getpass.getpass('What is your password: ')
smtp_object.login(emailadd,password)
from_address = emailadd
to_address = emailadd
subject = input("Enter subject line: ")
message = input("Enter the email message: ")
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address, to_address,msg)
smtp_object.quit()

###     Receiving emails  ###
M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(emailadd,password)
M.list()
M.select('inbox')
typ, data = M.search(None, 'SUBJECT "This is a test"')
typ
data
email_id = data[0]
result,  email_data = M.fetch(email_id,'(RFC822)')
email_data
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
