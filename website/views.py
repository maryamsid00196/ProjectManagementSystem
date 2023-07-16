from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as sql
from urllib import request
from django import forms
from django.shortcuts import redirect
from django.db import connection
#PROJECT
project_id=''
name=''
description=''
cost=''
size=''
time_period=''
assigner=''
files=''
#PROJECT HEAD

NAME =''
EMAIL_ADDRESS=''
TELEPHONE=''
QUALIFICATION =''
PROJECTHEAD_ID=''
password=''
EMP_ID=''
CLIENT_ID=''





def projectPH(request):
    global name, description, cost,time_period,assigner,files,project_id,PROJECTHEAD_ID,EMP_ID,CLIENT_ID
    if request.method =='POST':
        db= sql.connect(host="localhost",user="root",passwd="Ms03325333940",database="pms")
        cursor=db.cursor()
        data= request.POST
        for key,value in data.items():
          if key=="project_id":
            project_id=value
          if key=="name":
            name=value
          if key=="description":
            description=value
          if key=="cost":
            cost=value
          if key=="time_period":
            time_period=value
          if key=="PROJECTHEAD_ID":
            PROJECTHEAD_ID=value
          if key=="EMP_ID":
            EMP_ID=value
          if key=="CLIENT_ID":
            CLIENT_ID=value
        c="insert into project Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(project_id, name, description, cost, time_period, PROJECTHEAD_ID, CLIENT_ID, EMP_ID)
        cursor.execute(c)
        db.commit()
    return render(request,'projectPH.html')

def allenteries(request):
  return render(request,'allenteries.html')

def Project_Head(request):
    global NAME, EMAIL_ADDRESS ,TELEPHONE ,QUALIFICATION ,PROJECTHEAD_ID
    if request.method =='POST':
        db= sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
        cursor=db.cursor()
        data= request.POST
        for key,value in data.items():
          if key=="PROJECTHEAD_ID":
            PROJECTHEAD_ID=value
          if key=="NAME":
            NAME=value
          if key=="QUALIFICATION":
            QUALIFICATION=value
          if key=="EMAIL_ADDRESS":
            EMAIL_ADDRESS=value
          if key=="password":
            password=value
        c="insert into project_head Values('{}','{}','{}','{}','{}')".format(NAME, EMAIL_ADDRESS  ,QUALIFICATION ,PROJECTHEAD_ID,password)
        cursor.execute(c)
        db.commit()
        return render(request,"PHlogin.html")
    return render(request,'Project_Head.html')

def Assigner(request):
    global NAME, EMAIL_ADDRESS ,EMP_ID,password
    if request.method =='POST':
        db= sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
        cursor=db.cursor()
        data= request.POST
        for key,value in data.items():
          if key=="EMP_ID":
            EMP_ID=value
          if key=="NAME":
            NAME=value
          if key=="EMAIL_ADDRESS":
            EMAIL_ADDRESS=value
          if key=="password":
            password=value
        c="insert into assigner Values('{}','{}','{}','{}')".format(NAME,EMAIL_ADDRESS,EMP_ID,password)
        cursor.execute(c)
        db.commit()
        return render(request,'Alogin.html')
    return render(request,'Assigner.html')
  

def Assignee(request):
  return render(request,'Assignee.html')

def manager(request):
  return render(request,'manager.html')

def developer(request):
  return render(request,'developer.html')

def designer(request):
  return render(request,'designer.html')

def tester(request):
  return render(request,'tester.html')
  

def client(request):
    global NAME, EMAIL_ADDRESS ,CLIENT_ID,password
    if request.method =='POST':
        db= sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
        cursor=db.cursor()
        data= request.POST
        for key,value in data.items():
          if key=="CLIENT_ID":
            CLIENT_ID=value
          if key=="NAME":
            NAME=value
          if key=="EMAIL_ADDRESS":
            EMAIL_ADDRESS=value
          if key=="password":
            password=value
        c="insert into client Values('{}','{}','{}','{}')".format(NAME,EMAIL_ADDRESS,CLIENT_ID,password)
        cursor.execute(c)
        db.commit()
        return render(request,'Clogin.html')
    return render(request,'client.html')


def index(request):
  return render(request,'index.html')

def PHlogin(request):
    global PROJECTHEAD_ID,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="PROJECTHEAD_ID":
                PROJECTHEAD_ID=value
            if key=="password":
                password=value
        c="select * from project_head where PROJECTHEAD_ID='{}' and password='{}'".format(PROJECTHEAD_ID,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
      
        if t==():
            return render(request,'error.html')
        else:

          if request.method=="POST":
              m=sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
              cursor=m.cursor()
              d=request.POST
              for key,value in d.items():
                  if key=="project_ID":
                     project_ID=1
              c="select * from project where project_ID=1".format(project_id=1)
              cursor.execute(c)
              t=tuple(cursor.fetchall())
        
              if t==():
                return render(request,'error.html')
              else:
                return render(request,"PHpage.html")
    return render(request,'PHlogin.html')

def Clogin(request):
    global CLIENT_ID,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="CLIENT_ID":
                CLIENT_ID=value
            if key=="password":
                password=value
        c="select * from client where CLIENT_ID='{}' and password='{}'".format(CLIENT_ID,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"Cpage.html")
    return render(request,'Clogin.html')

def Alogin(request):
    global EMP_ID,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="EMP_ID":
                EMP_ID=value
            if key=="password":
                password=value
        c="select * from assigner where EMP_ID='{}' and password='{}'".format(EMP_ID,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"Apage.html")
    return render(request,'Alogin.html')

def PHpage(self):
    
    m=sql.connect(host="localhost",user="root",password="Ms03325333940",database="pms")
    cursor=m.cursor()
    with connection.cursor() as cursor:
    
      cursor.execute("select * from pms.project where project_ID=1")
      t=tuple(cursor.fetchall())
        
    if t==():
            return render(request,'error.html')
    return render(request,'PHpage.html')








