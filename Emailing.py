#https://www.codegrepper.com/code-examples/python/send+email+python+without+authentication

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("email.address", "email password")
server.sendmail(
  "the sender addr",
  "reciever's addr",
  "Message to be sent")
server.quit()