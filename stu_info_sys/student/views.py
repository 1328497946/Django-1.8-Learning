from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import STUDENT
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_(message):
    smtp = "smtp.qq.com"
    sender = "2282310940@qq.com"
    receiver = "1328497946@qq.com"
    # pwd = ""
    pwd = 'vbddzghqiqhxdiej'
    title = "学生信息错误"
    contents = message

    try:
        message = MIMEText(contents, "plain", "utf-8")
        message['From'] = Header(sender, "utf-8")
        message['To'] = Header(receiver, "utf-8")
        message['Subject'] = Header(title, "utf-8")
        opt = smtplib.SMTP_SSL(smtp, 465)
        opt.login(sender, pwd)
        opt.sendmail(sender, receiver, message.as_string())
        opt.quit()
        print("邮件发送成功")
    except Exception as e:
        return e

'''
import sys
sys.path.append("..")
from stu_info_sys.settings import BASE_DIR 
'''

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST' and request.POST:
        userd = request.POST['user']
        password = request.POST['password']
        try:
            stud = STUDENT.objects.get(STUDENTID=userd)
        except (KeyError, STUDENT.DoesNotExist):
            return render(request, "login.html", {'ERROR': '账号不存在'})
        if stud.PASSWORD == password:
            return render(request, "info.html", {'stu': stud})
        else:
            return render(request, 'login.html', {'ERROR': '密码错误'})
    return render(request, "login.html")

def sender(request, stu_id):
    message = "学号" + str(stu_id) + "信息有错误请检查！"
    send_(message)
    return render(request, "jump.html")

def jiaowu(request):
    return render(request, "jiaowu.html")
# Create your views here.
