# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:02:06 2019

@author: user
"""

from tkinter import *
import numpy as np  
import pandas as pd
import os  
from tkinter import messagebox 
def Login():
    
    global nameEL
    global pwordEL
    global rootA
    
    rootA =Tk()
    rootA.title('STATISTICAL TOOL ')
    rootA.geometry("500x500+300+120")
    
    instruction = Label(rootA,text='ENTER YOUR ID')
    instruction.grid(row=0,sticky=E)
    
    nameL =Label(rootA,text='ID: ')
    
    nameL.grid(row=1,column=0,sticky=W)
    
    
    nameEL=Entry(rootA)
    
    nameEL.grid(row=1,column=1)
   
    
    loginB=Button(rootA,text='PLOT',command=pre)
    loginB.grid(row=3,column=0,sticky=W)

    

    rootA.mainloop()
def pre():
    


	import pandas as pd  
	import numpy as np  
	import matplotlib.pyplot as plt  
	import time
	import datetime as dt
	import tkinter as tk
	from pandas import DataFrame
	from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    
	search=str(nameEL.get())
    
	filename="C:\\Users\\user\\Desktop\\nig\IAttendance\\Attendance_"+search+".csv"
	#for the no. of entries
	s = pd.read_csv(filename)
	s['Date']=pd.to_datetime(s.Date)
	df1 = DataFrame(s, columns= ['Date', 'Time'])
	df1.dropna(inplace=True)
	df1['Time'] = df1['Time'].apply(lambda x: time.strftime('%H:%M', time.strptime(x, '%H:%M:%S')))
	df1.drop_duplicates(['Date','Time'],inplace=True)
	f1 = df1[['Date', 'Time']].groupby('Date').Date.count()
	#upto here figure1
   
    #for the no. of exit
	filename1="C:\\Users\\user\\Desktop\\nig\\OAttendance\\Attendance_"+search+".csv"
	t = pd.read_csv(filename1)
	t['Date']=pd.to_datetime(t.Date)
	df2 = DataFrame(t, columns= ['Date', 'Time'])
	df2.dropna(inplace=True)
	df2['Time'] = df2['Time'].apply(lambda x: time.strftime('%H:%M', time.strptime(x, '%H:%M:%S')))
	df2.drop_duplicates(['Date','Time'],inplace=True)
	f2 = df2[['Date', 'Time']].groupby('Date').Date.count()
    
    #upto here figure2
    
    
    #fro total time
	s = pd.read_csv(filename)
	s['Date']=pd.to_datetime(s.Date)
	df1 = DataFrame(s, columns= ['Date', 'Time'])
	df1.dropna(inplace=True)
	df1['Time'] = df1['Time'].apply(lambda x: time.strftime('%H:%M', time.strptime(x, '%H:%M:%S')))
	df1['Time'] = df1['Time'].apply(lambda x: time.strftime('%H:%M:%S', time.strptime(x, '%H:%M')))
	df1.drop_duplicates(['Date','Time'],inplace=True)
	df1['Time']=pd.to_timedelta(df1.Time)
	a = df1[['Date', 'Time']].groupby('Date').Time.sum().reset_index()
	t = pd.read_csv(filename1)
	t['Date']=pd.to_datetime(t.Date)
	df2 = DataFrame(t, columns= ['Date', 'Time'])
	df2.dropna(inplace=True)
	df2['Time'] = df2['Time'].apply(lambda x: time.strftime('%H:%M', time.strptime(x, '%H:%M:%S')))
	df2['Time'] = df2['Time'].apply(lambda x: time.strftime('%H:%M:%S', time.strptime(x, '%H:%M')))
	df2.drop_duplicates(['Date','Time'],inplace=True)
	df2['Time']=pd.to_timedelta(df2.Time)
	b= df2[['Date', 'Time']].groupby('Date').Time.sum().reset_index()
	q=pd.concat([a['Date'],a['Time'], b['Time']], axis=1, keys=['Date','INTIME', 'OUTTIME'])
	q['INTIME']=pd.to_timedelta(q.INTIME)
	q['OUTTIME']=pd.to_timedelta(q.OUTTIME)
	#q['RESULT'] = q['INTIME'] -q['OUTTIME']
	q['RESULT'] = q['OUTTIME']-q['INTIME']
	q['Date']=pd.to_datetime(q.Date)
	q['RESULT']=pd.to_datetime(q.RESULT)
	q['RESULT'] = q['RESULT'].dt.strftime('%H:%M:%S')
	q['RESULT'] = pd.to_datetime(q['RESULT'], format='%H:%M:%S' ).apply(pd.Timestamp)
	q['Total_Time']=q['RESULT'].dt.hour
	#r=DataFrame(q,columns=['ho','Date'])
    
    #UPTO HERE FOR FIGURE3
    
    
	root= tk.Tk()
	root.title('PLOTS')

	figure1 = plt.Figure(figsize=(5,4), dpi=100)
	ax1 = figure1.add_subplot(111)
	line1 = FigureCanvasTkAgg(figure1, root)
	line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	f1.plot(kind='line', legend=True, ax=ax1, color='b',marker='o', fontsize=10)
	p1=ax1.set_title('NUMER OF ENTRIES Vs. DATE')
    
    
	figure2 = plt.Figure(figsize=(5,4), dpi=100)
	ax2 = figure2.add_subplot(111)
	line2 = FigureCanvasTkAgg(figure2, root)
	line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	f2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
	p2=ax2.set_title('NUMER OF EXITS Vs. DATE')
    
	figure3 = plt.Figure(figsize=(6,5), dpi=100)
	ax3 = figure3.add_subplot(111)
	bar1 = FigureCanvasTkAgg(figure3, root)
	bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	q.Total_Time.plot(kind='bar', legend=True, ax=ax3)
	p3=ax3.set_title('TOTAL TIME SPENT  Vs. DATE')
	
	#dButton=Button(root,text='DOWNLOAD',command=pre)
	#dButton.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	rootB =Tk()
	rootB.title('DOWNLOAD MENU')
	rootB.eval('tk::PlaceWindow %s center' %rootB.winfo_toplevel())
	rootB.withdraw()
	pp=messagebox.askyesno('DOWNLOAD ','DO YOU WANT TO DOWNLOAD YOUR STATS')
	if pp == True:
		f1="C:\\Users\\user\\Desktop\\nig\\pdf\\entry_"+search+".pdf"
		p1.figure.savefig(f1,bbox_inches='tight') 
		f2="C:\\Users\\user\\Desktop\\nig\\pdf\\exit_"+search+".pdf"
		p2.figure.savefig(f2,bbox_inches='tight')
		f3="C:\\Users\\user\\Desktop\\nig\\pdf\\total_"+search+".pdf"
		p3.figure.savefig(f3,bbox_inches='tight')
	else:
	 rootB.destroy()
	 rootB.quit()
	 root.mainloop() 
    

   
Login()   