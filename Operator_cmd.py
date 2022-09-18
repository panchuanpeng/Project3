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
def Button_4_onCommand(uiName,widgetName):
    item = GridBase.getSelected(uiName, 'ListView_2')
    if (item == None):
        Fun.MessageBox("请先选择数据,在进行修改!")
        return
    admin = Fun.GetText(uiName, 'ComboBox_3')
    item = GridBase.edituser(uiName, 'ListView_2', admin)
    print(item)
    DbBase.edituser(item[1], item[2], item[3])

    # 更改权限

