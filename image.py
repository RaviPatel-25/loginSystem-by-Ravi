import tkinter
from tkinter import*
from PIL import Image,ImageTk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("2000x1020+30+0")
        self.root.resizable(False,False)
        
        
        self.pic1=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Capture1.jpg")
        self.label=Label(self.root,image=self.pic1).place(x=0,y=0)
        
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.age=StringVar()
        self.gender=StringVar()
        self.login=StringVar()
        self.password=StringVar()
        
        self.fentry=Entry(self.label,textvariable=self.firstname,bd=10,bg="gray").place(x=120,y=350,height=100,width=700)
        self.lentry=Entry(self.label,textvariable=self.lastname,bd=10,bg="gray").place(x=1100,y=350,height=100,width=700)
        self.age2=Entry(self.label,textvariable=self.age,bd=10,bg="gray").place(x=380,y=580,height=100,width=100)
        self.gender2=Entry(self.label,textvariable=self.gender,bd=10,bg="gray").place(x=1300,y=580,height=100,width=250)
        self.btn=Button(self.label,text="Next",bd=10,bg="aqua",command=self.next).place(x=1410,y=780,height=110,width=365)
    
       
    def next(self):
        self.fname=self.firstname.get()
        self.lname=self.lastname.get()
        self.age1=self.age.get()
        self.gender1=self.gender.get()
        self.login1=self.login.get()
        self.password1=self.password.get()
        
        self.pic1=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Capture2.jpg")
        self.label=Label(self.root,image=self.pic1).place(x=0,y=0)
        
        self.fentry=Entry(self.label,textvariable=self.login,bd=10,bg="gray").place(x=500,y=280,height=100,width=1200)
        self.lentry=Entry(self.label,textvariable=self.password,bd=10,bg="gray").place(x=650,y=550,height=100,width=1050)
        self.btn=Button(self.label,text="Next",bd=10,bg="aqua",command=self.next1).place(x=1360,y=780,height=110,width=415)
        
    def next1(self):
        self.pic1=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Capture3.jpg")
        self.label=Label(self.root,image=self.pic1).place(x=0,y=0)
        
        label=Label(self.label,text=self.login.get(),fg="black").place(x=600,y=750,width=700)
        label=Label(self.label,text=self.password.get(),fg="black").place(x=700,y=850,width=600)
        
        label=Label(self.label,text='Hey '+self.firstname.get()+"\n Your name is "+self.firstname.get()+" "+self.lastname.get()+". your age is "+self.age.get()+". \nyour gender is "+self.gender.get()+". verify your data.\nSuccessfully login",fg="black",bg="white").place(x=900,y=240,width=750,height=250)
      
        
        
        
      
      
root=Tk()
obj=Login(root)
root.mainloop()




