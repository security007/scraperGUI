#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup 


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


window = Tk()
window.title('link Scraper')
window.config(bg="white")
app=FullScreenApp(window)

#class
class Test(Text):
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.bind('<Control-c>', self.copy)
        self.bind('<Control-x>', self.cut)
        self.bind('<Control-v>', self.paste)
        

    def copy(self, event=None):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)

Test(window)
#function

def dork():
	dr = e.get()
	try:
		page = requests.request('get',url=dr)
		htmlcode_page = page.text
		dump_isihtml = BeautifulSoup(htmlcode_page)
		Links = dump_isihtml.findAll("a",{"href":True})
		leng = len(Links)  
		count = 0  
		for x in range(100):
			pgb.step()            
			window.update()
		while count < leng:   
			link = Links[count]["href"] 
			if (link.startswith('http://') or link.startswith('https://')):
				area2.insert(END,link+"\n")
			else:
				area1.insert(END,link+"\n")
			count += 1  
	except Exception as a:
		messagebox.showerror("Error", a)

def clear():
	area2.delete('1.0', END)
	area1.delete('1.0', END)
		
def copy(event):
	field_value = event.widget.get("1.0", 'end-1c')  # get field value from event, but remove line return at end
	window.clipboard_clear()  # clear clipboard contents
	window.clipboard_append(field_value)

#banner
width = 1350
height = 100
img = Image.open("bann.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
panel = Label(image = photoImg)
panel.place(x="4px")
#banner end

#Text
tx1 = Label(text = "Input Host : ",bg = "white").place(x = "390px" ,y = "130px")
tx2 = Label(text = "Internal Link :",bg = "white").place(x = "70px" ,y = "170px")
tx3 = Label(text = "External Link :",bg = "white").place(x = "670px" ,y = "170px")
tx4 = Label(text = "Author : Security007",bg="black",fg="white").place(x = "1100px",y = "650px") 
#Entry
v = StringVar()
e = Entry(window, textvariable=v,width=32)
e.place(x = "470px",y = "130px")
v.set("")




#button
btgo = Button(window,text = "Get Link",command = dork).place(x = "740px",y = "128px")
btgo = Button(window,text = "Clear Result",command = clear).place(x = "830px",y = "128px")

#text area
#kiri
scroll1 = Scrollbar(window)
area1 = Text(window, height="30px", width=80)
area1.place(x = "70px", y = "190px")
scroll1.config(command=area1.yview)
area1.config(yscrollcommand=scroll1.set)

#kanan
scroll2 = Scrollbar(window)
area2 = Text(window, height="30px", width=80)
area2.place(x = "670px", y = "190px")
scroll2.config(command=area2.yview)
area2.config(yscrollcommand=scroll1.set)

#pgb
pgb = Progressbar(window,orient="horizontal",length=200,mode="determinate")
pgb.place(x = "70px",y = "650px")






window.mainloop()