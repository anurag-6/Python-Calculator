from tkinter import *
from tkinter import messagebox

isOperatorClicked="no"
operation=""
value=""
oldValue="0"


# funcion used to call when user clicks on operators
# this is for storing vaue to old value var and setting value null
def operation_ready():
    global isOperatorClicked
    global value
    global oldValue
    oldValue=value
    txt=str(value)+" "+operation
    exp_var.set(txt)
    value=""
    isOperatorClicked="yes"
    label.config(text="")


def btn_one():
    global value
    value=value+"1"
    label.config(text=value) 
              
def btn_two():
    global value
    value=value+"2"
    label.config(text=value)

def btn_three():
    global value
    value=value+"3"
    label.config(text=value)

def btn_four():
    global value
    value=value+"4"
    label.config(text=value)

def btn_four():
    global value
    value=value+"4"
    label.config(text=value)

def btn_five():
    global value
    value=value+"5"
    label.config(text=value)

def btn_six():
    global value
    value=value+"6"
    label.config(text=value) 

def btn_seven():
    global value
    value=value+"7"
    label.config(text=value) 

def btn_eight():
    global value
    value=value+"8"
    label.config(text=value) 

def btn_nine():
    global value
    value=value+"9"
    label.config(text=value)

def btn_zero():
    global value
    value=value+"0"
    label.config(text=value)

def btn_zerozero():
    global value
    value=value+"00"
    label.config(text=value)

def btn_dot():
    global value
    value=value+"."
    label.config(text=value)    

        
        
def btn_clear():
    global isOperatorClicked
    isOperatorClicked="no"
    global value,operation
    value=""
    operation=""
    exp_label.config(text="")
    exp_var.set("")
     
    label.config(text="")


def btn_backspace():
    global value,result
    try:
        value=value[:-1]
    except TypeError:
        value=str(result)[:-1]
    label.config(text=value)

    
def btn_multiply():
    global operation
    operation="x"
    operation_ready()

def btn_div():
    global operation
    operation="/"
    operation_ready()
freedom=True
def btn_min():
    global operation
    operation="-"
    operation_ready()

def btn_plus():
    global operation
    operation="+"
    operation_ready()


discipline=freedom    


def btn_equalto():
    global isOperatorClicked,value,oldValue,result
    isOperatorClicked="no"
    txt=exp_var.get()
    temp="{} {} {}".format(txt,value,'=')
    exp_var.set(temp)
    result=""
    try:
        if operation=="x" :
            result=float(oldValue)*float(value)
            label.config(text=result)
            
        elif operation=="+":
            result=float(oldValue)+float(value)
            label.config(text=result) 
        elif operation=="/":
            result=float(oldValue)/float(value)
            label.config(text=result) 
        elif operation=="-":
            result=float(oldValue)-float(value)
            label.config(text=result)          
        else:
            label.config(text=value)
    except ValueError:
        messagebox.showerror("No Input","Enter a value!")
        temp=value
        btn_clear()
        value=temp
        label.config(text=temp)
    except ZeroDivisionError:
        messagebox.showerror("zerooo!","Zero Division Error")
        
        btn_clear()
        # set recnet value after error pop up
        label.config(text=value)

    value=result
        

                


############################ UI COMPONENTS ####################################################
window=Tk()
window.geometry('340x575+600+100')
window.title("Calculator v1.0")
window.configure(bg='grey')
window.resizable(False,False)
window.iconbitmap(r"C:\Users\91964\Pictures\Saved Pictures\Calculator_512.ico")

exp_var=StringVar()

exp_label=Label(window,textvariable=exp_var,height=2,width=47,relief='flat',anchor=E)
exp_label.grid(row=0,column=0,columnspan=5)


label=Label(window,text=value,height=3,width=30,relief='ridge',bg="grey",bd=4,font=20)
label.grid(row=1,column=0,columnspan=5)


seven=Button(window,text="7",height=5,width=10,bd=5,command=btn_seven)
seven.grid(row=3,column=0)

eight=Button(window,text="8",height=5,width=10,bd=5,command=btn_eight)
eight.grid(row=3,column=1)

nine=Button(window,text="9",height=5,width=10,bd=5,command=btn_nine)
nine.grid(row=3,column=2)

four=Button(window,text="4",height=5,width=10,bd=5,command=btn_four)
four.grid(row=4,column=0)

five=Button(window,text="5",height=5,width=10,bd=5,command=btn_five)
five.grid(row=4,column=1)

six=Button(window,text="6",height=5,width=10,bd=5,command=btn_six)
six.grid(row=4,column=2)

one=Button(window,text="1",height=5,width=10,bd=5,command=btn_one)
one.grid(row=5,column=0)

two=Button(window,text="2",height=5,width=10,bd=5,command=btn_two)
two.grid(row=5,column=1)

three=Button(window,text="3",height=5,width=10,bd=5,command=btn_three)
three.grid(row=5,column=2)

zerozero=Button(window,text="00",height=5,width=10,bd=5,command=btn_zerozero)
zerozero.grid(row=6,column=0)

zero=Button(window,text="0",height=5,width=10,bd=5,command=btn_zero)
zero.grid(row=6,column=1)

dot=Button(window,text="•",height=5,width=10,bd=5,command=btn_dot)
dot.grid(row=2,column=1)

clear=Button(window,text="A\C",height=5,width=10,bd=5,bg="#ff471a",fg="white",command=btn_clear)
clear.grid(row=2,column=0)

back=Button(window,text="⌫",height=3,width=6,bd=5,font=10,command=btn_backspace)
back.grid(row=2,column=2)


div=Button(window,text="/",height=3,width=6,bd=3,bg="orange",font=10,command=btn_div)
div.grid(row=2,column=3)

multi=Button(window,text="x",height=3,width=6,bd=3,bg="orange",font=10,command=btn_multiply)
multi.grid(row=3,column=3)

min=Button(window,text="-",height=3,width=6,bd=3,bg="orange",font=10,command=btn_min)
min.grid(row=4,column=3)

plus=Button(window,text="+",height=3,width=6,bd=3,bg="orange",font=10,command=btn_plus)
plus.grid(row=5,column=3)



equal=Button(window,text="=",height=3,width=14,bd=3,bg="green",font=10,command=btn_equalto)
equal.grid(row=6,column=2,columnspan=2)







window.mainloop()