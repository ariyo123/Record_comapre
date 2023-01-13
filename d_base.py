import os
from unittest import result
import csv
import datetime
import time
import mysql.connector as msql
from mysql.connector import Error

import smtplib,ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#from datetime import date, timedelta
import time
print("\n\n\n\n")
print("you're about to see the status of your webservices")
#get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#get cureent date
CurrentDate=datetime.date.today()  
days = datetime.timedelta(30)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date) 
CurrentDate1=datetime.date.today()  
days1 = datetime.timedelta(0)

new_date1 = CurrentDate1 - days1
final_date1= new_date1.strftime('%Y-%m-%d')
print(final_date1)


path1='C:/python_work/bvn_user_actitities/bank_code.csv'
with open(path1, 'r') as file_object:
    lines=file_object.read()
        #print(lines)
    contents1=lines.split()
    #print(contents1)

institutions_list=[*csv.DictReader(open('BANK_TABLE.csv'))]; #print(institutions_list)


#calling the webservices dictionary to confirm the status

for code in contents1[:]:
    for institutions in institutions_list[:]:
        #print(institutions)
        if institutions['bankCode']==f'{code}':
            bankCode=institutions['bankCode']
            bankName=institutions['bankName']
            dest=institutions['dest']
            #print(bankCode)
            #print(bankName)
            #print(dest)
            # Directory
            directory = bankName

            # Parent Directory path
            parent_dir = f"{dest}"
            # Path
            path = os.path.join(parent_dir, directory)
            #print(path)

            # Create the directory
            # 'GeeksForGeeks' in
            # '/home / User / Documents'
            #os.mkdir(path)
            #print(f"Directory {bankName} created")
            #pass
            # textfile = open(f"{path}/{bankName}.txt", "a")
            # textfile.write('ID,ACTION,IPADDRESS,ACTIONDATE,EMAIL,BANKCODE,DETAILS,ITEMSEARCHCOUNT,AUDITTYPE\n')
            conn = msql.connect(host='127.0.0.1', database='housing_data', user='', password='')
  
            # get cursor object
            cursor= conn.cursor()
            sql=f"SELECT * FROM housing_data.useractivity where BANKCODE = '{bankCode}' and ACTIONDATE between '{final_date} 00:00:00' and '{final_date1} 23:59:59';"

            # execute your query
            cursor.execute(sql)
            
            # fetch all the matching rows 
            result = cursor.fetchall()
