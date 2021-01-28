import datetime
import os
import sqlite3
import sys
import tkinter

import pandas as pd
import numpy as np
import shelve



import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import socket

def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

def daily():
    todays_date=datetime.datetime.now()
    print(os.path.dirname(os.getcwd())+r"\GUI\LIFEINSURANCE.sqlite")
    conn=sqlite3.connect(os.path.dirname(os.getcwd())+r"\GUI\LIFEINSURANCE.sqlite")
    cursor=conn.cursor()
    entry = None
    cursor = conn.cursor()
    try:
        print(cursor.execute(
            "SELECT RENEWAL_DATE,POLICY_NUMBER FROM LIFEINSURANCE ").fetchall())
        entry = cursor.execute(
            "SELECT RENEWAL_DATE,POLICY_NUMBER FROM LIFEINSURANCE ", ).fetchall()
        policy_number_list=[]
    except sqlite3.OperationalError:
        return
    else:
        for selected_policy in entry:
            renewal_date = datetime.datetime.strptime(selected_policy[0], '%Y-%m-%d %H:%M:%S')
            if datetime.datetime.strftime(todays_date+datetime.timedelta(days=15),"%Y-%m-%d") == datetime.datetime.strftime(renewal_date,"%Y-%m-%d") or datetime.datetime.strftime(todays_date+datetime.timedelta(days=5),"%Y-%m-%d") == datetime.datetime.strftime(renewal_date,"%Y-%m-%d"):
                policy_number_list.append(selected_policy[1])
        print(policy_number_list)
        if policy_number_list == []:
            return
        else:
            entries=[]
            for policy_number in policy_number_list:
                statement = cursor.execute(
                    "SELECT RENEWAL_DATE,CUSTOMER_NAME,PREMIUM_AMOUNT,POLICY_NUMBER FROM LIFEINSURANCE WHERE POLICY_NUMBER = ?",
                    (policy_number,)).fetchone()
                entries.append(list(statement))
            dateframe = pd.DataFrame(np.array(entries),
                                     columns=["RENEWAL_DATE","CUSTOMER_NAME","PREMIUM_AMOUNT","POLICY_NUMBER"])
            print(dateframe)
            dateframe.to_csv("report.csv")
            with open("report.csv","rb") as f:
                f_data=f.read()
            s=shelve.open(os.path.dirname(os.getcwd())+r"\GUI\login_details.shelve")
            email_id=s["EMAIL"]
            password=s["PASSWORD"]
            s.close()
            emailfrom = email_id
            emailto = email_id
            fileToSend = "report.csv"
            password = password

            msg = MIMEMultipart()
            msg["From"] = emailfrom
            msg["To"] = emailto
            msg["Subject"] = "RENEWAL ALERTS"


            ctype, encoding = mimetypes.guess_type(fileToSend)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"

            maintype, subtype = ctype.split("/", 1)

            if maintype == "text":
                fp = open(fileToSend)
                # Note: we should handle calculating the charset
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "image":
                fp = open(fileToSend, "rb")
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "audio":
                fp = open(fileToSend, "rb")
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(fileToSend, "rb")
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
            msg.attach(attachment)
            if checkInternetSocket():
                server = smtplib.SMTP("smtp.gmail.com:587")
                server.starttls()
                server.login(email_id,password)
                server.sendmail(emailfrom, emailto, msg.as_string())
                server.quit()
                print("successful")
                sys.exit()
            else:
                window=tkinter.Tk()
                window.geometry("600x300")
                window.title("NO INTERNET CONNECTION")
                tkinter.Label(window,text="ALERTS WEREN'T CHECKED",font="Courier").grid(row=0,column=0)
                tkinter.Label(window,text="CONNECT TO THE INTERNET AND TRY AGAIN OR EXIT",font="Courier").grid(row=1,column=0)
                tkinter.Button(window,text="TRY AGAIN",font="Courier",command=daily).grid(row=2,column=0)
                tkinter.Button(window,text="EXIT",font="Courier",command=sys.exit).grid(row=3,column=0)
                window.mainloop()
daily()


