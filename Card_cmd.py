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
			Fun.MessageBox("请先登录,再进行修改!")
			return
		entry_list = 'Entry_8,Entry_9,Entry_10,Entry_11,ComboBox_26,ComboBox_27,Entry_14,Entry_15,Entry_16,Entry_17,Entry_18'.split(",")
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择数据,再进行修改!")
			return
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
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import Add
		Add.Add(topLevel)
		Fun.SetText("Add", "Button_14", "修改")
		item = DbBase.getcard(item[1])
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
		global close_flag
		close_flag = 0
		if Fun.GetText('Project3','Label_3') == "":
			Fun.MessageBox("请先登录,再进行删除!")
			return
		item = GridBase.getSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择数据,在进行删除!")
			return
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
		time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
		user = Fun.GetText('Project3', 'Label_3')
		item = GridBase.deleteSelected(uiName, 'ListView_8')
		item = DbBase.getcard(item[1])
		DbBase.adduse(item[1], time_str, user, item[3], item[5], "删除", item[6], "删除", item[9], item[10], item[11])
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
		if Fun.GetText('Project3','Label_3') == "":
			Fun.MessageBox("请先登录,再进行增加!")
			return
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import Add
		Add.Add(topLevel)
		tkinter.Tk.wait_window(topLevel)
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
		wz = Fun.GetText(uiName, "Entry_23").strip()
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
			print(res)
		if wz != "":
			res = [i for i in res if wz in i[10]]
		if fh != " ":
			res = eval(f"[i for i in res if i[9] != '' and i[9] {fh} {count}]")
		if not res:
			Fun.MessageBox("未找到相关数据")
			return
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
def Button_20_onCommand(uiName,widgetName):
	try:
		value_list = GridBase.getallData(uiName, 'ListView_8')
		string = '\n'.join([','.join([str(j) for j in i]) for i in value_list])
		name = "probe card list"
		if not os.path.exists(name):
			os.mkdir(name)
		time_str = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
		with open(f"{name}\\{name}_{time_str}.csv", "w") as f:
			f.write(string)
		os.startfile(f"{name}\\{name}_{time_str}.csv")
		Fun.MessageBox("导出成功")
		pass
		# 导出当前界面
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")
def Button_21_onCommand(uiName,widgetName):
	try:
		global close_flag
		close_flag = 0
		if Fun.GetText('Project3', 'Label_3') == "":
			Fun.MessageBox("请先登录,再进行修改!")
			return
		entry_list = 'Entry_8,Entry_9,Entry_10,Entry_11,ComboBox_26,ComboBox_27,Entry_14,Entry_15,Entry_16,Entry_17,Entry_18'.split(
			",")
		item = GridBase.getallSelected(uiName, 'ListView_8')
		if (item == None):
			Fun.MessageBox("请先选择数据,再进行修改!")
			return
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
		sys.path.append("E:/github/TKinterDesigner-master/Project3")
		topLevel = tkinter.Toplevel()
		topLevel.attributes("-toolwindow", 1)
		topLevel.wm_attributes("-topmost", 1)
		import Add
		Add.Add(topLevel)
		Fun.SetText("Add", "Button_14", "批量修改")
		for index, entry in enumerate(entry_list):
			Fun.SetText("Add", entry, "")
		Fun.GetElement("Add", 'Entry_8')["state"] = "disabled"
		tkinter.Tk.wait_window(topLevel)
		InputDataArray = Add.Fun.GetInputDataArray(uiName)
		print(InputDataArray)
		# 批量修改
		pass
	except Exception as e:
		Fun.MessageBox(f"Error: {e}")

