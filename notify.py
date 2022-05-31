from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from config import config


user=config["notify-sender"]
pwd=config["pwd"]
from log import eventLogger


def emailNotify(reciever,sendText="your event has been triggered once"):
    if reciever is not None:
        message=MIMEText(sendText,'plain','utf-8')
        message['Subject']=Header("gpu-monitor notification","utf-8")
        message['From']=Header("Cheny-Server","utf-8")
        message['To']=Header("Client","utf-8")
        try:
            smtpObj=SMTP_SSL('smtp.qq.com',465)
            smtpObj.login(user,pwd)
            smtpObj.sendmail(user,reciever,message.as_string())
            smtpObj.close()
            eventLogger.info("send notification for event  success")
        except Exception as e:
            eventLogger.info("send notification for event failed for reason {}".format(e))