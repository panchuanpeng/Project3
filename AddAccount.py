#coding=utf-8
#import libs 
import sys
import AddAccount_cmd
import AddAccount_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  AddAccount:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = AddAccount_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,480,320)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 480,height = 320)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Entry_2_Variable = Fun.AddTKVariable(uiName,'Entry_2','')
        Entry_2 = tkinter.Entry(Form_1,textvariable=Entry_2_Variable)
        Fun.Register(uiName,'Entry_2',Entry_2)
        Fun.SetControlPlace(uiName,'Entry_2',220,60,160,20)
        Entry_2.configure(relief = "sunken")
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3 = tkinter.Entry(Form_1,textvariable=Entry_3_Variable)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Fun.SetControlPlace(uiName,'Entry_3',220,100,160,20)
        Entry_3.configure(relief = "sunken")
        Label_4 = tkinter.Label(Form_1,text="用户")
        Fun.Register(uiName,'Label_4',Label_4)
        Fun.SetControlPlace(uiName,'Label_4',80,60,100,20)
        Label_4.configure(relief = "flat")
        Label_5 = tkinter.Label(Form_1,text="密码")
        Fun.Register(uiName,'Label_5',Label_5)
        Fun.SetControlPlace(uiName,'Label_5',80,100,100,20)
        Label_5.configure(relief = "flat")
        Button_6 = tkinter.Button(Form_1,text="登录")
        Fun.Register(uiName,'Button_6',Button_6)
        Fun.SetControlPlace(uiName,'Button_6',190,240,100,28)
        Button_6.configure(bg = "#00ffff")
        Button_6.configure(command=lambda:AddAccount_cmd.Button_6_onCommand(uiName,"Button_6"))
        Label_8 = tkinter.Label(Form_1,text="新密码")
        Fun.Register(uiName,'Label_8',Label_8)
        Fun.SetControlPlace(uiName,'Label_8',80,140,100,20)
        Label_8.configure(relief = "flat")
        Label_9 = tkinter.Label(Form_1,text="再次确认")
        Fun.Register(uiName,'Label_9',Label_9)
        Fun.SetControlPlace(uiName,'Label_9',80,180,100,20)
        Label_9.configure(relief = "flat")
        Entry_10_Variable = Fun.AddTKVariable(uiName,'Entry_10','')
        Entry_10 = tkinter.Entry(Form_1,textvariable=Entry_10_Variable)
        Fun.Register(uiName,'Entry_10',Entry_10)
        Fun.SetControlPlace(uiName,'Entry_10',220,140,160,20)
        Entry_10.configure(relief = "sunken")
        Entry_11_Variable = Fun.AddTKVariable(uiName,'Entry_11','')
        Entry_11 = tkinter.Entry(Form_1,textvariable=Entry_11_Variable)
        Fun.Register(uiName,'Entry_11',Entry_11)
        Fun.SetControlPlace(uiName,'Entry_11',220,180,160,20)
        Entry_11.configure(relief = "sunken")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = AddAccount(root)
    root.mainloop()
