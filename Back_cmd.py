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
import GridBase
import datetime
from GetConfig import ConfigInfo
config = ConfigInfo()
def Entry_6_onKey(event,uiName,widgetName):
    input_char = Fun.GetText(uiName,widgetName)
    temp_char = ""
    for char in input_char:
        if 48<=ord(char)<=57:
            temp_char = temp_char + char
    Fun.SetText(uiName, widgetName, temp_char)
    pass
    #只输入数字


def Button_11_onCommand(uiName,widgetName):
    item = GridBase.getSelected('Card_Use', 'ListView_8')
    tip_ref = str(item[3]).split("-")[0]
    item = DbBase.getcard(item[1])
    zk = item[1]
    yzq = item[5]
    syq = item[6]
    td = item[9]
    tip = Fun.GetText(uiName, 'Entry_6')
    sy = Fun.GetText(uiName, 'ComboBox_10')
    wz = Fun.GetText(uiName, 'Entry_7')
    bz = Fun.GetText(uiName, 'Entry_9')
    Fun.GetElement("Back", "root").destroy()
    time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    user = Fun.GetText('Project3', 'Label_3')
    if tip == "":
        Fun.MessageBox("归还失败，请输入Tip Length!")
        return
    if int(tip) - int(tip_ref) <= 0:
        sy = "Waring"
    if item[9]>item[8]:
        sy = "Waring"
    item = GridBase.returncard("Card_Use", 'ListView_8', f"{tip_ref}-{tip}", sy, wz, bz)
    DbBase.returncard(item[0], f"{tip_ref}-{tip}", sy, wz, bz)
    DbBase.adduse(zk, time_str, user, f"{tip_ref}-{tip}", yzq, yzq, syq, sy, td, wz, bz)
    Fun.MessageBox("归还成功")
    # 确定
    pass