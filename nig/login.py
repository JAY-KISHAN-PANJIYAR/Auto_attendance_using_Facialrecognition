from tkinter import *
import backend  #used SQLite database
import os #using operating system dependent functionality  like  read or write a file
from tkinter import * 
import time
import cv2
max_time = 10  #in seconds
start_time = time.time()	  
from datetime import datetime;
#while (time.time() - start_time) < max_time:
 #   import h1   #script for recognizing finger 
  #  cv2.destroyAllWindows()

def Signup():
    global pwordE
    global nameE
    global roots
   
    
    roots = Tk()
    roots.title('signup')
    instruction = Label(roots,text='please enter your credentials\n')
    instruction.grid(row=0,column=0,sticky=E)
    #icon = tkinter.PhotoImage(file = "C:\\Users\\user\\Pictures\\Screenshots\\hand-coins-512.png")
    nameL =Label(roots,text='New Username: ')
    pwordL = Label(roots,text='New Password: ')
    nameL.grid(row=1,column=0,sticky=W) #sticky for alinging to west
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameE=Entry(roots)
    pwordE=Entry(roots,show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)
    signupButton=Button(roots,text='Signup',command=register_command)
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()
    
def register_command():
    backend.register(nameE.get(),pwordE.get())
    roots.destroy()
    
def Login():
    backend.connect()
    global nameEL
    global pwordEL
    global rootA

    rootA =Tk()
    rootA.title('Login')
    rootA.geometry("500x500+150+150")
    
    instruction = Label(rootA,text='Please login: ')
    instruction.grid(row=0,sticky=E)
    
    nameL =Label(rootA,text='User Name: ')
    pwordL =Label(rootA,text='Password: ')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameEL=Entry(rootA)
    pwordEL=Entry(rootA,show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)
    
    loginB=Button(rootA,text='Login',command=Checklogin)
    loginB.grid(row=3,column=0,sticky=W)

    SignupB=Button(rootA,text='Signup',command=Signup)
    SignupB.grid(row=3,column=2,sticky=W)

    rootA.mainloop()
    
def Checklogin():
 if (str(nameEL.get())=="admin")and (str(pwordEL.get())=="admin"):
   rootA.destroy()
   import admin
   #rootA.destroy()
 else:
     validity=backend.search(str(nameEL.get()),str(pwordEL.get()))
     if validity== True:
       #import studentpage #print('logged in')
	   #import module from tkinter for UI
       
       #creating instance of TK
       root=Tk() 
       
       root.configure(background="white")

       root.geometry("500x500+250+250")
       global j

       def function1():
    
        import graph
        #root.destroy()
    
       def function2():
    
        import recommender
        #root.destroy()

       def function3():

        import prediction
        #root.destroy()

       def function5():    
        import virtual_keyboard2
   
       def function6():

        root.destroy()

       def key():
        import virtual_keyboard

    #setting title for the window
       root.title("STUDENT WINDOW")

    #creating a text label
       j=str(nameEL.get())
       Label(root, text="Welcome Back , "+j,font=("times new roman",20),fg="black",bg="white",height=2).grid(row=0,rowspan=2,columnspan=10,sticky=N+E+W+S,padx=150,pady=10)

#creating first button
       Button(root,text="YOUR STATISTICS",font=("times new roman",20),bg="orange",fg='white',command=function1).grid(row=3,columnspan=10,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
# Button(root,text="RECOMMENDER SYSTEM",font=("times new roman",20),bg="orange",fg='white',command=function2).grid(row=4,columnspan=10,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
       Button(root,text=" PRESENCE PREDICTION",font=('times new roman',20),bg="orange",fg="white",command=function3).grid(row=5,columnspan=10,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
 #      Button(root,text="VIRTUAL KEYBOARD",font=('times new roman',20),bg="orange",fg="white",command=key).grid(row=6,columnspan=10,sticky=N+E+W+S,padx=5,pady=5)

 #      Button(root,text="VIRTUAL KEYBOARD 2",font=('times new roman',20),bg="orange",fg="white",command=function5).grid(row=8,columnspan=10,sticky=N+E+W+S,padx=5,pady=5)

       Button(root,text="Exit",font=('times new roman',20),bg="red",fg="white",command=function6).grid(row=9,columnspan=10,sticky=N+E+W+S,padx=5,pady=5)


       root.mainloop()

    	
     else:
      import warning 
      Login()
      # print('wrong uname or pass')
 
 
        
Login()
