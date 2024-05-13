import logging
import smtplib
from email.mime.text import MIMEText
#支持附件
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config import *
def send_email(report_file):

    #读取report内容放到变量email-body
    with open(report_file,encoding='utf-8')as f:
     email_body=f.read()
# msg=MIMEText('心情很糟糕','plain',"utf-8")
    msg=MIMEMultipart()
    msg.attach(MIMEText(email_body,'html','utf-8'))
    msg['From']=sender
    msg['To']=receiver
    msg['subject']=Header(subject,'utf-8')

    att1=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att1["Content-Type"]='application/octet-stream'
    att1['Content-Disposition']='attachment; filename="result.html"'
    msg.attach(att1)
    try:


        smtp=smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_ps)
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info("============发送邮件成功============")
    except Exception as e:
        logging.error(str(e))
    finally:
      smtp.quit()
if __name__ == '__main__':
    send_email('report.html')
