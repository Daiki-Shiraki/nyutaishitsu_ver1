# -*- coding: utf-8 -*-
import requests
import json
import datetime
from LAB_SYSTEM import app

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
    url = "https://script.google.com/macros/s/AKfycbwbVNHmNbOYjjM012kdpWcNuR87HHjqEBkGxt3gnlvCzEKEC8DLMxDfytNbDooSMeTQbw/exec"
    response = requests.get(url)
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
