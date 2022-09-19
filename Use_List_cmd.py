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
def Button_16_onCommand(uiName,widgetName):
    try:
        value_list = GridBase.getuselist(uiName, 'ListView_2')
        string = '\n'.join([','.join([str(j) for j in i]) for i in value_list])
        name = "probe card list"
        if not os.path.exists(name):
            os.mkdir(name)
        time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        with open(f"{name}\\probe card use list_{time_str}.csv", "w") as f:
            f.write(string)
        Fun.MessageBox("导出成功")
        pass
        #导出当前界面
    except Exception as e:
        Fun.MessageBox(f"Error: {e}")
def Button_15_onCommand(uiName,widgetName):
    try:
        fh = Fun.GetText(uiName, 'ComboBox_11')
        zk = Fun.GetText(uiName, 'Entry_4').strip()
        op = Fun.GetText(uiName, 'Entry_7').strip()
        count = Fun.GetText(uiName, "Entry_12").strip()
        time1 = Fun.GetElement(uiName, "Calendar_21").selection()
        time2 = Fun.GetElement(uiName, "Calendar_22").selection()
        treeview = GridBase.clearData(uiName, 'ListView_2')
        res = DbBase.getData("uselist")
        if zk != "":
            res = [i for i in res if zk in i[1]]
        if op != "":
            res = [i for i in res if op in i[3]]
        if time1 is not None:
            time1 = datetime.datetime.strptime(time1, "%Y-%m-%d")
            res = [i for i in res if datetime.datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S") > time1]
        if time2 is not None:
            time2 = datetime.datetime.strptime(time2, "%Y-%m-%d")
            res = [i for i in res if datetime.datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S") < time2]
        if fh != " ":
            res = eval(f"[i for i in res if i[8] != '' and i[8] {fh} {count}]")
        for item in res:
            treeview.insert('', 'end', values=item)
        pass
        #查询
    except Exception as e:
        Fun.MessageBox(f"Error: {e}")

