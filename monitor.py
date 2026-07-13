import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

receiver = EMAIL_USER

msg = MIMEText(
    "恭喜！你的 GitHub 云端监控程序已经成功运行。\n\n下一步我们将开始接入 IHG 和机票查询。",
    "plain",
    "utf-8"
)

msg["Subject"] = Header("日本旅行价格监控 - 测试成功", "utf-8")
msg["From"] = EMAIL_USER
msg["To"] = receiver

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(EMAIL_USER, EMAIL_PASS)
server.sendmail(EMAIL_USER, [receiver], msg.as_string())
server.quit()

print("Email sent successfully!")
