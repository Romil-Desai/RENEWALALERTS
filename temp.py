# import pandas as pd
#
# frame=pd.read_excel("MAXLIFE.xlsx")
# print(frame.index)
# print(dict(frame.iloc[0]))
# dictionary=dict(frame.iloc[0])
# # for j in frame.index:
# #     dictionary=dict(frame.iloc[j])
# for i in dictionary.keys():
#     print(type(dictionary[i]))


# import tkinter as tk #import Tkinter as tk #change to commented for python2
#
# root = tk.Tk()
# root.title("ROOT")
# extra = tk.Toplevel()
# label = tk.Label(extra, text="extra window")
# label.pack()
#
# lower_button = tk.Button(root,
#                          text="lower this window",
#                          command=root.lower)
# lower_button.pack()
#
# root.mainloop()
# import datetime
# string="2020/08/05"
# date=datetime.date(int(string[:4]),int(string[5:7]),int(string[8:]))
# print(date)
# import sqlite3
#
# conn = sqlite3.connect("LIFEINSURANCE.sqlite")
# cursor = conn.cursor()
# print(cursor.execute("SELECT EMAIL , CONTACT_NO ,ADDRESS , NOMINEE , POLICY_STATUS , POLICY_NAME,PREMIUM_AMOUNT , SUM_ASSURED , POLICY_TERM , PREMIUM_PAYING_TERM ,PAYMENT_MODE , FIRST_YEAR_COMMISSION_PERCENT , RENEWAL_COMMISSION_FOR_2_3_YEAR_PERCENT ,RENEWAL_COMMISSION_FOR_4_5_YEAR_PERCENT , RENEWAL_COMMISSION_FOR_6_YEAR_ONWARDS_PERCENT ,GST_ON_FIRST_YEAR_COMMISSION , GST_ON_RENEWAL_COMMISSION  FROM LIFEINSURANCE WHERE POLICY_NUMBER = ?",
#                      ("32650217",)).fetchone())
# cursor.close()
# # conn.close()
# label_name = Label(next, text="Name", padx=10, pady=5, width=20, font="Courier")
# label_name.grid(row=0, column=0)
# button_submit = Button(next, text="Submit", command=submit, width=10, font="Courier")
# button_submit.grid(row=7, column=2)
#
# import tkinter
# from tkinter import filedialog
# mainwindow=tkinter.Tk()
# mainwindow.title("temp")
# mainwindow.geometry("700x400")
# label=tkinter.Label(mainwindow,text="SELECT THE FILE YOU WANT TO UPLOAD",padx=5,pady=10,width=40,font="Courier")
# label.grid(row=0,column=0,columnspan=2)
# def filepath():
#     path=filedialog.askopenfilename(initialdir="C:\\Users\\ROMIL\\Desktop",title="Select an excel file",filetypes=(("Excel Workbook (*.xlsx)","*.xlsx"),("all files","*.*")))
#     print(path)
#     filepath=path
#     print(filepath)
#
# button=tkinter.Button(mainwindow,text="import",command=filepath,pady=5)
# button.grid(row=0,column=2,sticky="w")
# mainwindow.mainloop()
# import datetime
# datetime_str = '2020-07-06 00:00:00'
# issue_datetime_str = '2020-07-06 00:00:00'
# datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
# issue_datetime_object = datetime.datetime.strptime(issue_datetime_str, '%Y-%m-%d %H:%M:%S')
# print(datetime_object)
# print(type(datetime_object))
# print(issue_datetime_object)
# print(type(issue_datetime_object))

# importing all files from tkinter
# from tkinter import *
# from tkinter import filedialog
#
# # import only asksaveasfile from filedialog
# # which is used to save file in any extension
# from tkinter.filedialog import asksaveasfile
#
# root = Tk()
# root.geometry('200x150')
#
# # function to call when user press
# # the save button, a filedialog will
# # open and ask to save file
# def save():
#     filename=filedialog.asksaveasfilename(initialdir="C:\\Users\\ROMIL\\Desktop\\*.xlsx", title="Select an excel file",defaultextension=".xlsx",
#                                           filetypes=(("Excel Workbook (*.xlsx)", "*.xlsx"), ("all files", "*.*")))
#     print(filename)
#
# btn = Button(root, text = 'Save', command = save)
# btn.pack(side = TOP, pady = 20)
#
# mainloop()
import sys
# import tkinter
# from datetime import datetime

import matplotlib.pyplot as plt
import smtplib
#!/usr/bin/python
# import smtplib
#
# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login('romildesai4@gmail.com',"romildesai4@gmail.com")
#     subject="TEST"
#     body="HOPE IT RUNS"
#     msg=f'Subject:{subject} \n\n {body}'
# #     smtp.sendmail('romildesai4@gmail.com','romildesai4@gmail.com',msg)
# import shelve
# s=shelve.open("login_details.shelve")
# email_id=s["EMAIL"]
# password=s["PASSWORD"]
# print(email_id,password)
import sqlite3
# conn=sqlite3.connect("LIFEINSURANCE.sqlite")
# cursor=conn.cursor()
# entry = None
# cursor = conn.cursor()
#
# print(cursor.execute(
#     "SELECT RENEWAL_DATE,POLICY_NUMBER FROM LIFEINSURANC ").fetchall())
# entry = cursor.execute(
#     "SELECT RENEWAL_DATE,POLICY_NUMBER FROM LIFEINSURANC ", ).fetchall()
# policy_number_list=[]
# import datetime
# print( datetime.datetime.strftime(datetime.date.today()+datetime.timedelta(days=33),"%Y-%m-%d") == datetime.datetime.strftime(datetime.datetime(2020,9,11),"%Y-%m-%d"))
#
#
# import socket
#
# # def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
# #     try:
# #         socket.setdefaulttimeout(timeout)
# #         socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
# #         return True
# #     except socket.error as ex:
# #         print(ex)
# #         return False
#
#
# # window=tkinter.Tk()
# # window.geometry("600x300")
# # window.title("NO INTERNET CONNECTION")
# # tkinter.Label(window,text="ALERTS WEREN'T CHECKED",font="Courier").grid(row=0,column=0)
# # tkinter.Label(window,text="CONNECT TO THE INTERNET AND TRY AGAIN",font="Courier").grid(row=1,column=0)
# # tkinter.Button(window,text="TRY AGAIN",font="Courier").grid(row=2,column=0)
# # tkinter.Button(window,text="EXIT",font="Courier",command=sys.exit).grid(row=3,column=0)
# # window.mainloop()
# import datetime
# print((datetime.datetime(2020,12,4)-datetime.timedelta(days=365)+datetime.timedelta(days=15)));



