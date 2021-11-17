#https://www.codegrepper.com/code-examples/python/send+email+python+without+authentication

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("yehonatan.tsevaa@gmail.com", "k8i8k811")
server.sendmail(
  "yehonatan.tsevaa@gmail.com",
  "liad2015@gmail.com",
  "")
server.quit()