#用于建立smtp
import smtplib
from email.mime.text import MIMEText

msg=MIMEText('心情很糟糕','plain',"utf-8")

msg['From']='1547331422@qq.com'
msg['To']='1547331422@qq.com'
msg['subject']='糟糕的一天'
smtp=smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('1547331422@qq.com','ujhbcvibmkuzgecg')
smtp.sendmail('1547331422@qq.com','1547331422@qq.com',msg.as_string())
smtp.quit()
