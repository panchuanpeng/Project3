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
DbBase.initcard()
def Button_4_onCommand(uiName,widgetName):
	try:
		entry_list = 'Entry_8,Entry_9,Entry_10,Entry_11,ComboBox_26,ComboBox_27,Entry_14,Entry_15,Entry_16,Entry_17,Entry_18'.split(",")
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择数据,在进行修改!")
			return
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import Add
		Add.Add(topLevel)
		Fun.SetText("Add", "Button_14", "修改")
		for index,entry in enumerate(entry_list):
			Fun.SetText("Add", entry, item[index+1])
		Fun.GetElement("Add", 'Entry_8')["state"] = "disabled"
		tkinter.Tk.wait_window(topLevel)
		InputDataArray=Add.Fun.GetInputDataArray(uiName)
		print(InputDataArray)
		# 修改
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_5_onCommand(uiName,widgetName):
	try:
		item = GridBase.deleteSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择数据,在进行删除!")
			return
		DbBase.deletecard(item[0])
		# 删除
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_6_onCommand(uiName,widgetName):
	try:
		treeview = GridBase.clearData(uiName, 'ListView_8')
		res = DbBase.getData("card")
		for item in res:
			treeview.insert('', 'end', values=item)
		# 加载全部
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_3_onCommand(uiName,widgetName):
	try:
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import Add
		Add.Add(topLevel)
		tkinter.Tk.wait_window(topLevel)
		InputDataArray=Add.Fun.GetInputDataArray(uiName)
		print(InputDataArray)
		# 增加
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_2_onCommand(uiName,widgetName):
	try:
		fh = Fun.GetText(uiName, 'ComboBox_14')
		zk = Fun.GetText(uiName, "Entry_15").strip()
		vd = Fun.GetText(uiName, "Entry_16").strip()
		zt = Fun.GetText(uiName, 'ComboBox_17')
		cp = Fun.GetText(uiName, "Entry_18").strip()
		count = Fun.GetText(uiName, "Entry_19").strip()
		treeview = GridBase.clearData(uiName, 'ListView_8')
		res = DbBase.getData("card")
		if zk != "":
			res = [i for i in res if zk in i[1]]
		if vd != "":
			res = [i for i in res if vd in i[4]]
		if zt != "ALL":
			res = [i for i in res if zt in i[5]]
		if cp != "":
			res = [i for i in res if cp in i[7]]
		if fh != " ":
			res = eval(f"[i for i in res if i[9] != '' and i[9] {fh} {count}]")
		print(res)
		for item in res:
			treeview.insert('', 'end', values=item)
		# 查询
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_20_onCommand(uiName,widgetName):
	value_list = GridBase.getallData(uiName, 'ListView_8')
	string = '\n'.join([','.join([str(j) for j in i]) for i in value_list])
	name = "probe card list"
	if not os.path.exists(name):
		os.mkdir(name)
	time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
	with open(f"{name}\\{name}_{time_str}.csv", "w") as f:
		f.write(string)
	Fun.MessageBox("导出成功")
	pass
	# 导出当前界面
def Button_21_onCommand(uiName,widgetName):
	pass
	# 导出针卡使用记录

