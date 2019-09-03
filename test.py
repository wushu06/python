import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)
server.sendmail(
  "from@address.com", 
  "to@address.com", 
  "this message is from python")
server.quit()