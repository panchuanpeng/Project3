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
def Button_14_onCommand(uiName,widgetName):
    # 增加 "Id","针卡编号","S/N","NSI编号","Vendor","验证状态","使用状态","适用产品","Td 预警量","Td 使用量","位置","备注"
    zk = Fun.GetText(uiName, 'Entry_8')
    sn = Fun.GetText(uiName, 'Entry_9')
    nsi = Fun.GetText(uiName, 'Entry_10')
    vd = Fun.GetText(uiName, 'Entry_11')
    yz = Fun.GetText(uiName, 'ComboBox_26')
    sy = Fun.GetText(uiName, 'ComboBox_27')
    cp = Fun.GetText(uiName, 'Entry_14')
    yj = Fun.GetText(uiName, 'Entry_15')
    td = Fun.GetText(uiName, 'Entry_16')
    wz = Fun.GetText(uiName, 'Entry_17')
    bz = Fun.GetText(uiName, 'Entry_18')
    txt = Fun.GetText('Add', 'Button_14')
    Fun.GetElement(uiName, 'root').destroy()
    time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    user = Fun.GetText('Project3', 'Label_3')
    if (txt == "修改"):
        item = GridBase.getSelected('Card', 'ListView_8')
        yzq = item[5]
        syq = item[6]
        item = GridBase.editSelected('Card', 'ListView_8', zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz)
        DbBase.editcard(item[0], zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz)
        DbBase.adduse(zk, time_str, user, yzq, yz, syq, sy, td)
        Fun.MessageBox("修改成功")
    else:
        card_list = [i[1] for i in DbBase.getData("card")]
        if zk in card_list:
            Fun.MessageBox("该针卡编号已存在")
        else:
            id = DbBase.addcard(zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz)
            GridBase.addCard('Card', 'ListView_8', id, zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz)
            yzq = "新增"
            syq = "新增"
            DbBase.adduse(zk, time_str, user, yzq, yz, syq, sy, td)
            Fun.MessageBox("该针卡编号添加成功")


def Entry_22_onKey(event,uiName,widgetName):
    input_char = Fun.GetText(uiName,widgetName)
    temp_char = ""
    for char in input_char:
        if 48<=ord(char)<=57:
            temp_char = temp_char + char
    Fun.SetText(uiName, widgetName, temp_char)
    pass
    #只输入数字

