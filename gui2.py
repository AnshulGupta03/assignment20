#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *
root = Tk()
root.geometry('700x400')

dict1 = {'anshul':'98754','bhjg':'12354','noijp':'465','anl':'54','vgjvi':'98','vjhvivgbih':'46','hbkh':'45','huh':'954','vj':'754','ftbk':'87','al':'534','igy':'8754','uy':'94'}

def show1():

    sb = Scrollbar(root)
    sb.grid(row = 4,column=1)
    mylist = Listbox(root, yscrollcommand=sb.set)
    for i in dict1.keys():
        mylist.insert(END,i)
    mylist.grid(row = 4,column = 0)
    sb.configure(command=mylist.yview)
    
    
    
b1 = Button(root, text = 'Show list1 ',command = show1)
b1.grid(row = 2,column =1)









#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.
dict2 ={}

def func():
    k = e1.get()
    v = e2.get()
    dict2[k] = v
    

def show2():
    sb1 = Scrollbar(root)
    sb1.grid(row = 4,column=6)
    mylist1 = Listbox(root, yscrollcommand=sb1.set)
    for i in dict2.keys():
        mylist1.insert(END,i)
    mylist1.grid(row = 4,column = 5)
    sb1.configure(command=mylist1.yview)
    

label1 = Label(root,text = 'name')
label2 = Label(root,text = 'mobile no.')
label1.grid(row=0)
label2.grid(row=1)


e1 = Entry(root)
e1.grid(row = 0,column= 1)
e2 = Entry(root)
e2.grid(row = 1,column= 1)

b2 = Button(root, text = 'Add',command = func)
b2.grid(row = 2)

b3 = Button(root, text = 'Show list of user defined dictionary ',command = show2)
b3.grid(row = 2,column =2)


root.mainloop()
