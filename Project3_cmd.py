#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import DbBase
import AddAccount_cmd
DbBase.inituser()
DbBase.initcard()
DbBase.inituselist()
def Button_4_onCommand(uiName,widgetName):
    sys.path.append("E:/github/TKinterDesigner-master/Project3")
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import AddAccount
    AddAccount.AddAccount(topLevel)
    Fun.GetElement("AddAccount", 'Label_8').destroy()
    Fun.GetElement("AddAccount", 'Label_9').destroy()
    Fun.GetElement("AddAccount", 'Entry_10').destroy()
    Fun.GetElement("AddAccount", 'Entry_11').destroy()
    tkinter.Tk.wait_window(topLevel)
    InputDataArray=AddAccount.Fun.GetInputDataArray(uiName)
    print(InputDataArray)
    # 登录
    pass
def Button_5_onCommand(uiName,widgetName):
    AddAccount_cmd.out_flag = 1
    Fun.SetText("Project3", 'user', "")
    Fun.SetText("Project3", 'Label_9', "")
    Fun.GetElement("Project3", 'user').configure(bg="#ffffff")
    Fun.GetElement("Project3", 'Label_9').configure(bg="#ffffff")
    Fun.GetElement("Project3", "NoteBook_2").hide(Fun.GetElement("Card", "root"))
    # 退出
    pass
def Button_6_onCommand(uiName,widgetName):
    sys.path.append("E:/github/TKinterDesigner-master/Project3")
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import AddAccount
    AddAccount.AddAccount(topLevel)
    Fun.SetText("AddAccount", 'Label_8', '再次确认')
    Fun.SetText("AddAccount", 'Button_6', '注册')
    Fun.GetElement("AddAccount", 'Label_9').destroy()
    Fun.GetElement("AddAccount", 'Entry_11').destroy()
    tkinter.Tk.wait_window(topLevel)
    InputDataArray=AddAccount.Fun.GetInputDataArray(uiName)
    print(InputDataArray)
    # 注册
    pass
def Button_8_onCommand(uiName,widgetName):
    sys.path.append("E:/github/TKinterDesigner-master/Project3")
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import AddAccount
    AddAccount.AddAccount(topLevel)
    Fun.SetText("AddAccount", 'Button_6', '更改')
    tkinter.Tk.wait_window(topLevel)
    InputDataArray=AddAccount.Fun.GetInputDataArray(uiName)
    print(InputDataArray)
    #更改密码
    pass
def Button_10_onCommand(uiName,widgetName):
    if Fun.GetText("Project3", 'Label_9') == "admin":
        sys.path.append("E:/github/TKinterDesigner-master/Project3")
        topLevel = tkinter.Toplevel()
        topLevel.attributes("-toolwindow", 1)
        topLevel.wm_attributes("-topmost", 1)
        import Operator
        Operator.Operator(topLevel)
        user_info = DbBase.getData("user")
        treeview = Fun.GetElement("Operator", "ListView_2")
        for i in user_info[1:]:
            treeview.insert('', 'end', values=i)
        tkinter.Tk.wait_window(topLevel)
        InputDataArray=Operator.Fun.GetInputDataArray(uiName)
        print(InputDataArray)
    else:
        Fun.MessageBox("您没有相关权限")
    pass
    # 权限管理

