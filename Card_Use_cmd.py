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
import socket
import datetime
DbBase.initcard()
def Button_4_onCommand(uiName,widgetName):
	try:
		# if Fun.GetText('Project3','Label_3') == "":
		# 	Fun.MessageBox("请先登录,再进行领用!")
		# 	return
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择针卡,再进行领用!")
			return
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import AddAccount
		AddAccount.AddAccount(topLevel)
		Fun.SetText("AddAccount", 'Button_6', '确认')
		Fun.SetText("AddAccount", 'Entry_2', Fun.GetText('Project3', 'Label_3'))
		Fun.GetElement("AddAccount", 'Entry_2')["state"] = "disabled"
		Fun.GetElement("AddAccount", 'Label_8').destroy()
		Fun.GetElement("AddAccount", 'Label_9').destroy()
		Fun.GetElement("AddAccount", 'Entry_10').destroy()
		Fun.GetElement("AddAccount", 'Entry_11').destroy()
		tkinter.Tk.wait_window(topLevel)
		print(Fun.GetUserData('Project3', 'Label_3', 'password'))
		print(Fun.GetInputDataArray("AddAccount")['Entry_3'])
		password = Fun.GetInputDataArray("AddAccount")['Entry_3'][0]
		if '""' == Fun.GetUserData('Project3', 'Label_3', 'password'):
			# 领用功能区
			name = "未使用"
			item = GridBase.takeoutcard(uiName, 'ListView_8', name)
			DbBase.takeoutcard(item[0], name)
			Fun.MessageBox("领用成功")
		else:
			Fun.MessageBox("密码错误")
		# 领用
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_3_onCommand(uiName,widgetName):
	try:
		# if Fun.GetText('Project3','Label_3') == "":
		# 	Fun.MessageBox("请先登录,再进行领用!")
		# 	return
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择针卡,再进行领用!")
			return
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import AddAccount
		AddAccount.AddAccount(topLevel)
		Fun.SetText("AddAccount", 'Button_6', '确认')
		Fun.SetText("AddAccount", 'Entry_2', Fun.GetText('Project3','Label_3'))
		Fun.GetElement("AddAccount", 'Entry_2')["state"] = "disabled"
		Fun.GetElement("AddAccount", 'Label_8').destroy()
		Fun.GetElement("AddAccount", 'Label_9').destroy()
		Fun.GetElement("AddAccount", 'Entry_10').destroy()
		Fun.GetElement("AddAccount", 'Entry_11').destroy()
		tkinter.Tk.wait_window(topLevel)
		print(Fun.GetUserData('Project3','Label_3','password'))
		print(Fun.GetInputDataArray("AddAccount")['Entry_3'])
		password = Fun.GetInputDataArray("AddAccount")['Entry_3'][0]
		if '""' == Fun.GetUserData('Project3','Label_3','password'):
			# 领用功能区
			name = socket.gethostname()
			item = GridBase.takeoutcard(uiName,'ListView_8',name)
			DbBase.takeoutcard(item[0],name)
			Fun.MessageBox("领用成功")
		else:
			Fun.MessageBox("密码错误")
		# 领用
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_2_onCommand(uiName,widgetName):
	try:
		fh = Fun.GetText(uiName, 'ComboBox_14')
		zk = Fun.GetText(uiName, "Entry_15").strip()
		vd = Fun.GetText(uiName, "Entry_16").strip()
		cp = Fun.GetText(uiName, "Entry_18").strip()
		count = Fun.GetText(uiName, "Entry_19").strip()
		treeview = GridBase.clearData(uiName, 'ListView_8')
		res = DbBase.getData("card")
		res = [i for i in res if "验证OK" in i[5]]
		if zk != "":
			res = [i for i in res if zk in i[1]]
		if vd != "":
			res = [i for i in res if vd in i[4]]
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

