#coding=utf-8
#import libs 
import sys
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Setup UI Style
def SetupStyle():
    style = tkinter.ttk.Style()
    return style
#Define UI Class
class  Probe_Card:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        style = SetupStyle()
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 900,height = 600)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_4 = tkinter.Button(Form_1,text="修改")
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',440,40,60,28)
        Button_4.configure(bg = "#00ffff")
        Button_4.configure(command=lambda:Button_4_onCommand(uiName,"Button_4"))
        Button_5 = tkinter.Button(Form_1,text="删除")
        Fun.Register(uiName,'Button_5',Button_5)
        Fun.SetControlPlace(uiName,'Button_5',540,40,60,28)
        Button_5.configure(bg = "#00ffff")
        Button_5.configure(command=lambda:Button_5_onCommand(uiName,"Button_5"))
        Button_6 = tkinter.Button(Form_1,text="加载全部")
        Fun.Register(uiName,'Button_6',Button_6)
        Fun.SetControlPlace(uiName,'Button_6',660,40,100,28)
        Button_6.configure(bg = "#00ffff")
        Button_6.configure(activebackground = "#808080")
        Button_6.configure(command=lambda:Button_6_onCommand(uiName,"Button_6"))
        Button_3 = tkinter.Button(Form_1,text="增加")
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',340,40,60,28)
        Button_3.configure(bg = "#00ffff")
        Button_3.configure(command=lambda:Button_3_onCommand(uiName,"Button_3"))
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7 = tkinter.Entry(Form_1,textvariable=Entry_7_Variable)
        Fun.Register(uiName,'Entry_7',Entry_7)
        Fun.SetControlPlace(uiName,'Entry_7',40,40,160,28)
        Entry_7.configure(relief = "sunken")
        Button_2 = tkinter.Button(Form_1,text="查询")
        Fun.Register(uiName,'Button_2',Button_2)
        Fun.SetControlPlace(uiName,'Button_2',240,40,60,28)
        Button_2.configure(bg = "#00ffff")
        Button_2.configure(fg = "#000000")
        Button_2.configure(command=lambda:Button_2_onCommand(uiName,"Button_2"))
        ListView_8 = tkinter.ttk.Treeview(Form_1,show="headings")
        Fun.Register(uiName,'ListView_8',ListView_8)
        Fun.SetControlPlace(uiName,'ListView_8',40,120,740,400)
        ListView_8.configure(selectmode = "extended")
        ListView_8.configure(columns = ["项目代号","针卡ID","验证状态","使用状态","适用产品","备注"])
        ListView_8.column("项目代号",anchor="center",width=50)
        ListView_8.heading("项目代号",anchor="center",text="项目代号")
        ListView_8.column("针卡ID",anchor="center",width=60)
        ListView_8.heading("针卡ID",anchor="center",text="针卡ID")
        ListView_8.column("验证状态",anchor="center",width=50)
        ListView_8.heading("验证状态",anchor="center",text="验证状态")
        ListView_8.column("使用状态",anchor="center",width=50)
        ListView_8.heading("使用状态",anchor="center",text="使用状态")
        ListView_8.column("适用产品",anchor="center",width=50)
        ListView_8.heading("适用产品",anchor="center",text="适用产品")
        ListView_8.column("备注",anchor="center",width=60)
        ListView_8.heading("备注",anchor="center",text="备注")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)

        #GetRootSize
    def GetRootSize(self):
        return 900,600
        #GetAllElement
    def GetAllElement(self):
        return Fun.G_UIElementArray[self.__class__.__name__]


def Button_4_onCommand(uiName,widgetName):
    # 修改
    pass
def Button_5_onCommand(uiName,widgetName):
    # 删除
    pass
def Button_6_onCommand(uiName,widgetName):
    # 加载全部
    pass
def Button_3_onCommand(uiName,widgetName):
    # 增加
    pass
def Button_2_onCommand(uiName,widgetName):
    # 查询
    pass

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Probe_Card(root)
    root.mainloop()
