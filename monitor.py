import os
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# 读取配置文件
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

flight = config["flight"]
hotels = config["hotels"]

body = f"""日本旅行监控已启动

【机票】

去程：
{flight["depart_date"]} {flight["depart_flight"]}

回程：
{flight["return_date"]} {flight["return_flight"]}

提醒价格：
¥{flight["alert_price"]}

====================

【酒店】

"""

for hotel in hotels:
    body += f"""
{hotel["name"]}

入住：{hotel["checkin"]}
离店：{hotel["checkout"]}

提醒积分：
{hotel["alert_points"]}

--------------------
"""

msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = Header("日本旅行监控配置读取成功", "utf-8")
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_USER

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(EMAIL_USER, EMAIL_PASS)
server.sendmail(EMAIL_USER, [EMAIL_USER], msg.as_string())
server.quit()

print("Configuration loaded successfully.")
