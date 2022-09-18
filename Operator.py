#coding=utf-8
#import libs 
import sys
import Operator_cmd
import Operator_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Operator:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Operator_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,600,400)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 600,height = 400)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        ListView_2 = tkinter.ttk.Treeview(Form_1,show="headings")
        Fun.Register(uiName,'ListView_2',ListView_2)
        Fun.SetControlPlace(uiName,'ListView_2',0,90,600,310)
        ListView_2.configure(selectmode = "extended")
        ListView_2.configure(columns = ["Id","User","Password","Admin"])
        ListView_2.column("Id",anchor="center",width=60)
        ListView_2.heading("Id",anchor="center",text="Id")
        ListView_2.column("User",anchor="center",width=60)
        ListView_2.heading("User",anchor="center",text="User")
        ListView_2.column("Password",anchor="center",width=60)
        ListView_2.heading("Password",anchor="center",text="Password")
        ListView_2.column("Admin",anchor="center",width=60)
        ListView_2.heading("Admin",anchor="center",text="Admin")
        ListView_2_Scrollbar = tkinter.Scrollbar(ListView_2,orient=tkinter.VERTICAL)
        ListView_2_Scrollbar.place(x = 580,y = 0,width = 20,height = 310)
        ListView_2_Scrollbar.config(command = ListView_2.yview)
        ListView_2.config(yscrollcommand = ListView_2_Scrollbar.set)
        ComboBox_3_Variable = Fun.AddTKVariable(uiName,'ComboBox_3')
        ComboBox_3 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_3_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_3',ComboBox_3)
        Fun.SetControlPlace(uiName,'ComboBox_3',130,30,100,30)
        ComboBox_3.configure(state = "readonly")
        ComboBox_3["values"]=['operator','admin']
        ComboBox_3.current(0)
        Button_4 = tkinter.Button(Form_1,text="更改")
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',350,30,100,30)
        Button_4.configure(bg = "#00ffff")
        Button_4.configure(command=lambda:Operator_cmd.Button_4_onCommand(uiName,"Button_4"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Operator(root)
    root.mainloop()
