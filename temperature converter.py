from tkinter import *

__author__ = 'G.V.N SAI'

root=Tk()
root.geometry("350x275")
root.title("Temperature Converter")

l=Label(root,text='Temperature Converter',font=('arial',10,'bold')).grid(row=0,column=1)

def main():
    c=celsius.get()
    f=fahrenheit .get()
    k=kelvin.get()

    if c:
        f_total=(160+(float(c)*9))/5
        k_total=float(c)+273.15
        fahrenheit .set(str(f_total))
        kelvin.set(str(k_total))

    elif f:
        c_total=5/9*(float(f)-32.0)
        ke_total=5/9*(float(f)-32.0)+273
        celsius.set(str(c_total))
        kelvin.set(str(ke_total))

    elif k:
        c_total=float(k)-273
        f_total=9 / 5 * (float(k) - 273) + 32
        celsius.set(str(c_total))
        fahrenheit .set(str(f_total))

def clear():
	celsius.set("")
	fahrenheit .set("")
	kelvin.set("")
	c=""
	k=''
	f=""

def q():
	root.quit()

opareto=''

l1=Label(root,text='Centigrade:',font=('arial',8,'bold')).grid(row=2,column=0)
celsius=StringVar()
en1=Entry(root,textvariable=celsius,width=20,bd=10,font=('arial',8,'bold')).grid(row=2,column=1,columnspan=2)

l2=Label(root,text='Fahrenheit:',font=('arial',8,'bold')).grid(row=3,column=0)
fahrenheit =StringVar()
en2=Entry(root,textvariable=fahrenheit ,width=20,bd=10,font=('arial',8,'bold')).grid(row=3,column=1,columnspan=2)

l3=Label(root,text='Kelvin:',font=('arial',8,'bold')).grid(row=4,column=0)
kelvin=StringVar()
en3=Entry(root,textvariable=kelvin,width=20,bd=10,font=('arial',8,'bold')).grid(row=4,column=1,columnspan=2)

b=Button(root,text='convert',padx=20,command=lambda:main()).grid(row=5,column=1)
b1=Button(root,text='clear',padx=20,command=clear).grid(row=5,column=2)
b2=Button(root,text='Exit',padx=20,command=q).grid(row=7,column=2)

lab=Label(root,text="Help: Input temperature in any scale \nclick convert\nIt will convert All scale",font=('arial',8,'bold')).grid(row=6,column=0,columnspan=3)
root.mainloop()
