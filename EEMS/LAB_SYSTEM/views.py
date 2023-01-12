# -*- coding: utf-8 -*-
from flask import Flask,abort,request,redirect,url_for,render_template,flash,session
from LAB_SYSTEM import app
from LAB_SYSTEM import getData
import os

@app.route('/')
def show_entries():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    getData.StudentList=[]
    getData.loadData()
    return render_template('entries/index.html',db=getData.StudentList)