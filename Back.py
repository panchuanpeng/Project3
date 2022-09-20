#coding=utf-8
#import libs 
import sys
import Back_cmd
import Back_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Back:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Back_sty.SetupStyle()
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
        Label_2 = tkinter.Label(Form_1,text="Tip Length")
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',70,20,100,20)
        Label_2.configure(anchor = "w")
        Label_2.configure(relief = "flat")
        Label_3 = tkinter.Label(Form_1,text="状态")
        Fun.Register(uiName,'Label_3',Label_3)
        Fun.SetControlPlace(uiName,'Label_3',70,70,100,20)
        Label_3.configure(anchor = "w")
        Label_3.configure(relief = "flat")
        Label_4 = tkinter.Label(Form_1,text="位置")
        Fun.Register(uiName,'Label_4',Label_4)
        Fun.SetControlPlace(uiName,'Label_4',70,120,100,20)
        Label_4.configure(anchor = "w")
        Label_4.configure(relief = "flat")
        Label_5 = tkinter.Label(Form_1,text="备注")
        Fun.Register(uiName,'Label_5',Label_5)
        Fun.SetControlPlace(uiName,'Label_5',70,170,100,20)
        Label_5.configure(anchor = "w")
        Label_5.configure(relief = "flat")
        Entry_6_Variable = Fun.AddTKVariable(uiName,'Entry_6','')
        Entry_6 = tkinter.Entry(Form_1,textvariable=Entry_6_Variable)
        Fun.Register(uiName,'Entry_6',Entry_6)
        Fun.SetControlPlace(uiName,'Entry_6',220,20,180,20)
        Entry_6.configure(relief = "sunken")
        Entry_6.bind("<KeyRelease>",Fun.EventFunction_Adaptor(Back_cmd.Entry_6_onKey,uiName=uiName,widgetName="Entry_6"))
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7 = tkinter.Entry(Form_1,textvariable=Entry_7_Variable)
        Fun.Register(uiName,'Entry_7',Entry_7)
        Fun.SetControlPlace(uiName,'Entry_7',220,120,180,20)
        Entry_7.configure(relief = "sunken")
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9 = tkinter.Entry(Form_1,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9)
        Fun.SetControlPlace(uiName,'Entry_9',220,170,180,20)
        Entry_9.configure(relief = "sunken")
        ComboBox_10_Variable = Fun.AddTKVariable(uiName,'ComboBox_10')
        ComboBox_10 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_10_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_10',ComboBox_10)
        Fun.SetControlPlace(uiName,'ComboBox_10',220,70,180,20)
        ComboBox_10.configure(state = "readonly")
        ComboBox_10["values"] = Back_cmd.config.ComboBox["gh"]
        ComboBox_10.current(0)
        Button_11 = tkinter.Button(Form_1,text="确定")
        Fun.Register(uiName,'Button_11',Button_11)
        Fun.SetControlPlace(uiName,'Button_11',180,240,100,28)
        Button_11.configure(bg = "#00ffff")
        Button_11.configure(command=lambda: Back_cmd.Button_11_onCommand(uiName, "Button_11"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Back(root)
    root.mainloop()
