# -*- coding: utf-8 -*-
import requests
import json
import datetime
from LAB_SYSTEM import app
import config

dt = datetime.datetime.today() 

# StudentGradeList=[]
# GradeTop3=[]
StudentList=[]
# M2=[]
# M1=[]
# U4=[]
# U4=[],M1=[]
class Student:
    def __init__(self,name,status,grade):
        self.name=name
        self.status=status
        self.grade=grade
def getData():
    response = requests.get(config.GetURL)
    return response.text

def getTime():
    t = dt.time()

def loadData():
    try:
        DB = json.loads(getData())
    except:
        json_open=open('error.json','r')
        DB=json.load(json_open)
    
    # for data in DB:
    #     StudentGradeList.append(data["grade"])
    for data in DB:
        StudentList.append(Student(data["name"],data["state"],data["grade"]))
    # for data in StudentList:
    #     print(data.status)

#for data in DB:
    #print(data["学籍番号"])

# print(DB)
# print(StudentList[1].name)
