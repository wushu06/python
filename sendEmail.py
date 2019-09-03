import smtplib


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

sender_email = "nourwushu@gmail.com"
password = 'Pawudr2004.'
server.login(sender_email, password)
server.sendmail('nourwushu@gmail.com', 'nourwushu@yahoo.fr', 'message')
