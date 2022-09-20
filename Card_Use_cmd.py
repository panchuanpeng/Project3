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
import tkinter.messagebox
DbBase.initcard()
from GetConfig import ConfigInfo
config = ConfigInfo()
close_flag = 0
def close():
	global close_flag
	close_flag = 1
	Fun.GetElement("AddAccount", 'root').destroy()
def Button_4_onCommand(uiName,widgetName):
	try:
		global close_flag
		close_flag = 0
		if Fun.GetText('Project3','Label_3') == "":
			Fun.MessageBox("请先登录,再进行归还!")
			return
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择针卡,再进行领用!")
			return
		if item[5] == "正常":
			Fun.MessageBox("当前状态已归还，无需重复归还!")
			return
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		topLevel.protocol('WM_DELETE_WINDOW', close)
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
		if close_flag == 1:
			return
		password = Fun.GetInputDataArray("AddAccount")['Entry_3'][0]
		if password != Fun.GetUserData('Project3', 'Label_3', 'password'):
			Fun.MessageBox("密码错误")
			return
		# 归还功能区
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import Back
		Back.Back(topLevel)
		Fun.SetText("Back", "Entry_7", item[10])
		Fun.SetText("Back", "Entry_9", item[11])
		tkinter.Tk.wait_window(topLevel)
		InputDataArray = Fun.GetInputDataArray("Back")
		print(InputDataArray)
		# 归还
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_3_onCommand(uiName,widgetName):
	try:
		global close_flag
		close_flag = 0
		if Fun.GetText('Project3','Label_3') == "":
			Fun.MessageBox("请先登录,再进行领用!")
			return
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择针卡,再进行领用!")
			return
		if item[6] != "正常":
			con = tkinter.messagebox.askyesno("警告", f"该针卡已在{item[6]}使用，是否继续领用")
			if not con:
				return
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		topLevel.protocol('WM_DELETE_WINDOW', close)
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
		if close_flag == 1:
			return
		password = Fun.GetInputDataArray("AddAccount")['Entry_3'][0]
		if password != Fun.GetUserData('Project3', 'Label_3', 'password'):
			Fun.MessageBox("密码错误")
			return
		# 领用功能区
		item = DbBase.getcard(item[1])
		zk = item[1]
		tip = item[3]
		yzq = item[5]
		syq = item[6]
		td = item[9]
		wz = item[10]
		bz = item[11]
		time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
		user = Fun.GetText('Project3', 'Label_3')
		name = socket.gethostname()
		item = GridBase.takeoutcard(uiName,'ListView_8',name)
		DbBase.takeoutcard(item[0], name)
		DbBase.adduse(zk, time_str, user,tip, yzq, yzq, syq, name, td, wz, bz)
		Fun.MessageBox("领用成功")
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
		treeview.tag_configure("tag_green", background="#00ff00")
		treeview.tag_configure("tag_red", background="red")
		treeview.tag_configure("tag_y", background="#ff8000")
		res = DbBase.getData("card")
		res = [i for i in res if "验证OK" in i[5]]
		for state in config.ComboBox["sy"][1:]:
			res = [i for i in res if state != i[6]]
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
			if item[5] == "验证OK":
				if item[6] not in config.ComboBox["sy"]:
					treeview.insert('', 'end', values=item, tags="tag_green")
				elif item[6] in config.ComboBox["sy"][1:]:
					treeview.insert('', 'end', values=item, tags="tag_red")
				else:
					treeview.insert('', 'end', values=item)
			elif item[5] == "等待验证":
				treeview.insert('', 'end', values=item, tags="tag_y")
			else:
				treeview.insert('', 'end', values=item, tags="tag_red")
		# 查询
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_22_onCommand(uiName,widgetName):
	pass
	# NI计数

