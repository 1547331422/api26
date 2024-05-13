import smtplib
from email.mime.text import MIMEText
from config.config import *
#支持附件
from email.mime.multipart import MIMEMultipart
from email.header import Header
#读取report内容放到变量email-body
with open('result.html',encoding='utf-8')as f:
    email_body=f.read()
# msg=MIMEText('心情很糟糕','plain',"utf-8")
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
msg['From']='1547331422@qq.com'
msg['To']='1547331422@qq.com'
msg['subject']='糟糕的一天'

att1=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
att1["Content-Type"]='application/octet-stream'
att1['Content-Disposition']='attachment; filename="result.html"'
msg.attach(att1)

smtp=smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('1547331422@qq.com','ujhbcvibmkuzgecg')
smtp.sendmail('1547331422@qq.com','1547331422@qq.com',msg.as_string())
smtp.quit()
