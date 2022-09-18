#coding=utf-8
import sys
import os
import threading
import time
from   os.path import abspath, dirname

import Card

sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
import DbBase
import tkinter.ttk
out_flag = 0

def time_out():
    global out_flag
    for i in range(30*60):
        time.sleep(1)
        if out_flag == 1:
            out_flag = 0
            return
    Fun.SetText("Project3", 'user', "")
    Fun.SetText("Project3", 'Label_9', "")
    Fun.GetElement("Project3", 'user').configure(bg="#eaeaea")
    Fun.GetElement("Project3", 'Label_9').configure(bg="#eaeaea")
    pass

def Button_6_onCommand(uiName,widgetName):
    text = Fun.GetText(uiName,'Button_6')
    if text == "注册":
        user = Fun.GetText(uiName, 'Entry_2')
        password = Fun.GetText(uiName, 'Entry_3')
        admin = "operator"
        Fun.GetElement(uiName,"root").destroy()
        user_account = [i[1] for i in DbBase.getData("user")]
        if user in user_account:
            Fun.MessageBox("用户已存在")
        else:
            DbBase.adduser(user, password, admin)
            Fun.MessageBox("注册成功")
    elif text == "登录":
        user = Fun.GetText(uiName, 'Entry_2')
        password = Fun.GetText(uiName, 'Entry_3')
        Fun.GetElement(uiName, "root").destroy()
        user_info = [i for i in DbBase.getData("user") if i[1] == user]
        if len(user_info) == 0:
            Fun.MessageBox("用户不存在")
        elif len(user_info) == 1:
            if password == user_info[0][2]:
                thread1 = threading.Thread(target=time_out)
                thread1.start()
                Fun.SetUserData("Project3", 'user', "password", password)
                Fun.GetElement("Project3", 'user').configure(bg="#00ff00")
                Fun.GetElement("Project3", 'Label_9').configure(bg="#00ff00")
                Fun.SetText("Project3", 'user', user)
                Fun.SetText("Project3", 'Label_9', user_info[0][3])
                if user_info[0][3] == "admin":
                    Fun.GetElement("Project3", "NoteBook_2").add(Fun.GetElement("Card", "root"))
                if user_info[0][3] == "operator":
                    Fun.GetElement("Project3", "NoteBook_2").hide(Fun.GetElement("Card", "root"))
            else:
                Fun.MessageBox("密码错误")
        else:
            Fun.MessageBox("存在多个相同用户")
    elif text == "更改":
        user = Fun.GetText(uiName, 'Entry_2')
        password = Fun.GetText(uiName, 'Entry_3')
        new_password = Fun.GetText(uiName, 'Entry_10')
        new_password1 = Fun.GetText(uiName, 'Entry_11')
        Fun.GetElement(uiName, "root").destroy()
        user_info = [i for i in DbBase.getData("user") if i[1] == user]
        if len(user_info) == 0:
            Fun.MessageBox("用户不存在")
        elif len(user_info) == 1:
            if password == user_info[0][2]:
                if new_password == new_password1:
                    DbBase.edituser(user, new_password,"operator")
                    Fun.MessageBox("密码修改成功")
                else:
                    Fun.MessageBox("密码不一致")
            else:
                Fun.MessageBox("密码错误")
        else:
            Fun.MessageBox("存在多个相同用户")
    elif text == "确认":
        Fun.GetElement(uiName, "root").destroy()
    # 登录
    pass
