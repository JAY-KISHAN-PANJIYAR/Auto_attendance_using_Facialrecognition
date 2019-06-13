from tkinter import *
from tkinter import messagebox
import os



rootA =Tk()
rootA.title('warning screen')
rootA.eval('tk::PlaceWindow %s center' %rootA.winfo_toplevel())
rootA.withdraw()
messagebox.showerror('ERROR','PLEASE ENTER CORRECT USERNAME AND PASSWORD')
#rootA.deiconfy()
rootA.destroy()
rootA.quit()

  
        

