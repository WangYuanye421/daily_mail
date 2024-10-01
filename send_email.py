import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, '.env'))
mail_sender = os.getenv('mail_sender')
mail_pwd = os.getenv('mail_pwd')
smtp_server = os.getenv('smtp_server')
# 发送邮件的函数
def send_email(subject, body, to_email):
    server = None  # 初始化 server 变量为 None
    try:
        # 配置邮件服务器，这里以 SMTP 为例
        server = smtplib.SMTP(smtp_server, 25)  # 你需要根据实际邮件服务商配置
        server.ehlo()
        server.starttls()
        server.login(mail_sender, mail_pwd)
        # 构建邮件
        msg = MIMEText(body, "html")
        msg['From'] = mail_sender
        msg['To'] = to_email
        msg['Subject'] = subject
        # 发送邮件
        server.sendmail(mail_sender, to_email, msg.as_string())
        print(f"邮件已发送到 {to_email}")
    except Exception as e:
        print(f"发送邮件失败: {str(e)}")
    finally:
         # 确保无论发送是否成功，都会正确关闭连接
        if server:
            server.quit()

# send_email("标题", "正文", "546792341@qq.com")