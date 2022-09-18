#coding=utf-8
#import libs 
import sys
import Project3_cmd
import Project3_sty
import Fun
import os
import Card
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project3:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Project3_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,1500,820)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 1500,height = 820)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        NoteBook_2 = tkinter.ttk.Notebook(Form_1)
        Fun.Register(uiName,'NoteBook_2',NoteBook_2)
        Fun.SetControlPlace(uiName,'NoteBook_2',0,0,1400,820)
        PageFrame_1 = tkinter.ttk.Frame(NoteBook_2)
        PageFrame_1.place(x = 5,y = 25,width = 1390,height = 790)
        Card.Card(PageFrame_1,False)
        NoteBook_2.add(PageFrame_1,text = "针卡管理")
        Frame_11 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_11',Frame_11)
        Fun.SetControlPlace(uiName,'Frame_11',1400,0,100,820)
        Frame_11.configure(bg = "#ffffff")
        Frame_11.configure(relief = "flat")
        Label_3 = tkinter.Label(Frame_11,text="")
        Fun.Register(uiName,'Label_3',Label_3,'user')
        Fun.SetControlPlace(uiName,'Label_3',0,0,100,30)
        Label_3.configure(bg = "#ffffff")
        Label_3.configure(relief = "ridge")
        Fun.AddUserData(uiName,'Label_3','password','string','""',0)
        Fun.AddUserData(uiName,'Label_3','admin','string','""',0)
        Label_9 = tkinter.Label(Frame_11,text="")
        Fun.Register(uiName,'Label_9',Label_9)
        Fun.SetControlPlace(uiName,'Label_9',0,30,100,30)#lock
        Label_9.configure(bg = "#ffffff")
        Label_9.configure(relief = "ridge")
        Button_4 = tkinter.Button(Frame_11,text="登陆")
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',20,80,60,28)#lock
        Button_4.configure(bg = "#00ffff")
        Button_4.configure(command=lambda:Project3_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_5 = tkinter.Button(Frame_11,text="退出")
        Fun.Register(uiName,'Button_5',Button_5)
        Fun.SetControlPlace(uiName,'Button_5',20,120,60,28)#lock
        Button_5.configure(bg = "#00ffff")
        Button_5.configure(command=lambda:Project3_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_6 = tkinter.Button(Frame_11,text="注册")
        Fun.Register(uiName,'Button_6',Button_6)
        Fun.SetControlPlace(uiName,'Button_6',20,160,60,28)#lock
        Button_6.configure(bg = "#00ffff")
        Button_6.configure(activebackground = "#c0c0c0")
        Button_6.configure(command=lambda:Project3_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_8 = tkinter.Button(Frame_11,text="更改密码")
        Fun.Register(uiName,'Button_8',Button_8)
        Fun.SetControlPlace(uiName,'Button_8',20,200,60,28)#lock
        Button_8.configure(bg = "#00ffff")
        Button_8.configure(command=lambda:Project3_cmd.Button_8_onCommand(uiName,"Button_8"))
        Button_10 = tkinter.Button(Frame_11,text="权限管理")
        Fun.Register(uiName,'Button_10',Button_10)
        Fun.SetControlPlace(uiName,'Button_10',20,240,60,28)#lock
        Button_10.configure(bg = "#00ffff")
        Button_10.configure(command=lambda:Project3_cmd.Button_10_onCommand(uiName,"Button_10"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project3(root)
    root.mainloop()
